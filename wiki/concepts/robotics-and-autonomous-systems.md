---
title: Robotics and autonomous systems — the sense–plan–act loop and its architectures (subsumption, hierarchical, behaviour trees), rigid-body kinematics (configuration space, transforms, forward/inverse kinematics, Jacobians), dynamics (Lagrangian/Newton–Euler, underactuation), perception for robots (depth, point clouds, ICP, pose estimation, tactile), grasping and manipulation, mobile robots and self-driving stacks, learning for robotics (imitation, RL, sim-to-real, diffusion policies, foundation models), simulation (Drake, MuJoCo, Isaac), and safety
type: concept
section: "6.10"
level: 400
tags: [robotics, autonomous-systems, sense-plan-act, subsumption, brooks, behavior-trees, hierarchical-control, kinematics, configuration-space, rigid-body-transforms, se3, rotations, quaternions, forward-kinematics, inverse-kinematics, jacobian, differential-ik, singularities, dynamics, lagrangian, newton-euler, manipulator-equation, underactuated, fully-actuated, nonholonomic, perception, depth-cameras, point-clouds, icp, pose-estimation, tactile, grasping, grasp-planning, manipulation, force-control, impedance-control, mobile-robots, self-driving, autonomy-stack, localization, mapping, slam, learning-for-robotics, imitation-learning, behavior-cloning, diffusion-policy, sim-to-real, domain-randomization, robot-foundation-models, vla, simulation, drake, mujoco, isaac, urdf, ros, safety, tedrake, thrun]
sources: [robotics-texts-courses-and-seminal-papers]
summary: A robot closes a loop between sensing, estimating the state of itself and the world, deciding, and acting through motors — and robotics is the engineering of every stage under uncertainty and physical contact: kinematics describes configurations and motion (rigid-body transforms in SE(3), forward kinematics from joint angles to end-effector pose, inverse kinematics by numerical optimization, the Jacobian relating joint velocities to end-effector velocities and its singularities), dynamics gives the manipulator equation M(q)q̈ + C(q, q̇)q̇ + g(q) = τ and the distinction between fully-actuated systems (which feedback can make do anything) and underactuated ones (walkers, quadrotors, everything that must exploit its dynamics), perception turns cameras/depth/LiDAR/tactile into poses and maps (point clouds, ICP, learned detectors, SLAM), planning and control (motion-planning-and-control) produce trajectories and torques, and architectures organize it — Brooks' subsumption (layered reactive behaviours, no central model) against sense–plan–act, resolved today as hierarchies with fast reactive controllers under slower planners and behaviour trees for task logic; manipulation adds contact (grasp planning, force/impedance control, bin picking) and is Tedrake's "more than pick-and-place"; mobile robots and self-driving cars stack localization, mapping, perception, prediction, planning and control with redundancy and validation; learning has moved from tuned models to imitation (behaviour cloning, diffusion policies), RL with sim-to-real transfer (domain randomization, system identification) and vision-language-action foundation models; simulation (Drake, MuJoCo, Isaac) is where design, testing and most training happen; and safety — physical, functional, and verified — is the constraint the other fields don't have.
---
# Robotics and autonomous systems

**In one sentence.** A robot is a control loop through the physical world — estimate the
state, plan, act, repeat at hundreds of hertz — and every part of it (kinematics, dynamics,
perception, planning, learning) is CS made harder by contact, uncertainty, and the fact
that mistakes break things.

## Architectures (Brooks 1986; Poole & Mackworth ch. 2; Tedrake Manipulation ch. 1)
**Sense–plan–act** (Shakey, 1960s–80s): build a world model, plan in it, execute — slow and
brittle when the model is wrong. **Subsumption** (Brooks): layers of simple behaviours
(avoid → wander → explore → map) each a finite-state machine wired to sensors and actuators;
higher layers subsume lower ones; no central representation ("the world is its own best
model") — fast, robust, hard to scale to tasks needing reasoning. Modern practice is
**hierarchical**: reactive controllers at 1 kHz (joint torque, balance), whole-body/motion
controllers at 100 Hz, planners at 1–10 Hz, task logic as **behaviour trees** or state
machines, with a **world model** shared through a middleware (**ROS 2** topics/services/
actions; real-time executors — [[real-time-scheduling]], [[cyber-physical-systems-and-models-of-computation]]).
Tedrake's framing: "manipulation is more than pick-and-place" — open-world manipulation
needs perception, planning, control and learning together, developed in simulation
(**Drake**) with model-based design and analysis.

## Kinematics (Lynch & Park ch. 2–6; CS223A)
**Configuration** q ∈ configuration space (joint angles for arms — dimension = DOF; SE(2)/
SE(3) for mobile bases/drones); **rigid-body transforms** T = [R t; 0 1] ∈ SE(3) compose
(ᴬTᶜ = ᴬTᴮ ᴮTᶜ — keep the frames straight; Tedrake's "spatial algebra" notation); rotations as
matrices, axis–angle/exponential coordinates, **quaternions** (no gimbal lock — [[matrices-and-linear-maps]]);
**screw theory**: any rigid motion is a rotation about + translation along an axis, so
**forward kinematics** is a **product of exponentials** T(q) = e^{[S₁]q₁} … e^{[Sₙ]qₙ} M (or DH
parameters); **inverse kinematics**: closed form for 6-DOF wrists, else numerical
optimization (Newton/least squares with constraints, joint limits, multiple solutions —
[[nonlinear-optimization]]). **Jacobian** J(q): ẋ = J(q) q̇ maps joint velocities to end-
effector twist; **differential IK**: q̇ = J⁺ ẋ_desired (pseudoinverse; damped least squares
near **singularities** where J loses rank — [[svd-and-pca]]), QP formulations with limits;
statics by duality: τ = Jᵀ F; **manipulability** ellipsoids. Redundant arms (7-DOF) use the
null space for secondary objectives.

## Dynamics and actuation (Underactuated ch. 1–3; Lynch & Park ch. 8)
**Manipulator equation** M(q) q̈ + C(q, q̇) q̇ + g(q) = τ + Jᵀ F_ext (mass matrix, Coriolis/
centrifugal, gravity) from Lagrangian mechanics L = T − V or recursive Newton–Euler (O(n)).
**Fully actuated** (rank of the control input = DOF): feedback linearization (computed
torque τ = M(q) v + C q̇ + g) makes any dynamics behave as you like — so for arms the hard
problems are perception and contact, not control. **Underactuated** (fewer actuators than
DOF, or input limits): walkers, quadrotors (4 inputs, 6 DOF), cart-poles, acrobots,
anything falling or floating — must exploit natural dynamics (passive walkers walk downhill
with no motors; birds vs aircraft); tools: energy shaping (pump energy to swing a
torque-limited pendulum up), LQR about trajectories, trajectory optimization, Lyapunov
analysis, hybrid dynamics for contact ([[motion-planning-and-control]]). **Nonholonomic**
constraints (a car can't slide sideways) restrict velocities not configurations. Actuators:
electric motors with gearboxes (backdrivability, reflected inertia; torque- vs position-
controlled — Tedrake ch. 2), hydraulics, series-elastic and quasi-direct-drive for legged
robots; sensors: encoders, IMUs, force/torque, cameras, depth (structured light, ToF,
stereo), LiDAR, tactile skins.

## Perception for robots (Tedrake Manipulation ch. 4–5; [[computer-vision-fundamentals]])
Depth cameras → **point clouds** (in the camera frame; transform to world with calibrated
extrinsics — [[multiple-view-geometry-and-3d-vision]]); **ICP** (iterative closest point:
alternate correspondence and least-squares rigid alignment — the SVD/Kabsch solution;
local minima, outliers → RANSAC/robust kernels) for pose estimation of known geometry;
learned **object detection/segmentation** (Mask R-CNN, SAM) and 6-DoF pose networks;
scene representations (occupancy grids, TSDFs, NeRF/Gaussian splats for manipulation);
**tactile** sensing (GelSight) for contact-rich tasks; sensor fusion and state estimation —
[[state-estimation-and-kalman-filters]]; SLAM for mobile robots. Perception uncertainty is
the main reason manipulation is hard: a 5 mm pose error is a failed grasp.

## Grasping, manipulation, and contact — why is it hard for a robot arm to pick things up reliably? (Tedrake ch. 5–8; Lynch & Park ch. 12)
Grasp quality (force closure, friction cones, antipodal grasps), grasp planning by
geometry (point-cloud normals — the Tedrake bin-picking pipeline) or learned grasp
networks (Dex-Net, GraspNet); **force control**: hybrid position/force, **impedance/admittance**
control (make the arm behave like a spring–damper for safe contact); contact dynamics are
hybrid and non-smooth (complementarity, friction — simulators approximate), which is why
learning and simulation matter; dexterous in-hand manipulation (OpenAI's Rubik's cube via
RL + domain randomization); deformable objects (cloth, cables) as the frontier.

## Mobile robots and self-driving (Thrun et al.; Toronto course)
Wheeled kinematics (differential drive, Ackermann), legged locomotion (ZMP walking, hybrid
zero dynamics, MPC + RL — Boston Dynamics, ANYmal, Unitree), aerial (quadrotor control,
differential flatness). **Autonomy stack**: localization (GPS/IMU/LiDAR/maps — [[state-estimation-and-kalman-filters]]),
HD/semantic mapping, perception (3D detection from LiDAR + cameras, tracking), **prediction**
of other agents (multimodal trajectory forecasting), **planning** (behaviour planning →
trajectory optimization with constraints — [[motion-planning-and-control]]), control
(MPC/PID on the vehicle), plus simulation, scenario testing, redundancy, and end-to-end
learned alternatives (imitation from fleet data). Waymo/Tesla/Cruise as the case studies:
long-tail scenarios, validation (miles are not enough — scenario-based), remote assistance.

## Learning for robotics (Levine et al. 2016; Chi et al. 2023; RT-2/π0)
Why learning: perception and contact are hard to model. **Imitation learning** — behaviour
cloning from teleoperation (ALOHA, VR), **DAgger** for compounding errors, **diffusion
policies** (model the action distribution as a denoising process — multimodal demonstrations,
the current default — [[deep-generative-models]]), action chunking; **RL** — sample-hungry,
so mostly in **simulation** with **sim-to-real** transfer (domain randomization of physics/
visuals, system identification, real-world fine-tuning; legged locomotion is the success
story — [[deep-reinforcement-learning]]); **end-to-end visuomotor** policies (Levine 2016: pixels
→ torques via guided policy search); **foundation models**: vision-language-action models
(RT-1/RT-2, OpenVLA, π0) pretrained on internet + cross-embodiment robot data, language-
conditioned tasks, LLM task planners calling skills ([[large-language-models]] agents with
a body); the data bottleneck (no internet of robot experience) drives teleoperation
fleets, simulation at scale, and video pretraining. **Simulators**: Drake (contact-accurate,
optimization-friendly), MuJoCo (fast RL), Isaac Sim/Lab (GPU-parallel), PyBullet, Gazebo
(ROS); the sim-to-real gap is the tax on all of them.

## Safety and verification
Physical safety (collision avoidance, speed/force limits — ISO 10218/15066 for cobots),
functional safety (watchdogs, redundant sensing, safe states — [[cyber-physical-systems-and-models-of-computation]]),
formal guarantees (reachability analysis, control barrier functions, Lyapunov certificates
— [[motion-planning-and-control]]; [[model-checking]] for discrete logic), and the open
problem of verifying learned components; human–robot interaction and shared autonomy.

## Pitfalls
- Frame confusion (which frame is the transform expressed in) — the most common robotics
  bug; Euler angles near gimbal lock.
- Jacobian pseudoinverse at singularities without damping (joint velocities explode).
- Controlling an underactuated system as if feedback linearization applied.
- Trusting simulation contact physics; training in sim without randomization.
- Evaluating a learned policy on the demonstrations' distribution only.
- Ignoring latency and timing in the loop (the controller "works" at 1 kHz, not at 30 Hz).

## Related
- [[motion-planning-and-control]], [[state-estimation-and-kalman-filters]],
  [[multiple-view-geometry-and-3d-vision]], [[computer-vision-fundamentals]],
  [[deep-reinforcement-learning]], [[markov-decision-processes]], [[deep-generative-models]],
  [[large-language-models]], [[real-time-scheduling]],
  [[cyber-physical-systems-and-models-of-computation]], [[matrices-and-linear-maps]],
  [[svd-and-pca]], [[nonlinear-optimization]], [[model-checking]],
  [[intelligent-agents-and-ai-history]] (agent architectures).

## Sources
Tedrake, *Robotic Manipulation* ch. 1–2 (read), 3–8 (from the book); Tedrake, *Underactuated Robotics* ch. 1–3 (read); Lynch & Park ch. 2–8, 12; Thrun, Burgard & Fox; Brooks 1986; Levine et al. 2016; Chi et al. 2023; Brohan et al. 2023 (RT-2); Black et al. 2024 (π0); Khatib 1987 (operational space).
