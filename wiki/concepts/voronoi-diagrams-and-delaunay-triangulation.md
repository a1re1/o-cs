---
title: Voronoi Diagrams and Delaunay Triangulation
type: concept
section: "11.4"
level: 400
tags: [voronoi, delaunay, proximity, fortune-sweep, triangulation, duality, mesh-generation]
sources: [computational-geometry-texts]
summary: The two dual proximity structures of a point set — the Voronoi diagram partitioning space by nearest site, and the Delaunay triangulation that maximizes minimum angles and enables good meshes and nearest-neighbor queries.
---

# Voronoi Diagrams and Delaunay Triangulation
**In one sentence.** Given points ("sites") in the plane, the **Voronoi diagram**
partitions space into cells of "everywhere closest to this site," and its geometric
**dual**, the **Delaunay triangulation**, connects sites into triangles with the fattest
possible angles — together the central proximity structures of computational geometry.

## Why it matters
These structures answer nearest-neighbor and proximity questions and produce
well-shaped meshes, so they power GIS ("nearest hospital"), wireless coverage, robotics,
terrain modeling, and the mesh generation feeding finite-element
[[numerical-linear-algebra-and-solvers]] and [[geometry-processing-and-meshes]].

## How it works
**Voronoi diagram.** For sites `p₁…pₙ`, the Voronoi cell of `pᵢ` is all points closer to
`pᵢ` than to any other site. Cell boundaries are perpendicular bisectors between
neighboring sites; vertices are equidistant from three sites. It encodes *all* nearest
-site information in O(n) total size (planar).

**Delaunay triangulation** is the **straight-line dual**: connect two sites whenever
their Voronoi cells share an edge. Its defining property is the **empty-circle
(Delaunay) criterion** — the circumcircle of every triangle contains no other site.
Equivalent characterizations:
- It **maximizes the minimum angle** over all triangulations (avoids skinny slivers —
  why it makes good meshes).
- The nearest neighbor of any site is a Delaunay neighbor.

**Construction.**
- **Fortune's sweep (1987)** builds the Voronoi diagram in **O(n log n)** with a sweep
  line and a "beach line" of parabolic arcs.
- **Incremental / randomized incremental** Delaunay insertion with **edge flips**
  (flip any edge violating the empty-circle test) is simple and O(n log n) expected.
- Duality means computing either gives the other in linear time.
- The Delaunay triangulation in 2D equals the lower convex hull of the sites lifted onto
  a paraboloid in 3D — linking it to [[computational-geometry]]'s convex-hull machinery.

## Complexity & trade-offs
- Both are O(n log n) to build and O(n) in size in the plane; in `d` dimensions the size
  can grow to O(n^⌈d/2⌉), so high-dimensional Voronoi/Delaunay is impractical (use ANN
  instead — see [[approximate-nearest-neighbor-search]]).
- Delaunay gives the best-conditioned triangulation for meshing, but may need
  **constraints** (constrained Delaunay) to respect required edges/boundaries, and
  **refinement** (Ruppert/Shewchuk) to bound triangle quality.

## Pitfalls & gotchas
- **Degeneracies** — four cocircular points or three collinear points make the diagram
  non-unique and break naive code; handle with symbolic perturbation.
- **Floating-point in-circle tests** — the empty-circle predicate is a sign-of
  -determinant test that FP gets wrong near-degenerately, producing inverted or
  inconsistent triangulations; use **exact/adaptive predicates** (Shewchuk). See
  [[floating-point]].
- **Curse of dimensionality** — do not use Voronoi/Delaunay for nearest neighbors in
  high dimensions; the structure explodes.

## Worked example
Place cell towers as sites; the Voronoi diagram immediately gives each tower's coverage
region (every phone connects to its nearest tower). Its Delaunay dual tells you which
towers are neighbors — the graph along which to plan handoffs — and its empty-circle,
max-min-angle property means using the same triangulation as a terrain mesh avoids thin
slivers that would wreck a numerical simulation.

## Related
- [[computational-geometry]] — hulls, sweep lines, and the lifting duality.
- [[geometry-processing-and-meshes]] — Delaunay meshing for surfaces/simulation.
- [[approximate-nearest-neighbor-search]] — the high-dimensional proximity alternative.
- [[floating-point]] — why robust geometric predicates are needed.

## Sources
Distilled from [[computational-geometry-texts]] (de Berg et al.; Fortune 1987;
Shewchuk robust predicates).
