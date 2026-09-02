---
title: Computer Graphics Rendering
type: concept
section: "9.2"
level: 400
tags: [rasterization, rendering-pipeline, shading, transforms, gpu-pipelines, real-time-rendering]
sources: [computer-graphics-texts-courses-and-seminal-papers]
summary: How a 3D scene becomes a 2D image — the transform/projection/rasterization/shading pipeline that GPUs implement, plus texturing, the z-buffer, and shading models.
---

# Computer Graphics Rendering
**In one sentence.** Rendering turns a description of 3D geometry, materials, and
lights into a 2D image of pixels, classically through the *rasterization pipeline*
that GPUs implement in hardware.

## Why it matters
Rasterization is why real-time 3D — games, CAD, AR/VR, every GPU — is possible: it
is an O(triangles) streaming algorithm that maps perfectly onto
[[parallel-architectures-simd-gpu]]. Understanding the pipeline explains what shaders are,
why the z-buffer exists, and where [[ray-tracing-and-path-tracing]] takes over for
photorealism.

## How it works
**The rasterization pipeline** (logical stages; the GPU parallelizes each):
1. **Model & view transform** — place objects in the world and the world relative
   to the camera, via 4×4 matrices in **homogeneous coordinates** (so translation is
   a matrix multiply). See [[matrices-and-linear-maps]].
2. **Projection** — perspective or orthographic transform into clip space; the
   perspective divide produces foreshortening.
3. **Clipping & viewport transform** — cut geometry to the frustum, map to pixels.
4. **Rasterization** — determine which pixels each triangle covers; interpolate
   vertex attributes (position, normal, UV) across the triangle with
   perspective-correct interpolation.
5. **Fragment shading** — compute each pixel's color from lights, materials, and
   textures (a *fragment/pixel shader* program).
6. **Depth test (z-buffer)** — keep the nearest fragment per pixel, resolving
   visibility in O(fragments) without sorting geometry.

**Shading models** (local illumination, no inter-object light):
- **Lambertian/diffuse** — brightness ∝ `max(0, n·l)`.
- **Phong / Blinn-Phong** — add a specular highlight from the reflection (or half)
  vector; **Gouraud** interpolates vertex colors, **Phong** interpolates normals
  (smoother highlights).
- **Physically based shading (PBR)** — energy-conserving microfacet BRDFs
  parameterized by roughness and metalness; the modern real-time standard.

**Textures** map images onto surfaces via UV coordinates; **mipmapping**
pre-filters them to avoid aliasing at distance. **Antialiasing** (MSAA, or
post-process) fights jagged edges from point sampling.

**The programmable pipeline.** Vertex, geometry, tessellation, and fragment
*shaders* (GLSL/HLSL) replaced the fixed function pipeline; *compute shaders* run
general parallel work. This is the API surface of OpenGL/Vulkan/Metal/DirectX.

**Neural rendering** (recent): **NeRF** represents a scene as an MLP mapping
position+direction to color+density, rendered by volumetric ray marching; **3D
Gaussian splatting** represents it as millions of anisotropic blobs rasterized in
real time. Both *reconstruct* renderable scenes from ordinary photos.

## Complexity & trade-offs
- Rasterization is **O(triangles × covered pixels)** and embarrassingly parallel —
  hence GPUs — but computes only *local* lighting; shadows, reflections, and
  indirect light need extra passes (shadow maps, environment maps, screen-space
  tricks) or hybrid ray tracing.
- The z-buffer trades memory for a sort-free visibility solution; transparency
  breaks it (needs back-to-front blending or order-independent methods).

## Pitfalls & gotchas
- **Interpolating in screen space** without perspective correction warps textures.
- **Z-fighting** — coplanar surfaces flicker from limited depth precision; use a
  non-linear depth buffer carefully and avoid overlapping geometry.
- **Gamma/linear confusion** — lighting must be done in linear space, output in
  sRGB, or images look wrong.

## Worked example
To draw a spinning textured cube: upload vertices once; each frame set the
model-view-projection matrix, the vertex shader transforms vertices to clip space,
the rasterizer fills triangles interpolating UVs, the fragment shader samples the
texture and applies Blinn-Phong lighting, and the z-buffer discards hidden faces.

## Related
- [[ray-tracing-and-path-tracing]] — the physically based alternative for photorealism.
- [[geometry-processing-and-meshes]] — the surfaces being rendered.
- [[parallel-architectures-simd-gpu]] — the hardware the pipeline maps onto.
- [[matrices-and-linear-maps]] — transforms and projections are matrix math.

## Sources
Distilled from [[computer-graphics-texts-courses-and-seminal-papers]] (Marschner &
Shirley; *Real-Time Rendering*; Gouraud/Phong/Blinn; NeRF; Gaussian splatting).
