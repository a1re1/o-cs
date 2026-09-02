---
title: State estimation and Kalman filters — the Bayes filter, the Kalman filter (predict/update, gain, covariance; optimal for linear-Gaussian systems), extended and unscented Kalman filters for nonlinear models, information filters, particle filters and Monte Carlo localization, sensor fusion (IMU + GPS + vision/LiDAR), motion and measurement models, occupancy-grid mapping, and SLAM (EKF-SLAM, GraphSLAM/factor graphs, FastSLAM, loop closure, data association)
type: concept
section: "6.10"
level: 500
tags: [state-estimation, bayes-filter, recursive-estimation, kalman-filter, predict-update, kalman-gain, covariance, linear-gaussian, process-noise, measurement-noise, innovation, extended-kalman-filter, ekf, linearization, unscented-kalman-filter, ukf, sigma-points, information-filter, particle-filter, monte-carlo-localization, mcl, resampling, importance-weights, sensor-fusion, imu, gps, odometry, dead-reckoning, motion-model, measurement-model, beam-model, likelihood-field, occupancy-grid, mapping, slam, ekf-slam, graphslam, factor-graphs, pose-graph, least-squares, isam, gtsam, fastslam, rao-blackwellized, loop-closure, data-association, landmarks, visual-inertial-odometry, thrun, kalman-1960]
sources: [robotics-texts-courses-and-seminal-papers]
summary: Every robot estimates a state it cannot observe directly from noisy sensors and a model of its own motion, and the unifying algorithm is the Bayes filter — predict the belief forward through the motion model, then multiply by the measurement likelihood and normalize — instantiated by representation: the Kalman filter (Kalman 1960) keeps a Gaussian mean and covariance and is the exact, optimal (minimum-variance) Bayes filter for linear dynamics with Gaussian noise, alternating a predict step (x̂ ← Ax̂ + Bu, P ← APAᵀ + Q) and an update that weights the innovation (measurement minus prediction) by the Kalman gain K = PHᵀ(HPHᵀ + R)⁻¹ — a precision-weighted average of prediction and measurement; the extended KF linearizes nonlinear motion/measurement models with Jacobians (works when errors stay small; diverges when they don't), the unscented KF propagates deterministically chosen sigma points instead (no Jacobians, better for strong nonlinearity), information filters carry the inverse covariance (sparse for SLAM), and particle filters represent arbitrary multimodal beliefs by weighted samples — Monte Carlo localization solves global localization and kidnapping that Gaussians cannot; sensor fusion combines IMU integration (fast, drifting), wheel odometry, GPS, and vision/LiDAR in one filter with consistent noise models; mapping builds occupancy grids by log-odds updates, and SLAM estimates the map and pose jointly — EKF-SLAM with landmarks (O(n²) covariance), FastSLAM's Rao-Blackwellized particles (a map per particle), and the modern standard, GraphSLAM/factor graphs: poses and landmarks as nodes, odometry/observations/loop closures as factors, solved as sparse nonlinear least squares (Gauss–Newton/Levenberg–Marquardt, incremental iSAM/GTSAM) — where loop-closure detection and data association decide whether the map is consistent or corrupted.
---
# State estimation and Kalman filters

**In one sentence.** Predict where you are from where you were and what you did, correct
with what you see, weighted by how much you trust each — the Kalman filter does this
exactly for Gaussians, particle filters for anything, and SLAM does it for the map and the
robot at once as one big sparse least-squares problem.

## The Bayes filter (Thrun et al. ch. 2; [[bayesian-networks-and-hmms]])
State xₜ (pose, velocity, biases, map), controls uₜ, measurements zₜ. **Belief** bel(xₜ) =
p(xₜ | z₁:ₜ, u₁:ₜ); recursion: **predict** b̄el(xₜ) = ∫ p(xₜ | uₜ, xₜ₋₁) bel(xₜ₋₁) dxₜ₋₁ (motion
model — belief spreads), **update** bel(xₜ) = η p(zₜ | xₜ) b̄el(xₜ) (measurement model — belief
sharpens). Markov assumptions: the state is complete; measurements depend only on the
current state. Every filter below is this recursion with a different belief
representation; the HMM forward algorithm is the discrete case. **Motion models**
(velocity/odometry models with noise growing with motion; IMU integration of angular rate
and acceleration with bias states — dead reckoning drifts quadratically); **measurement
models** (range/bearing to landmarks; LiDAR beam models and likelihood fields against a
map; camera reprojection — [[multiple-view-geometry-and-3d-vision]]; GPS with covariance).
Noise models matter more than algorithms: an overconfident covariance is the usual bug.

## The Kalman filter (Kalman 1960; Thrun et al. ch. 3)
Linear-Gaussian system: xₜ = A xₜ₋₁ + B uₜ + εₜ (εₜ ~ N(0, Q)), zₜ = H xₜ + δₜ (δₜ ~ N(0, R));
belief N(x̂, P). **Predict**: x̂⁻ = A x̂ + B u; P⁻ = A P Aᵀ + Q. **Update**: innovation y = z − H x̂⁻,
innovation covariance S = H P⁻ Hᵀ + R, **Kalman gain** K = P⁻ Hᵀ S⁻¹, x̂ = x̂⁻ + K y, P = (I − KH) P⁻
(Joseph form for numerical stability). Interpretation: the posterior mean is a precision-
weighted average of prediction and measurement ([[bayesian-inference]] Normal–Normal
conjugacy applied recursively); K → 0 when the measurement is noisy (R large), K → H⁻¹ when
the prediction is uncertain. Properties: exact Bayes filter for linear-Gaussian models;
minimum-variance among linear estimators even for non-Gaussian noise; O(n³) per step in
the state dimension (n ≈ 15 for a pose + velocity + IMU bias state — trivial). Extensions:
Kalman smoother (RTS — use future data, [[bayesian-networks-and-hmms]] forward–backward),
multiple-model filters (IMM for manoeuvring targets — tracking in [[computer-vision-fundamentals]]),
outlier gating by innovation χ² tests, adaptive Q/R.

## EKF and UKF (Thrun et al. ch. 3.3–3.4)
Real models are nonlinear: xₜ = g(uₜ, xₜ₋₁), zₜ = h(xₜ). **EKF**: linearize at the current
estimate — G = ∂g/∂x, Hₜ = ∂h/∂x — and run the KF equations with them; simple, fast, the
workhorse (GPS/INS, attitude estimation, early SLAM); fails when the linearization is bad
(large uncertainty, strong curvature — bearing-only measurements, wrap-around angles),
and it is inconsistent (overconfident) under repeated linearization; error-state
formulations for rotations (quaternions on the manifold — [[robotics-and-autonomous-systems]]).
**UKF**: pick 2n+1 **sigma points** around the mean (deterministic, spread by the
covariance), push them through g and h, recover mean/covariance from the transformed
points — captures the posterior to second order without Jacobians, same cost order;
better for strong nonlinearity, still unimodal Gaussian. **Information filter**: track Ω =
P⁻¹, ξ = Ω x̂ — the update is additive (measurements add information), prediction is expensive;
sparsity of Ω is what makes GraphSLAM scale.

## Particle filters and Monte Carlo localization (Dellaert et al. 1999; Thrun et al. ch. 4, 8)
Represent bel by N weighted particles (samples of x) — arbitrary, multimodal beliefs
([[monte-carlo-methods]] sequential Monte Carlo). Loop: sample each particle's motion from
the motion model, weight by p(z | x), **resample** proportional to weight (low-variance/
systematic resampling; resample only when ESS drops; add a few random particles for
recovery). **MCL**: global localization from an unknown start in a known map (particles
converge from everywhere to the true pose — impossible for a Gaussian), the **kidnapped
robot** problem, non-Gaussian LiDAR likelihoods; KLD-sampling adapts N; cost O(N) per step
with N ~ 10³–10⁵. Failure modes: particle deprivation (the true pose has no particle),
degeneracy without resampling, and high-dimensional states (curse of dimensionality — hence
Rao-Blackwellization: sample only the pose, keep Gaussians/grids for the rest).

## Sensor fusion in practice
A typical estimator fuses **IMU** (200–1000 Hz gyro + accelerometer, integrated in the
predict step with bias states), **wheel odometry**, **GPS/GNSS** (1–10 Hz, metres of noise,
outages; RTK for cm), magnetometers, barometers, **vision** (VIO: visual–inertial odometry —
feature tracks as measurements, tightly coupled MSCKF/optimization-based — ARKit/ARCore),
**LiDAR** odometry (scan matching/ICP); time synchronization and latency compensation are
half the engineering; consistency checks (NEES/NIS) validate the covariance;
[[cyber-physical-systems-and-models-of-computation]] for the timing. Attitude estimation
(complementary/Madgwick filters) is the cheap special case on every drone.

## Mapping and SLAM (Smith, Self & Cheeseman 1990; Thrun et al. ch. 9–13; Grisetti et al. 2010)
**Occupancy grids** with known poses: each cell's log-odds updated by inverse sensor
models; ray casting; 3D voxels/octrees (OctoMap), TSDFs, semantic maps. **SLAM**: estimate
pose *and* map when neither is known — errors in one corrupt the other, and the joint
posterior is what makes it consistent. **EKF-SLAM**: state = pose + all landmark positions;
covariance O(n²) and full updates O(n²) per step — hundreds of landmarks max, and
inconsistency from linearization; correlations between landmarks are the key insight (the
"stochastic map"). **FastSLAM**: Rao-Blackwellized particle filter — each particle is a
trajectory hypothesis with its own map of independent EKF landmarks (or grid); O(N log n);
handles data-association ambiguity per particle. **GraphSLAM / factor graphs** (the modern
default — g2o, GTSAM, Ceres): nodes = poses (and landmarks), factors = odometry, landmark
observations, GPS, IMU preintegration, **loop closures**; MAP estimate = nonlinear least
squares Σ ‖eᵢ(x)‖²_{Ωᵢ} solved by Gauss–Newton/Levenberg–Marquardt exploiting sparsity
(Cholesky on the sparse information matrix — [[sparse-linear-algebra]], [[nonlinear-optimization]];
the same machinery as bundle adjustment — [[multiple-view-geometry-and-3d-vision]]);
**incremental** solvers (iSAM2 with the Bayes tree) for online use; **pose-graph SLAM** marginalizes
landmarks into relative-pose constraints. **Loop closure** detection (place recognition:
bag-of-words, learned descriptors, scan context) and **data association** (which landmark is
this? nearest neighbour with Mahalanobis gating, JCBB; wrong associations are catastrophic —
robust kernels/switchable constraints) decide the map's integrity. Visual SLAM systems
(ORB-SLAM, VINS-Mono), LiDAR SLAM (LOAM, Cartographer), and dense/semantic/NeRF-based SLAM
are instances; the "SLAM problem" is considered solved for static indoor scenes and open
for dynamic, long-term, and lifelong mapping.

## Pitfalls
- Overconfident noise covariances (the filter rejects correct measurements); Q/R tuned by
  guesswork without NIS checks.
- EKF with large heading uncertainty or angle wrap-around bugs; linearizing at a stale
  estimate.
- Particle filters with too few particles for the state dimension; resampling every step.
- Fusing measurements with unmodelled correlations or wrong timestamps.
- Loop closures accepted without verification (a single false positive folds the map).

## Related
- [[bayesian-networks-and-hmms]], [[monte-carlo-methods]], [[bayesian-inference]],
  [[probabilistic-graphical-models]] (factor graphs), [[multiple-view-geometry-and-3d-vision]],
  [[robotics-and-autonomous-systems]], [[motion-planning-and-control]],
  [[computer-vision-fundamentals]], [[sparse-linear-algebra]], [[nonlinear-optimization]],
  [[cyber-physical-systems-and-models-of-computation]], [[matrices-and-linear-maps]].

## Sources
Kalman 1960; Thrun, Burgard & Fox 2005 ch. 2–4, 7–13; Smith, Self & Cheeseman 1990; Dellaert et al. 1999; Montemerlo et al. 2002 (FastSLAM); Grisetti, Kümmerle, Stachniss & Burgard 2010 (graph-based SLAM tutorial); Kaess et al. 2012 (iSAM2); Mourikis & Roumeliotis 2007 (MSCKF); Cadena et al. 2016 (SLAM survey); Julier & Uhlmann 1997 (UKF); Barfoot, *State Estimation for Robotics* 2017.
