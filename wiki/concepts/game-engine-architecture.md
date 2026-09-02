---
title: Game Engine Architecture
type: concept
section: "9.3"
level: 400
tags: [game-loops, ecs, engines, fixed-timestep, procedural-generation]
sources: [games-and-simulation-texts-and-seminal-papers]
summary: How real-time interactive engines are structured — the fixed-timestep game loop, the entity-component-system pattern, and the subsystem architecture under a hard frame budget.
---

# Game Engine Architecture
**In one sentence.** A game engine is a soft-real-time system whose *game loop*
samples input, advances simulation by a fixed timestep, and renders, coordinating
subsystems (physics, rendering, audio, AI) within a per-frame budget of ~16 ms.

## Why it matters
The engine architecture determines whether a game runs deterministically, scales to
thousands of entities, and stays within frame budget. The patterns here — fixed
timestep, ECS, data-oriented layout — recur in any real-time simulation, robotics
loop, or high-throughput event system.

## How it works
**The game loop.** Repeatedly: process input, update the world, render. The naive
"update by however long the last frame took" makes physics frame-rate-dependent and
non-deterministic. The standard fix decouples simulation from rendering:

```
accumulator = 0; dt = 1/60
while running:
    accumulator += frameTime()          # real elapsed time
    processInput()
    while accumulator >= dt:             # fixed-timestep updates
        update(dt); accumulator -= dt
    render(accumulator / dt)             # interpolate for smoothness
```

Fixed timestep gives deterministic, stable physics; the leftover accumulator is used
to *interpolate* rendered positions so motion looks smooth between updates.

**Entity-Component-System (ECS).** Instead of deep inheritance hierarchies
("Enemy extends Character extends GameObject"), compose behavior from data:
- **Entity** — just an id.
- **Component** — plain data (Position, Velocity, Health, Sprite).
- **System** — logic that iterates over all entities having a given set of components
  (a MovementSystem reads Position+Velocity).

This is **data-oriented design**: storing components in contiguous arrays (structure
of arrays) makes systems iterate cache-friendly, a major performance win over
scattered heap objects. See [[data-oriented-design]] and [[caches-and-memory-hierarchy]].

**Subsystems** run each frame in order: input → AI/scripting → physics → animation →
rendering → audio. A **scene graph** or spatial partition (grid, BVH, quadtree)
answers "what is near what" for culling and collision.

**Common patterns** (Nystrom): *update method* (per-entity tick), *object pool*
(reuse allocations to avoid GC/malloc spikes), *spatial partition*, *component*,
*state* (finite-state machines for AI/animation), *observer/event queue*.

## Complexity & trade-offs
- Fixed timestep trades a little latency and interpolation complexity for
  determinism and stability — essential for networked lockstep and replays.
- ECS trades OOP's intuitive modeling for cache locality and flexible composition;
  it shines at high entity counts and pays overhead at small ones.

## Pitfalls & gotchas
- **Variable-timestep physics** → tunneling and non-reproducible bugs; use fixed dt.
- **Spiral of death** — if updates take longer than dt, the accumulator grows without
  bound; clamp the max updates per frame.
- **GC/allocation spikes** blow the frame budget; pool objects and avoid per-frame
  allocation on the hot path.

## Worked example
A bullet-hell game with 5,000 projectiles: store Position and Velocity as parallel
arrays, run one tight MovementSystem loop per fixed step, cull off-screen bullets via
a uniform grid, and interpolate positions at render time. The same entities in a deep
class hierarchy with per-object virtual `update()` calls would thrash the cache and
miss frame budget.

## Related
- [[physics-simulation-and-collision-detection]] — the physics subsystem's algorithms.
- [[data-oriented-design]] — why ECS stores components in arrays.
- [[caches-and-memory-hierarchy]] — the hardware reason data-oriented design wins.
- [[computer-graphics-rendering]] — the rendering subsystem.

## Sources
Distilled from [[games-and-simulation-texts-and-seminal-papers]] (Gregory *Game
Engine Architecture*; Nystrom *Game Programming Patterns*).
