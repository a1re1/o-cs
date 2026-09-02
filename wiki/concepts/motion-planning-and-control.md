---
title: Motion planning and control — configuration space and obstacles, combinatorial vs sampling-based planning (PRM, RRT, RRT*, bidirectional and kinodynamic variants, collision checking), potential fields and their local minima, trajectory optimization (direct collocation, shooting, CHOMP/TrajOpt), optimal control (dynamic programming, LQR, iLQR/DDP, MPC), feedback control (PID, feedback linearization, impedance), stability (Lyapunov, regions of attraction, control barrier functions), underactuated examples (pendulum swing-up, cart-pole, walking), and learning-based planners
type: concept
section: "6.10"
level: 500
tags: [motion-planning, configuration-space, c-obstacles, collision-checking, combinatorial-planning, visibility-graph, cell-decomposition, sampling-based-planning, prm, probabilistic-roadmap, rrt, rapidly-exploring-random-tree, voronoi-bias, rrt-connect, rrt-star, asymptotic-optimality, prm-star, kinodynamic-planning, probabilistic-completeness, narrow-passages, potential-fields, local-minima, trajectory-optimization, direct-collocation, shooting, chomp, trajopt, optimal-control, dynamic-programming, hjb, lqr, riccati, ilqr, ddp, mpc, model-predictive-control, receding-horizon, pid, feedback-linearization, computed-torque, impedance-control, lyapunov, region-of-attraction, sums-of-squares, control-barrier-functions, safety-filters, pendulum-swing-up, energy-shaping, cart-pole, acrobot, walking, hybrid-dynamics, learned-planners, lavalle, tedrake]
sources: [robotics-texts-courses-and-seminal-papers]
summary: Motion planning finds a collision-free path (and, with dynamics, a feasible trajectory) from start to goal in configuration space — where obstacles become C-obstacles and exact combinatorial methods (visibility graphs, cell decomposition) scale only to low dimensions, so practical planners sample: PRM builds a reusable roadmap by sampling free configurations and connecting neighbours with a local planner, RRT grows a tree from the start whose random-sample-then-extend rule biases growth toward unexplored space (Voronoi bias), RRT-Connect grows two trees, RRT*/PRM* rewire to converge to optimal paths (asymptotic optimality, at extra cost), and kinodynamic variants sample controls to respect dynamics — all probabilistically complete, all fast because collision checking is the cost and narrow passages the weakness, and all followed by smoothing; potential fields are fast local reactive planners with local-minima traps; trajectory optimization instead poses the path as a nonlinear program over states and controls (direct collocation, multiple shooting, CHOMP/TrajOpt with signed-distance constraints) — local but handles dynamics and costs naturally; optimal control gives the feedback laws: dynamic programming/HJB in principle, LQR in closed form for linear systems and quadratic costs (the Riccati equation; linearize about a trajectory for time-varying LQR), iLQR/DDP iterating LQR on nonlinear systems, and MPC re-solving a finite-horizon optimization at every step with constraints (the workhorse of legged robots, drones and cars); classical feedback (PID, feedback linearization/computed torque for fully-actuated arms, impedance control for contact) and stability certificates (Lyapunov functions, regions of attraction via sums-of-squares, control barrier functions as safety filters) close the loop and bound what learned policies may do; and Tedrake's underactuated examples — swinging up a torque-limited pendulum by energy shaping, cart-pole and acrobot via LQR/trajectory optimization, walking as hybrid dynamics — show why dynamics, not just geometry, is the planning problem.
---
# Motion planning and control

**In one sentence.** Plan in configuration space by sampling when the space is
high-dimensional, optimize trajectories when dynamics and costs matter, and close the
loop with feedback laws (LQR, MPC, impedance) whose stability you can certify — because a
plan that ignores dynamics or a controller that ignores obstacles fails on the real robot.

## Configuration space and collision checking (LaValle ch. 3–5; Lozano-Pérez 1983)
The robot is a point in **C-space** (joint angles; SE(2)/SE(3) for free-flying bodies);
workspace obstacles map to **C-obstacles** (for a translating polygon, the Minkowski sum);
C_free is what to plan in. Dimension: 6–7 for arms, 12+ for mobile manipulators, 30+ for
humanoids — exact **combinatorial** methods (visibility graphs — optimal in 2D polygons;
exact/approximate cell decomposition; Voronoi/retraction roadmaps) are complete but
exponential in dimension ([[computational-geometry]]); grid search (A*/D*/hybrid A* on
lattices — [[search-algorithms-ai]]) works to ~4–5 dimensions and for cars. **Collision
checking** dominates runtime: bounding-volume hierarchies, GJK, signed distance fields,
swept volumes; continuous collision checking along edges ([[computational-geometry]]).

## Sampling-based planning (Kavraki et al. 1996; LaValle & Kuffner 2001; Karaman & Frazzoli 2011)
- **PRM**: sample n configurations, keep the collision-free ones, connect each to its k
  nearest (or within radius r) by a straight-line **local planner** if collision-free; answer
  queries by graph search on the roadmap — multi-query, parallelizable, **probabilistically
  complete** (finds a path with probability → 1 as n → ∞ if one exists); struggles with
  **narrow passages** (Gaussian/bridge sampling, obstacle-based sampling).
- **RRT**: tree rooted at the start; repeat: sample x_rand (goal-biased with probability
  5–10 %), find the nearest tree node, **extend** toward x_rand by step ε if collision-free —
  the nearest-node rule makes large Voronoi regions get chosen more often (**Voronoi bias**),
  pulling the tree into unexplored space; single-query, handles differential constraints by
  extending with sampled controls (**kinodynamic RRT**); **RRT-Connect** grows trees from start
  and goal and connects them (the fastest practical planner); paths are jagged →
  **shortcutting/smoothing** afterwards.
- **RRT\* / PRM\***: choose parents within a shrinking neighbourhood by cost and **rewire** —
  **asymptotically optimal** (path cost → optimum) at O(log n) extra work per sample; RRT
  alone converges to a *suboptimal* path with probability 1; informed RRT*, BIT*, FMT* speed
  convergence; LazyPRM defers collision checks. Libraries: OMPL, MoveIt; typical arm
  planning in milliseconds to seconds.
- **Potential fields** (Khatib 1986): attractive goal + repulsive obstacles, follow the
  gradient — real-time, reactive, but **local minima** (U-shaped obstacles); navigation
  functions fix it in special cases; vector-field/velocity-obstacle methods for dynamic
  obstacles (crowds, multi-robot).

## Trajectory optimization (Underactuated ch. 10; Betts; Ratliff et al. 2009; Schulman et al. 2014)
Pose the trajectory as a **nonlinear program**: minimize Σ cost(xₜ, uₜ) s.t. dynamics
x_{t+1} = f(xₜ, uₜ), bounds, obstacle constraints. **Transcription**: **direct collocation**
(states and controls as decision variables, dynamics as defect constraints — sparse, robust,
Hermite–Simpson), **direct/multiple shooting** (integrate dynamics, optimize controls),
solved by SQP/interior-point ([[nonlinear-optimization]], [[convexity]] where possible —
convex MPC for linearized systems); **CHOMP** (gradient descent on a smoothness + obstacle
cost with a Riemannian metric), **TrajOpt** (sequential convex optimization with signed-
distance collision constraints), STOMP (sampling-based). Local (initial guess from a
sampling planner), handles dynamics/torque limits/contact schedules, produces smooth
trajectories; the output needs a feedback controller to track it. Contact-implicit and
hybrid trajectory optimization for walking/manipulation (mode sequences, complementarity).

## Optimal control: DP, LQR, iLQR, MPC (Underactuated ch. 7–8; Bertsekas; CS287)
**Dynamic programming**: cost-to-go J*(x) = min_u [ℓ(x, u) + J*(f(x, u))] — the Bellman
equation ([[markov-decision-processes]]; continuous-time **HJB**); exact only for small
discretized state spaces (value iteration on grids: the pendulum, 2-D). **LQR**: for linear
dynamics ẋ = Ax + Bu and quadratic cost xᵀQx + uᵀRu, the optimal policy is linear u = −Kx
with K from the (algebraic/differential) **Riccati equation** — closed form, the most-used
optimal controller; **time-varying LQR** about a nominal trajectory stabilizes it (linearize
along the trajectory — [[derivatives-and-gradients]]); **LQG** adds Gaussian noise and a
Kalman filter (certainty equivalence — [[state-estimation-and-kalman-filters]]). **iLQR/DDP**:
iterate — linearize/quadratize about the current trajectory, solve the LQR backward pass,
roll forward with line search — trajectory optimization with a built-in feedback law
(the algorithm behind many MuJoCo humanoid controllers). **MPC**: at each step solve a
finite-horizon trajectory optimization from the current state with constraints, apply the
first control, repeat (receding horizon) — handles constraints and disturbances; convex/
quadratic MPC at kHz for drones and legged robots (whole-body MPC), nonlinear MPC for cars;
stability via terminal costs/sets; the practical bridge between planning and control.
Reachability/robust/stochastic control extend it ([[cyber-physical-systems-and-models-of-computation]]).

## Feedback control and stability (Underactuated ch. 2–3, 9; Lynch & Park ch. 11; Slotine & Li)
**PID** (proportional–integral–derivative) on each joint: the default for position control;
gain tuning, integrator windup, derivative noise. **Feedback linearization / computed
torque**: τ = M(q)(q̈_d + K_d ė + K_p e) + C q̇ + g cancels the dynamics of a fully-actuated
arm; **impedance control** renders a desired mass–spring–damper at the end effector for
contact; operational-space control (Khatib). **Stability**: **Lyapunov** functions (V > 0,
V̇ < 0 ⇒ asymptotic stability; energy is the natural candidate — pendulum energy shaping
pumps energy toward the homoclinic orbit, then LQR catches the top), **regions of
attraction** estimated by **sums-of-squares** programming (SDP — [[linear-programming-and-duality]]
cousin) for polynomial systems, **LQR-trees** (funnels covering the state space —
feedback motion planning), **control barrier functions** (a QP-based **safety filter** that
minimally modifies any controller — including a learned policy — to keep a safe set
invariant: the standard way to make learning safe), passivity, sliding mode/robust control.
**Hybrid dynamics**: walking as alternating continuous phases and impacts; Poincaré maps
for periodic gaits; ZMP and centroidal MPC for humanoids; passive dynamic walkers as the
underactuated ideal (Underactuated ch. 1).

## Underactuated case studies (Underactuated ch. 2–3)
**Pendulum swing-up** with limited torque: no linear controller works; **energy shaping**
u = −k q̇ (E − E_desired) drives the energy to the upright orbit, LQR stabilizes at the top.
**Cart-pole** / **acrobot**: partial feedback linearization + energy shaping, or trajectory
optimization → time-varying LQR; **quadrotor**: differentially flat, so trajectories in
flat outputs + LQR/MPC; **walking**: hybrid zero dynamics, MPC + RL ([[deep-reinforcement-learning]]).
The lesson: exploit the dynamics you cannot cancel.

## Learning meets planning
Learned samplers and heuristics for RRT/PRM; neural motion planners; learned dynamics
models inside MPC (model-based RL — [[deep-reinforcement-learning]]); policies as planners
(diffusion policies output trajectories — [[robotics-and-autonomous-systems]]); LLM task
planners emitting subgoals for motion planners; safety via CBFs/reachability wrapped
around learned components. Guarantees are the open question.

## Pitfalls
- Planning a geometric path and expecting a dynamic system to follow it (no feasibility);
  ignoring velocity/torque limits.
- RRT with a poorly scaled distance metric (rotations vs translations) or no goal bias;
  RRT read as optimal.
- Trajectory optimization from a bad initial guess (local minimum in an obstacle).
- LQR gains from a linearization far from the operating point; MPC without a terminal
  cost (instability) or with a horizon too short to see obstacles.
- PID on an underactuated system; integrator windup on saturated actuators.
- Verifying safety in simulation only.

## Related
- [[robotics-and-autonomous-systems]], [[state-estimation-and-kalman-filters]],
  [[search-algorithms-ai]] (A*, lattices), [[computational-geometry]],
  [[nonlinear-optimization]], [[convexity]], [[linear-programming-and-duality]],
  [[markov-decision-processes]] (DP/Bellman), [[deep-reinforcement-learning]],
  [[derivatives-and-gradients]], [[cyber-physical-systems-and-models-of-computation]],
  [[real-time-scheduling]], [[monte-carlo-methods]] (sampling).

## Sources
LaValle, *Planning Algorithms* 2006 ch. 3–8, 13–14; Tedrake, *Underactuated Robotics* ch. 1–3 (read), 7–10, 12 (from the book); Lynch & Park ch. 10–11; Kavraki et al. 1996; LaValle & Kuffner 2001; Kuffner & LaValle 2000 (RRT-Connect); Karaman & Frazzoli 2011; Khatib 1986; Ratliff et al. 2009 (CHOMP); Schulman et al. 2014 (TrajOpt); Tassa et al. 2012 (iLQR/MPC); Ames et al. 2019 (CBFs); Betts 2010; Bertsekas, *Dynamic Programming and Optimal Control*.
