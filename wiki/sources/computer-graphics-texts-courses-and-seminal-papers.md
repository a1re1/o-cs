---
title: Computer Graphics — Texts, Courses, and Seminal Papers
type: source
section: "9.2"
level: 400
tags: [computer-graphics, rendering, ray-tracing, rasterization, geometry-processing]
authors: Various
year: 2023
institution: CMU, Stanford, MIT, Berkeley
url: https://www.pbr-book.org/
year_note: PBRT 4th ed free online
license: mixed
format: courses+texts+papers
sources: []
summary: The computer-graphics canon — PBRT and Real-Time Rendering, the CMU/MIT/Berkeley courses, and the seminal papers from Phong shading and Whitted ray tracing to the rendering equation, path tracing, NeRF, and Gaussian splatting.
---

# Computer Graphics — Texts, Courses, and Seminal Papers (Various)

## What it is
The literature of synthesizing images from geometric and physical descriptions of
scenes. Two branches dominate: **real-time rendering** (rasterization on GPUs, for
games and interaction) and **physically based / offline rendering** (ray and path
tracing, for film and photorealism). A third, **geometry processing**, manipulates
the meshes and surfaces themselves.

## Key ideas
- **The rendering pipeline** — transforms, projection, rasterization, shading,
  texturing; the GPU model. See [[computer-graphics-rendering]].
- **Ray tracing and the rendering equation** — global illumination by simulating
  light transport; Monte Carlo path tracing. See [[ray-tracing-and-path-tracing]].
- **Geometry processing** — meshes, subdivision, simplification, differential
  geometry on discrete surfaces. See [[geometry-processing-and-meshes]].
- **Neural rendering** — NeRF and 3D Gaussian splatting reconstruct scenes from
  photos. See [[computer-graphics-rendering]].

## Chapter / lecture map
- **Marschner & Shirley, *Fundamentals of Computer Graphics*** — the standard intro:
  transforms, rasterization, ray tracing, shading, color.
- **Pharr, Jakob & Humphreys, *Physically Based Rendering* (PBRT, free online)** —
  the definitive physically based renderer, literate-programming style; a Nobel—no,
  a *Sci-Tech Academy Award* winner for its film impact.
- **Akenine-Möller et al., *Real-Time Rendering*** — the GPU-pipeline bible.
- **CMU 15-462/662 (Keenan Crane), MIT 6.837, Berkeley CS184** — open course spines.
- **"Ray Tracing in One Weekend" (Shirley, free)** and **Learn OpenGL (free)** —
  hands-on ramps.
- **Crane, *Discrete Differential Geometry* (free)** — geometry-processing theory.

## Notable claims & quotes
- **Kajiya's rendering equation (1986)** unified all of rendering into one integral
  equation of light transport; everything since is a way to approximate it.
- Whitted (1980): recursive ray tracing gives reflections, refractions, and shadows
  "for free" from one elegant recursion.

## Seminal papers (chronological)
- **Sutherland, Sketchpad (1963)** — interactive graphics is born.
- **Gouraud (1971), Phong (1975), Blinn (1977)** — smooth shading and the
  specular reflection models still used in real-time rendering.
- **Catmull & Clark (1978)** — subdivision surfaces.
- **Whitted (1980)** — recursive ray tracing.
- **Cook, Porter & Carpenter (1984)** — distributed (stochastic) ray tracing:
  soft shadows, motion blur, depth of field.
- **Kajiya (1986)** — the rendering equation.
- **Veach (1997)** — Metropolis light transport; bidirectional path tracing.
- **Garland & Heckbert (1997)** — quadric mesh simplification.
- **Mildenhall et al., NeRF (2020)** and **Kerbl et al., 3D Gaussian Splatting
  (2023)** — neural / point-based scene reconstruction from images.

## What it adds
Graphics is where linear algebra, calculus, and physics become pictures. It links to
[[matrices-and-linear-maps]] (transforms are matrices), [[monte-carlo-methods]]
(path tracing is Monte Carlo integration), [[parallel-architectures-simd-gpu]] (the
pipeline is massively parallel), and [[deep-learning-basics]] (neural rendering).
