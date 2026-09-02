---
title: Geometry Processing and Meshes
type: concept
section: "9.2"
level: 400
tags: [meshes, geometry-processing, subdivision, mesh-simplification, discrete-differential-geometry]
sources: [computer-graphics-texts-courses-and-seminal-papers]
summary: Representing and manipulating surfaces as polygon meshes — data structures, subdivision, simplification, parameterization, and discrete differential geometry.
---

# Geometry Processing and Meshes
**In one sentence.** The algorithms that create, edit, smooth, simplify, and analyze
the polygon meshes that represent 3D surfaces.

## Why it matters
Every rendered surface is ultimately a mesh (or converted to one). Geometry
processing decides whether a scanned model is watertight, whether a game asset fits
in memory, and whether a simulation mesh is well-conditioned. It is where discrete
math meets differential geometry.

## How it works
**Mesh representation.** A **triangle mesh** is vertices (positions) plus faces
(index triples). For editing you need adjacency: the **half-edge** data structure
stores, per directed edge, its twin, next, origin vertex, and incident face,
giving O(1) local traversal (all faces around a vertex, all edges of a face).

**Subdivision surfaces** (Catmull-Clark 1978) — repeatedly split faces and
reposition vertices by weighted averages, converging to a smooth limit surface from
a coarse control cage; the standard for film modeling.

**Mesh simplification** (Garland & Heckbert 1997) — greedily collapse edges,
choosing the pair whose removal least increases a **quadric error metric** (sum of
squared distances to adjacent planes). Produces level-of-detail (LOD) hierarchies
so distant objects use fewer triangles.

**Parameterization** — flatten a surface to 2D (UV mapping) for texturing, minimizing
angle or area distortion; ARAP ("as-rigid-as-possible") methods keep local shape.

**Discrete differential geometry (DDG).** Port smooth notions — curvature, the
Laplacian, geodesics — to meshes so they converge under refinement. The **cotangent
Laplacian** is the workhorse operator for smoothing (mean-curvature flow),
parameterization, and deformation; it connects meshes to
[[spectral-graph-theory-and-clustering]].

## Complexity & trade-offs
- Half-edge gives O(1) local queries at the cost of ~6× the storage of a bare index
  list and only representing **manifold** meshes cleanly (non-manifold junctions
  need extensions).
- Simplification trades fidelity for triangle count; quadric metrics give the best
  quality-per-triangle but need care at boundaries and to preserve UV seams.

## Pitfalls & gotchas
- **Non-manifold / non-watertight meshes** (holes, T-junctions, duplicate vertices)
  break half-edge structures, simulation, and 3D printing; repair first.
- **Uniform Laplacian vs cotangent Laplacian** — the uniform (graph) Laplacian
  ignores geometry and distorts on irregular meshes; use cotangent weights.
- **Sliver triangles** wreck numerical conditioning in simulation and shading.

## Worked example
Decimating a 2M-triangle scanned statue for real-time viewing: build a quadric per
vertex, put candidate edge collapses in a priority queue keyed by error, and
collapse until 50k triangles remain — preserving sharp features (high curvature)
because collapsing them incurs large quadric error.

## Related
- [[computer-graphics-rendering]] — meshes are what gets rasterized.
- [[spectral-graph-theory-and-clustering]] — the mesh Laplacian is a graph Laplacian.
- [[linear-algebra-for-cs]] — DDG operators are sparse linear systems.

## Sources
Distilled from [[computer-graphics-texts-courses-and-seminal-papers]] (Catmull-Clark
1978; Garland & Heckbert 1997; Botsch et al. *Polygon Mesh Processing*; Crane DDG).
