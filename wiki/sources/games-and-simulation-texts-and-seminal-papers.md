---
title: Games, Animation & Simulation — Texts and Seminal Papers
type: source
section: "9.3"
level: 400
tags: [game-engines, physics-simulation, animation, collision-detection, procedural-generation]
authors: Various
year: 2018
institution: CMU, MIT, Pixar
url: https://gameprogrammingpatterns.com/
license: mixed
format: texts+courses+papers
sources: []
summary: The game-engine and physics-animation canon — Gregory's Game Engine Architecture, Nystrom's Game Programming Patterns, Ericson on collision, and the seminal simulation papers (Reynolds Boids, Stam Stable Fluids, position-based dynamics).
---

# Games, Animation & Simulation — Texts and Seminal Papers (Various)

## What it is
The engineering of interactive real-time worlds: the **game loop** and engine
architecture, **physics simulation** (rigid bodies, cloth, fluids), **collision
detection**, and **procedural generation**. It combines soft-real-time systems
engineering with numerical simulation.

## Key ideas
- **Game-engine architecture** — the fixed-timestep loop, entity-component-system
  (ECS) design, subsystems (render, physics, audio, input). See
  [[game-engine-architecture]].
- **Physics-based animation** — numerically integrate equations of motion; keep it
  stable and fast. See [[physics-simulation-and-collision-detection]].
- **Collision detection** — broad phase (spatial pruning) + narrow phase (exact
  tests); response via impulses or constraints. See
  [[physics-simulation-and-collision-detection]].

## Chapter / lecture map
- **Gregory, *Game Engine Architecture*** — the comprehensive engine reference.
- **Nystrom, *Game Programming Patterns* (free)** — game loop, update method,
  component, object pool, spatial partition, state.
- **Ericson, *Real-Time Collision Detection*** — the collision bible (BVHs, GJK,
  spatial hashing, SAT).
- **CMU 15-466 Computer Game Programming; Handmade Hero (video)** — build engines
  from scratch.
- **Baraff & Witkin, Pixar SIGGRAPH physically based modeling notes (free)** — the
  standard intro to simulating rigid bodies and cloth.

## Notable claims & quotes
- Nystrom: decouple *game time* from *real time* with a fixed timestep so physics is
  deterministic regardless of frame rate.
- Reynolds: complex flocking emerges from three local rules — no leader, no global plan.

## Seminal papers
- **Reynolds, Boids (1987)** — emergent flocking from separation, alignment,
  cohesion; foundational for agent-based crowds.
- **Stam, "Stable Fluids" (1999)** — an unconditionally stable Navier-Stokes solver
  (semi-Lagrangian advection) that made real-time fluid simulation practical.
- **Müller et al., Position-Based Dynamics (2007)** — simulate by directly projecting
  positions to satisfy constraints; robust, fast, ubiquitous in games (cloth, soft
  bodies).

## What it adds
Games are where real-time systems, numerical methods, and graphics meet under a hard
frame-time budget. Links to [[computer-graphics-rendering]], [[monte-carlo-methods]]
and numerical [[numerical-methods-and-stability]], and [[data-oriented-design]] via
ECS and cache-friendly layout.
