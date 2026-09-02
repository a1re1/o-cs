---
title: Robotics texts, courses and seminal papers — Tedrake's Robotic Manipulation and Underactuated Robotics (free, interactive; MIT 6.4210/6.832), Thrun–Burgard–Fox's Probabilistic Robotics, Lynch & Park's Modern Robotics (free), LaValle's Planning Algorithms (free); Stanford CS223A, Berkeley CS287, UPenn Robotics MOOC, Toronto Self-Driving Cars; Kalman 1960, Smith–Self–Cheeseman SLAM, Monte Carlo localization, RRT, PRM, Levine et al. end-to-end visuomotor, Brooks' subsumption architecture
type: source
section: "6.10"
level: 400
tags: [tedrake, robotic-manipulation, underactuated-robotics, 6-4210, 6-832, drake, thrun, probabilistic-robotics, burgard, fox, lynch-park, modern-robotics, lavalle, planning-algorithms, cs223a, khatib, cs287, abbeel, upenn-robotics, self-driving-cars, kalman, smith-self-cheeseman, slam, monte-carlo-localization, mcl, rrt, prm, kavraki, levine, end-to-end-visuomotor, brooks, subsumption]
sources: []
authors: [Russ Tedrake, Sebastian Thrun, Wolfram Burgard, Dieter Fox, Kevin Lynch, Frank Park, Steven LaValle, Oussama Khatib, Pieter Abbeel, Rudolf Kalman, Randall Smith, Peter Cheeseman, Lydia Kavraki, Sergey Levine, Rodney Brooks]
year: 2005
institution: MIT / Stanford / Berkeley / Northwestern
url: https://manipulation.csail.mit.edu/
license: mixed (Tedrake, Lynch & Park, LaValle free; Thrun et al. commercial)
format: html
summary: Tedrake's two free interactive MIT texts define modern robotics teaching — Robotic Manipulation ("manipulation is more than pick-and-place"; open-world manipulation; simulation and model-based design in Drake; robot description files, position- vs torque-controlled arms, hands and grippers, sensors; then kinematics, geometric perception, differential kinematics, grasping, mobile manipulation, and learning-based approaches) and Underactuated Robotics (fully-actuated vs underactuated systems — ASIMO vs passive walkers, birds vs aircraft; feedback equivalence; nonholonomic constraints; the simple pendulum with energy shaping; acrobots, cart-poles and quadrotors; then dynamic programming, LQR, Lyapunov analysis, trajectory optimization, motion planning, feedback motion planning, and policy search/RL); Probabilistic Robotics is the reference for recursive Bayesian state estimation (Kalman/EKF/UKF, particle filters, localization, mapping, SLAM — EKF, GraphSLAM, FastSLAM — and POMDP planning); Modern Robotics is the screw-theory kinematics/dynamics/control text; LaValle's Planning Algorithms the encyclopaedia of motion planning (configuration space, sampling-based planning, differential constraints, decision-theoretic planning); CS223A (Khatib) teaches kinematics, dynamics and operational-space control, CS287 (Abbeel) advanced robotics with estimation and RL; and the seminal papers are Kalman's filter (1960), Smith–Self–Cheeseman's stochastic map (1990, SLAM's origin), Monte Carlo localization (Dellaert/Fox/Thrun 1999), RRT (LaValle 1998) and PRM (Kavraki et al. 1996), Levine et al.'s end-to-end visuomotor policies (2016) that started deep robot learning, and Brooks' subsumption architecture (1986) arguing for layered reactive behaviours over central planning.
---
# Robotics: texts, courses, and seminal papers

## What they are
- **Tedrake, Robotic Manipulation** (6.4210/6.4212; read: ch. 1 intro — manipulation is more
  than pick-and-place, open-world manipulation, simulation, interactive notes, model-based
  design and analysis; ch. 2 "let's get you a robot" — robot description files (URDF/SDF),
  arms (position-controlled, torque-controlled, link dynamics with transmissions, the Kuka
  iiwa in simulation), hands (dexterous, simple grippers, soft/underactuated), sensors;
  then basic pick-and-place (spatial algebra, kinematics, differential IK), geometric pose
  estimation (depth cameras, point clouds, ICP), object detection/segmentation, bin
  picking (grasp selection), force control, motion planning (kinematic trajectory
  optimization, sampling-based), mobile manipulation, reinforcement learning, behaviour
  cloning and diffusion policies, multibody simulation, tactile sensing) — all runnable in
  **Drake**.
- **Tedrake, Underactuated Robotics** (6.832; read: ch. 1 fully-actuated vs underactuated —
  ASIMO vs passive dynamic walkers, birds vs aircraft, manipulation, definitions,
  feedback equivalence, input and state constraints, nonholonomic constraints, goals;
  ch. 2 the simple pendulum — nonlinear dynamics, overdamped/undamped, orbits, torque-
  limited with energy-shaping control; ch. 3 acrobots, cart-poles, quadrotors; then dynamic
  programming, LQR, Lyapunov analysis, trajectory optimization (direct collocation),
  planning (RRT, kinodynamic), feedback motion planning (LQR-trees, funnels), policy
  search, model-free RL, contact/hybrid dynamics, walking and running, humanoids, system
  identification, output feedback/state estimation, robust/stochastic control, sums-of-
  squares).
- **Thrun, Burgard & Fox, Probabilistic Robotics** (2005): recursive state estimation
  (Bayes filter), Gaussian filters (KF, EKF, UKF, information filter), nonparametric
  (histogram, particle), robot motion and measurement models, mobile robot localization
  (Markov, MCL, EKF), occupancy grid mapping, SLAM (EKF-SLAM, GraphSLAM, sparse extended
  information filter, FastSLAM), planning and control under uncertainty (MDPs, POMDPs,
  exploration). **Lynch & Park, Modern Robotics** (free): configuration space, rigid-body
  motions (screws, exponential coordinates), forward kinematics (product of exponentials),
  velocity kinematics and statics (Jacobians), inverse kinematics, closed chains, dynamics
  (Newton–Euler, Lagrangian), trajectory generation, motion planning, robot control
  (motion, force, hybrid), grasping and manipulation, wheeled mobile robots. **LaValle,
  Planning Algorithms** (free): discrete planning, configuration space, sampling-based and
  combinatorial motion planning, extensions (closed kinematic chains, coverage), decision-
  theoretic planning (uncertainty, sensing, information spaces), planning under
  differential constraints (kinodynamic, nonholonomic, optimal control, feedback planning).
- **Courses**: Stanford **CS223A** (Khatib: spatial descriptions, kinematics, Jacobians,
  dynamics, control, force/operational-space control); Berkeley **CS287** (Abbeel: MDPs,
  optimal control/LQR/iLQR, estimation, SLAM, imitation and RL for robotics); UPenn
  Robotics MOOC (aerial, computational motion planning, mobility, perception, estimation
  and learning); Toronto Self-Driving Cars (Coursera: vehicle dynamics, state estimation
  and localization, perception, planning).
- **Seminal**: Kalman 1960 (the optimal linear-Gaussian recursive estimator); Smith, Self &
  Cheeseman 1990 (the stochastic map — joint estimation of robot pose and landmarks: SLAM);
  Dellaert, Fox, Burgard & Thrun 1999 (**Monte Carlo localization** — particle filters for
  global localization); Kavraki, Švestka, Latombe & Overmars 1996 (**PRM**: sample the
  configuration space, connect neighbours, query a roadmap); LaValle 1998 / LaValle & Kuffner
  2001 (**RRT**: grow a tree by random samples with Voronoi bias; kinodynamic planning);
  Levine, Finn, Darrell & Abbeel 2016 (**end-to-end training of deep visuomotor policies**:
  guided policy search from pixels to torques); Brooks 1986 (**subsumption architecture**:
  layers of behaviours, "intelligence without representation" — the reactive counterpoint
  to sense–plan–act); also Khatib 1986 (potential fields), Lozano-Pérez 1983 (configuration
  space), Karaman & Frazzoli 2011 (RRT*/PRM* asymptotic optimality), Chi et al. 2023
  (diffusion policy).

## Key ideas → pages
[[robotics-and-autonomous-systems]], [[state-estimation-and-kalman-filters]],
[[motion-planning-and-control]]; existing: [[markov-decision-processes]],
[[deep-reinforcement-learning]], [[multiple-view-geometry-and-3d-vision]] (SLAM's geometry),
[[cyber-physical-systems-and-models-of-computation]], [[real-time-scheduling]].

## What they add
Tedrake for the modern synthesis (optimization-based control + learning, all in
simulation you can run), Thrun et al. for the probabilistic estimation canon, Lynch & Park
for the mechanics, LaValle for planning's full taxonomy; the papers trace the field's two
long arguments — model-based planning vs reactive behaviours (Brooks) and estimation as
Bayesian filtering (Kalman → particles) — both now absorbed into learned policies with
model-based safety.
