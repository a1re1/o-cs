---
title: Computational geometry — cross products, orientation, segment intersection, polygon area, convex hull, sweep line, closest pair
type: concept
section: "3.4"
level: 300
tags: [computational-geometry, cross-product, orientation-test, segment-intersection, point-in-polygon, shoelace-formula, convex-hull, andrews-monotone-chain, graham-scan, sweep-line, closest-pair, line-intersection, rotating-calipers, integer-coordinates, floating-point-epsilon]
sources: [competitive-programmers-handbook, clrs]
summary: Almost every 2D geometry primitive reduces to the sign of a cross product — orientation of three points (left/right/collinear), segment intersection by orientation tests plus the collinear bounding-box case, point-in-polygon by ray crossing or winding number, area by the shoelace formula (and Pick's theorem for lattice points), convex hull in O(n log n) by Andrew's monotone chain or Graham scan, and sweep-line algorithms for segment intersections and the O(n log n) closest pair — with integer arithmetic wherever possible to avoid epsilon bugs.
---
# Computational geometry

**In one sentence.** Represent points as vectors, decide everything by the sign of
`cross(b − a, c − a)`, and keep coordinates integer as long as you can.

## Primitives (CPH ch. 29)
- Points as `(x, y)` (or `complex<long long>`); `dot(u, v) = uₓvₓ + u_yv_y`, `cross(u, v) =
  uₓv_y − u_yvₓ` (signed area of the parallelogram; z of the 3D cross product —
  [[vectors-and-inner-products]]).
- **Orientation** `ccw(a, b, c) = sign(cross(b − a, c − a))`: > 0 left turn, < 0 right, 0
  collinear. Point-line distance = |cross| / |b − a|.
- **Segment intersection**: segments ab and cd intersect iff ccw(a,b,c) ≠ ccw(a,b,d) and
  ccw(c,d,a) ≠ ccw(c,d,b), plus the collinear cases via bounding-box overlap. Line intersection by
  solving with cross products (parametric t = cross(c − a, d − c) / cross(b − a, d − c)).
- **Polygon area**: shoelace ½|Σ (xᵢ y_{i+1} − x_{i+1} yᵢ)|; sign gives orientation. **Pick's
  theorem** A = I + B/2 − 1 for lattice polygons (B via gcd of edge deltas).
- **Point in polygon**: ray casting parity (O(n)); winding number for robustness; for convex
  polygons binary search on the fan (O(log n)).
- Distances: point–segment (project, clamp), circle intersections, angles via `atan2`.

## Convex hull (CPH 30.3)
**Andrew's monotone chain**: sort points by (x, y); build lower hull then upper hull, popping while
the last turn is not counter-clockwise — O(n log n), handles collinear points by choosing ≤ vs <.
Graham scan (sort by polar angle), Jarvis march O(nh), Chan's O(n log h). Applications: diameter
by **rotating calipers**, minimum bounding box, width, Minkowski sums, half-plane intersection
(O(n log n) sort + deque).

## Sweep line (CPH ch. 30)
Process events sorted by x while maintaining a status structure ([[balanced-search-trees]]):
- Segment intersections (Bentley–Ottmann, O((n + k) log n)); does any pair intersect (Shamos–
  Hoey).
- Union of rectangles area (segment tree over compressed y — [[range-queries-segment-trees-fenwick]]).
- **Closest pair**: sort by x, sweep keeping a set of points within d in x ordered by y; check
  the ≤ 7 candidates within the d-window — O(n log n); or divide and conquer
  ([[divide-and-conquer]]).
- Delaunay triangulation / Voronoi (Fortune's sweep) — usually a library.

## Numerical robustness
Prefer integer coordinates (cross products fit in 64-bit if |coords| ≤ ~10⁹… careful: products
reach 10¹⁸); with floats compare using an epsilon scaled to magnitude, avoid `==`, avoid `sqrt`
and `acos` when a cross/dot suffices, and be aware that CGAL-style exact predicates exist
([[floating-point]]).

## Pitfalls
- Overflow in cross products (use `__int128` or long double).
- Degeneracies: collinear triples, duplicate points, vertical lines, touching segments.
- Sorting by angle with `atan2` precision; use cross-product comparators by half-plane.

## Related
- [[vectors-and-inner-products]], [[divide-and-conquer]], [[balanced-search-trees]],
  [[range-queries-segment-trees-fenwick]], [[floating-point]], [[similarity-search-and-lsh]] (k-d trees).

## Sources
CPH ch. 29–30; CLRS ch. 33; de Berg et al. *Computational Geometry* (reference).
