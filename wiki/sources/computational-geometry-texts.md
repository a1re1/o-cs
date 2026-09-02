---
title: Computational Geometry — Texts and Seminal Algorithms
type: source
section: "11.4"
level: 400
tags: [computational-geometry, convex-hull, voronoi, delaunay, robustness]
authors: de Berg et al.; O'Rourke
year: 2008
institution: various
url: https://www.cs.uu.nl/geobook/
license: mixed
format: texts+papers
sources: []
summary: The computational-geometry canon — de Berg et al.'s Computational Geometry, O'Rourke's Computational Geometry in C, CGAL, and the seminal algorithms (Graham scan, Fortune's sweep, Delaunay/Voronoi, robust predicates).
---

# Computational Geometry — Texts and Seminal Algorithms

## What it is
The study of algorithms for geometric problems — convex hulls, triangulations,
proximity, intersection, range searching — with a distinctive obsession with **numerical
robustness**, since geometric predicates fail catastrophically under floating-point error.

## Key ideas
- **Convex hulls & sweep lines** — Graham scan, monotone chain; segment intersection.
  See [[computational-geometry]].
- **Voronoi diagrams & Delaunay triangulation** — proximity structures and their
  duality. See [[voronoi-diagrams-and-delaunay-triangulation]].
- **Robustness** — exact/adaptive predicates to avoid catastrophic FP failures. See
  [[computational-geometry]].

## Chapter / lecture map
- **de Berg, Cheong, van Kreveld & Overmars, *Computational Geometry: Algorithms and
  Applications*** — the standard text: hulls, line segment intersection, polygon
  triangulation, Voronoi/Delaunay, range trees.
- **O'Rourke, *Computational Geometry in C*** — implementation-focused.
- **CGAL docs** — the industrial-strength geometry library.

## Seminal papers
- **Graham scan (1972)** — O(n log n) convex hull; see [[computational-geometry]].
- **Fortune's sweep (1987)** — O(n log n) Voronoi diagram construction.
- **Delaunay / Voronoi foundations** — the dual proximity structures.
- **Shewchuk, Triangle & robust predicates** — adaptive-precision exact geometric tests.

## What it adds
Rigorous geometry underpins graphics ([[geometry-processing-and-meshes]]), GIS,
robotics motion planning, and mesh generation for [[numerical-linear-algebra-and-solvers]]
(finite elements). Its robustness lessons are a case study in [[floating-point]] hazards.
