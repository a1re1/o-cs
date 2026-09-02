---
title: Ray Tracing and Path Tracing
type: concept
section: "9.2"
level: 400
tags: [ray-tracing, path-tracing, rendering-equation, global-illumination, monte-carlo]
sources: [computer-graphics-texts-courses-and-seminal-papers]
summary: Physically based rendering by simulating light transport — Whitted ray tracing, Kajiya's rendering equation, and Monte Carlo path tracing for photorealistic global illumination.
---

# Ray Tracing and Path Tracing
**In one sentence.** Instead of projecting geometry to pixels, ray tracing shoots
rays *from* the camera into the scene and simulates how light bounces, producing
shadows, reflections, refractions, and full global illumination.

## Why it matters
Rasterization computes only local shading; ray tracing computes light *transport*,
so soft shadows, mirror reflections, caustics, and color bleeding emerge from one
physical model rather than a bag of tricks. It is how film-quality images are made,
and modern GPUs now accelerate it in real time. It is a direct application of
[[monte-carlo-methods]].

## How it works
**Whitted ray tracing (1980).** For each pixel, cast a primary ray; at the hit
point, recursively spawn reflection, refraction, and shadow rays. Elegant and gives
sharp reflections/refractions, but handles only ideal specular surfaces — no diffuse
inter-reflection.

**The rendering equation (Kajiya 1986)** unifies all of rendering:

```
Lo(x, ωo) = Le(x, ωo) + ∫_Ω  f_r(x, ωi, ωo) · Li(x, ωi) · (ωi · n) dωi
```

Outgoing radiance = emitted radiance + integral over the hemisphere of incoming
radiance times the BRDF `f_r` times the cosine term. Every rendering algorithm is a
way to approximate this recursive integral (the integrand contains `Li`, which is an
`Lo` elsewhere).

**Monte Carlo path tracing.** Estimate the integral by random sampling: trace a
path from the camera that bounces randomly according to the BRDF, accumulating
radiance, and average many paths per pixel. Unbiased, converges to the true image,
but noise decreases only as **O(1/√N)** in the number of samples — hence
denoisers and variance-reduction (importance sampling, next-event estimation,
bidirectional path tracing, Veach's Metropolis light transport).

**Acceleration structures.** Naively each ray tests every triangle (O(rays ×
triangles)). A **bounding volume hierarchy (BVH)** or kd-tree brings ray-scene
intersection to roughly O(log triangles) per ray; building and traversing BVHs is
what RT cores accelerate in hardware.

## Complexity & trade-offs
| | Rasterization | Path tracing |
|---|---|---|
| Cost | O(triangles), local | O(rays·log tris), global |
| Lighting | local + tricks | full transport, unbiased |
| Noise | none | O(1/√N), needs many samples |
| Best for | real-time | photorealism / film |

Ray tracing scales with *pixels and bounces* rather than triangles, so it handles
huge scenes and complex light paths gracefully but pays for every sample. Real
engines now go **hybrid**: rasterize primary visibility, ray-trace shadows and
reflections.

## Pitfalls & gotchas
- **Firefly noise** — rare high-energy paths make bright speckles; clamp or use
  better importance sampling.
- **Bias vs consistency** — many fast methods (photon mapping, biased denoisers)
  trade unbiasedness for speed; know which guarantee you have.
- **Naive uniform sampling** wastes rays; importance-sample the BRDF and the lights.

## Worked example
Rendering a glass sphere on a diffuse floor under an area light: path tracing
naturally produces the refracted background, the caustic focus of light on the
floor, and soft shadows — all from sampling the rendering equation — where
rasterization would need separate refraction, caustic, and shadow-map hacks.

## Related
- [[computer-graphics-rendering]] — the rasterization alternative it complements.
- [[monte-carlo-methods]] — path tracing is Monte Carlo integration.
- [[parallel-architectures-simd-gpu]] — BVH traversal and RT cores.

## Sources
Distilled from [[computer-graphics-texts-courses-and-seminal-papers]] (Whitted 1980;
Kajiya 1986; Cook et al. 1984; Veach 1997; PBRT).
