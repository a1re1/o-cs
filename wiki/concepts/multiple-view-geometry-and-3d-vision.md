---
title: Multiple-view geometry and 3D vision — projective geometry and homogeneous coordinates, camera intrinsics/extrinsics and calibration, homographies, epipolar geometry (fundamental and essential matrices, the 8-point algorithm), triangulation, stereo matching and disparity, structure from motion and bundle adjustment, visual SLAM, multi-view stereo, monocular depth, and neural scene representations (NeRF, 3D Gaussian splatting)
type: concept
section: "6.5"
level: 500
tags: [multiple-view-geometry, projective-geometry, homogeneous-coordinates, camera-model, intrinsics, extrinsics, calibration, zhang-calibration, homography, dlt, epipolar-geometry, epipolar-line, fundamental-matrix, essential-matrix, 8-point-algorithm, 5-point, ransac, triangulation, stereo, disparity, rectification, block-matching, semi-global-matching, structure-from-motion, sfm, bundle-adjustment, reprojection-error, levenberg-marquardt, sparse, colmap, visual-slam, orb-slam, loop-closure, pose-graph, multi-view-stereo, mvs, point-clouds, meshes, monocular-depth, nerf, neural-radiance-fields, volume-rendering, 3d-gaussian-splatting, novel-view-synthesis, hartley-zisserman]
sources: [computer-vision-texts-courses-and-seminal-papers]
summary: Recovering 3D from images rests on projective geometry — points and lines in homogeneous coordinates, the camera as a 3×4 matrix P = K[R|t] (intrinsics K from calibration with a checkerboard, extrinsics as pose), planar scenes and pure rotations related between views by a 3×3 homography (fit by DLT from 4 correspondences) — and on epipolar geometry: for two views a point in one image constrains its match to a line in the other, encoded by the fundamental matrix F (x'ᵀFx = 0, 7 dof, estimated from 8+ matches with normalization and RANSAC) or, with known intrinsics, the essential matrix E = [t]ₓR from which relative pose is recovered (5-point algorithm), so that matched points are triangulated into 3D; stereo rectifies two views so matches lie on the same scanline and estimates disparity (depth ∝ baseline·f/disparity) by block matching, semi-global matching or learned cost volumes; structure from motion chains this over many images and refines all cameras and points jointly by bundle adjustment (nonlinear least squares on reprojection error, sparse Levenberg–Marquardt — COLMAP), which in real time with loop closure and pose graphs is visual SLAM; multi-view stereo densifies to point clouds and meshes; monocular depth networks learn priors instead; and neural fields — NeRF (an MLP from position and view direction to colour and density rendered by differentiable volume integration, trained from posed images) and 3D Gaussian splatting (explicit anisotropic Gaussians rasterized in real time) — turned reconstruction into optimizing a differentiable renderer.
---
# Multiple-view geometry and 3D vision

**In one sentence.** Two calibrated views of a rigid scene pin every point to a line in the
other image (epipolar geometry); intersect those constraints to get depth, chain them
over many views and jointly refine (bundle adjustment) to get cameras and structure, and
today fit a differentiable renderer (NeRF, Gaussian splatting) to the same posed images.

## Projective geometry and cameras (H&Z ch. 2–7; Szeliski ch. 2, 11)
**Homogeneous coordinates** make projection linear: 2D point (x, y, 1), line l with lᵀx = 0,
points at infinity (x, y, 0) (vanishing points, horizon); 3D likewise. **Camera**: x ≃ P X,
P = K [R | t] (3×4, 11 dof): **intrinsics** K = [fₓ s cₓ; 0 f_y c_y; 0 0 1] (+ lens
distortion coefficients), **extrinsics** rotation R and translation t (camera pose —
[[matrices-and-linear-maps]], rotations as SO(3)/quaternions). **Calibration** (Zhang 2000):
photograph a planar checkerboard in several poses; each view gives a homography; solve for
K, then refine with distortion by nonlinear least squares (OpenCV `calibrateCamera`).
**Homography** H (3×3, 8 dof) relates two images of a plane, or any two images from a
camera that only rotates (panoramas); estimate by **DLT** from ≥ 4 correspondences (SVD of
a 2n×9 system — [[svd-and-pca]]), normalize coordinates first, wrap in **RANSAC**
([[computer-vision-fundamentals]]). Vanishing points give K from a single image (Manhattan
world); PnP recovers a camera pose from 3D–2D correspondences (P3P + RANSAC — the relocalization
primitive in AR/SLAM).

## Epipolar geometry (H&Z ch. 9–11)
Two cameras: the **epipolar plane** through both centres and X cuts each image in an
**epipolar line**; epipoles are the images of the other camera's centre. **Fundamental
matrix** F (3×3, rank 2, 7 dof): x'ᵀ F x = 0 for all correspondences; l' = F x is the epipolar
line of x. **Estimation**: the **8-point algorithm** (linear from ≥ 8 matches; Hartley's
normalization is essential; enforce rank 2 by SVD), 7-point (minimal), inside RANSAC with
the Sampson error. With known K: **essential matrix** E = Kᵀ' F K = [t]ₓ R (5 dof: rotation +
translation up to scale); decompose E by SVD into 4 (R, t) candidates, choose the one with
points in front of both cameras (cheirality); the **5-point algorithm** (Nistér 2004) is the
minimal solver. **Triangulation**: intersect rays — linear DLT then minimize reprojection
error (the rays never exactly meet). Scale is unobservable from images alone (needs a known
baseline, IMU, or object size). Three views: the trifocal tensor; degeneracies: pure
rotation (F undefined — use H), planar scenes.

## Stereo (Szeliski ch. 12; Scharstein & Szeliski taxonomy)
**Rectify** so epipolar lines are horizontal; for each pixel find the match along the
scanline; **disparity** d = x_L − x_R, depth Z = f·B/d (baseline B) — depth precision degrades
quadratically with distance. Matching costs (SAD/NCC/census over windows), aggregation, and
**global** optimization: dynamic programming per scanline ([[dynamic-programming]]),
graph cuts/belief propagation on an MRF ([[network-flow]]), **semi-global matching** (SGM:
DP along 8–16 directions — the industry standard for real-time stereo); occlusions,
textureless regions, repetitive patterns are the failure cases; **learned stereo** (cost-
volume networks, RAFT-Stereo) dominates benchmarks (KITTI, Middlebury). Active stereo and
structured light (Kinect v1), time-of-flight, and LiDAR are the hardware alternatives.

## Structure from motion and SLAM (Szeliski ch. 11; Triggs et al. 1999; COLMAP 2016)
**SfM** from an unordered photo collection: detect/match features (SIFT — [[computer-vision-fundamentals]])
→ verify pairs geometrically (F/E + RANSAC) → **incremental** reconstruction (initialize with
a good pair, triangulate, register new images by PnP, triangulate new points) → **bundle
adjustment**: minimize Σ ‖xᵢⱼ − π(Pⱼ, Xᵢ)‖² over all cameras and points — a sparse nonlinear
least-squares problem solved by **Levenberg–Marquardt** with the Schur complement exploiting
the camera–point bipartite structure ([[nonlinear-optimization]], [[sparse-linear-algebra]];
Ceres, g2o); global SfM averages rotations then translations. Photo Tourism (2006), "Building
Rome in a Day" (2009), **COLMAP** (Schönberger & Frahm 2016) is the standard pipeline.
**Visual SLAM** — the same in real time from a video stream: tracking (pose per frame),
local mapping, **loop closure** (recognize a revisited place by bag-of-words — [[similarity-search-and-lsh]]
— and correct accumulated drift by **pose-graph** optimization), relocalization; ORB-SLAM
(feature-based), LSD/DSO (direct, photometric), visual–inertial (VINS, ARKit/ARCore fuse
IMU for scale and robustness). Probabilistic framing (EKF-SLAM, particle filters,
factor graphs) is [[robotics-and-autonomous-systems]] / [[state-estimation-and-kalman-filters]].

## Dense reconstruction and neural scene representations (Szeliski ch. 12–14; Mildenhall 2020; Kerbl 2023)
**Multi-view stereo** (PatchMatch MVS, plane sweeps, learned MVSNet) → depth maps → fused
point clouds → meshes (Poisson surface reconstruction, marching cubes, TSDF fusion —
KinectFusion) → textures; representations: point clouds, meshes, voxels/TSDFs, implicit
surfaces (SDFs). **Monocular depth** (MiDaS, Depth Anything): a network learns depth priors
from millions of images — relative depth, metric with calibration. **NeRF**: represent the
scene as F_Θ(x, y, z, θ, φ) → (r, g, b, σ) with an MLP + positional encoding; render a pixel
by **volume rendering** along its ray (numerical integration of transmittance × density ×
colour); train by photometric loss against posed images (poses from COLMAP); photorealistic
novel views with view-dependent effects, slow to train/render → Instant-NGP (hash grids),
Mip-NeRF; dynamic, large-scale, and generative variants (DreamFusion: text-to-3D via
diffusion — [[deep-generative-models]]). **3D Gaussian splatting**: millions of anisotropic
Gaussians with colour/opacity, optimized by differentiable rasterization — real-time
rendering with NeRF quality; the current default for view synthesis. Both are
"reconstruction = inverse rendering by gradient descent" ([[computer-graphics-rendering]]).

## Pitfalls
- Estimating F without coordinate normalization (numerically useless) or without RANSAC.
- Using F (or E) for a pure-rotation or planar scene (degenerate — fit H).
- Wrong chirality choice after decomposing E; forgetting that scale is unobservable.
- Stereo without rectification; trusting disparity at far range.
- Bundle adjustment without a good initialization (local minima); NeRF with bad poses.

## Related
- [[computer-vision-fundamentals]], [[matrices-and-linear-maps]], [[svd-and-pca]],
  [[nonlinear-optimization]], [[sparse-linear-algebra]], [[dynamic-programming]],
  [[network-flow]], [[similarity-search-and-lsh]], [[state-estimation-and-kalman-filters]],
  [[robotics-and-autonomous-systems]], [[computer-graphics-rendering]],
  [[deep-generative-models]], [[convolutional-neural-networks]].

## Sources
Hartley & Zisserman 2e ch. 2–12, 18; Szeliski 2e ch. 2, 11–14 (ToC read); Zhang 2000; Hartley 1997 (normalized 8-point); Nistér 2004; Triggs et al. 1999 (bundle adjustment); Schönberger & Frahm 2016 (COLMAP); Mur-Artal et al. 2015 (ORB-SLAM); Hirschmüller 2008 (SGM); Mildenhall et al. 2020 (NeRF); Kerbl et al. 2023 (3DGS).
