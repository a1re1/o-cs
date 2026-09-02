---
title: Physics Simulation and Collision Detection
type: concept
section: "9.3"
level: 400
tags: [physics-engines, collision-detection, position-based-dynamics, fluids, numerical-integration]
sources: [games-and-simulation-texts-and-seminal-papers]
summary: Simulating motion in real time — numerical integration of rigid bodies, broad/narrow-phase collision detection, constraint and impulse response, position-based dynamics, and stable fluids.
---

# Physics Simulation and Collision Detection
**In one sentence.** Real-time physics advances a world of bodies by numerically
integrating forces, detects when bodies overlap (collision detection), and resolves
overlaps with impulses or constraints — all stably within a frame.

## Why it matters
Physics engines (Box2D, Bullet, PhysX) power games, robotics, VFX, and engineering
simulation. The core tension is **stability vs speed**: a wrong integrator or a
missed collision makes objects explode or pass through walls. The same numerical and
geometric ideas appear in any dynamics simulation.

## How it works
**Numerical integration.** Advance position/velocity under forces. Explicit Euler
(`v += a·dt; x += v·dt`) is simplest but *gains energy* and blows up for stiff
systems. **Semi-implicit (symplectic) Euler** — update velocity first, then position
with the new velocity — is stable enough and standard in games. Stiff systems
(cloth, springs) need implicit or position-based methods. See
[[numerical-methods-and-stability]].

**Collision detection, two phases:**
- **Broad phase** — cheaply prune non-colliding pairs using spatial structures:
  uniform grid / spatial hashing, sweep-and-prune, or a BVH. Reduces O(n²) pair
  tests to near O(n).
- **Narrow phase** — exact tests on surviving pairs: the **Separating Axis Theorem
  (SAT)** for convex polytopes, or **GJK** (Gilbert-Johnson-Keerthi) for
  convex-convex distance, producing contact points and normals.

**Collision response.** Compute an **impulse** that instantaneously changes
velocities to prevent interpenetration and apply friction/restitution; stacking and
joints are handled by iteratively solving many contact **constraints** (a sequential
impulse / projected Gauss-Seidel solver).

**Position-Based Dynamics (PBD, Müller 2007).** Skip forces: predict positions, then
iteratively *project* them to satisfy constraints (distance, volume, contact)
directly. Unconditionally stable, controllable, and cheap — the backbone of modern
cloth, soft bodies, and even fluids (PBF) in games.

**Fluids (Stam's Stable Fluids, 1999).** Solve Navier-Stokes on a grid with
**semi-Lagrangian advection** (trace backward along the velocity field) plus a
pressure projection to keep the field divergence-free; unconditionally stable, so
real-time smoke and water became feasible.

**Emergent agents (Reynolds Boids, 1987).** Flocking from three local steering rules
— separation, alignment, cohesion — with no central controller; the template for
crowd and swarm simulation.

## Complexity & trade-offs
- Broad phase turns collision from O(n²) to ~O(n log n) or O(n); the constant and
  robustness depend on the structure and object size distribution.
- Explicit integrators are cheap but unstable for stiff systems; implicit/PBD are
  stable but need iterative solves. More solver iterations = stiffer, costlier
  constraints.

## Pitfalls & gotchas
- **Tunneling** — fast thin objects skip through walls between steps; use continuous
  collision detection (swept tests) or smaller dt.
- **Explicit Euler on stiff springs** explodes; use semi-implicit or PBD.
- **Restitution/friction hacks** that inject energy make stacks jitter; damp and cap
  iteration.
- **Non-convex shapes** need decomposition before GJK/SAT apply.

## Worked example
Simulating a hanging cloth: model it as a grid of particles with distance
constraints between neighbors. Each step, predict positions under gravity, then run
several PBD iterations projecting each edge back to its rest length and resolving
collisions with the character body — stable at 60 Hz where an explicit spring model
would oscillate and blow up.

## Related
- [[game-engine-architecture]] — physics is a subsystem in the fixed-timestep loop.
- [[numerical-methods-and-stability]] — integrator stability underlies all of this.
- [[computer-graphics-rendering]] — simulated geometry gets rendered.

## Sources
Distilled from [[games-and-simulation-texts-and-seminal-papers]] (Ericson
*Real-Time Collision Detection*; Baraff & Witkin; Müller et al. 2007; Stam 1999;
Reynolds 1987).
