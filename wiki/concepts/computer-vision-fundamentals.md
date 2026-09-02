---
title: Computer vision fundamentals — image formation (pinhole camera, lenses, sensors, colour), images as signals (convolution, Gaussian and derivative filters, Fourier view, pyramids, aliasing), edges (Canny) and corners (Harris), invariant features (SIFT, HOG) and matching (RANSAC), classical detection (Viola–Jones) and segmentation (k-means, graph cuts, superpixels), optical flow and tracking, and how deep learning replaced each stage
type: concept
section: "6.5"
level: 400
tags: [computer-vision, image-formation, pinhole-camera, perspective-projection, lens, focal-length, sensor, bayer, color-spaces, gamma, image-processing, convolution, linear-filters, gaussian-blur, derivative-filters, sobel, laplacian, fourier, sampling, aliasing, nyquist, image-pyramids, gaussian-pyramid, laplacian-pyramid, edge-detection, canny, non-maximum-suppression, hysteresis, corners, harris, scale-space, sift, dog, keypoints, descriptors, feature-matching, ransac, homography, hog, viola-jones, integral-image, haar, cascade, segmentation, k-means, mean-shift, graph-cuts, superpixels, optical-flow, lucas-kanade, horn-schunck, tracking, kalman, marr, deep-learning-replacement]
sources: [computer-vision-texts-courses-and-seminal-papers]
summary: Classical computer vision is the physics of how a 3D scene becomes a 2D array (perspective projection through a pinhole/lens, sensor sampling, Bayer colour, gamma) plus the signal processing of what to do with the array — linear filtering by convolution (Gaussian smoothing, derivative filters, the Fourier view of blur and sharpening, sampling and aliasing, Gaussian/Laplacian pyramids for multi-scale), edge detection (Canny: Gaussian-derivative gradients, non-maximum suppression, hysteresis thresholds), corner detection (Harris: eigenvalues of the structure tensor), scale-invariant keypoints and descriptors (SIFT: difference-of-Gaussian extrema, orientation-normalized gradient histograms) matched robustly with RANSAC to fit homographies for stitching or recognize objects, histogram-of-gradients features with linear SVMs for detection, boosted Haar-feature cascades for real-time faces (Viola–Jones), segmentation by clustering pixels (k-means, mean shift), graph cuts and superpixels, and motion estimation by optical flow (brightness constancy, Lucas–Kanade's local least squares, Horn–Schunck's global smoothness) and tracking with Kalman filters; deep learning replaced the learned parts stage by stage — CNN features for SIFT/HOG, detectors and segmenters for cascades and graph cuts, learned flow (RAFT) and depth — but the formation model, filtering, geometry and the classical vocabulary of invariance remain how practitioners reason about what a network must learn.
---
# Computer vision fundamentals

**In one sentence.** An image is a projection of the world sampled onto a grid, and
classical vision is the chain pinhole → filter → gradient → feature → match/group →
motion that deep networks now learn end to end — but whose stages still name the
invariances (scale, rotation, illumination, viewpoint) any vision system must achieve.

## Image formation (Szeliski ch. 2; Nayar lectures 1–3)
**Pinhole camera**: a 3D point (X, Y, Z) projects to (f X/Z, f Y/Z) — perspective: parallel
lines meet at vanishing points, size falls with depth; in homogeneous coordinates
x = K [R | t] X with intrinsics K (focal length, principal point, skew) and extrinsics
([[multiple-view-geometry-and-3d-vision]]). **Lenses** gather light at the cost of depth of
field (aperture, f-number, thin-lens equation, focus, vignetting, radial distortion).
**Sensors**: CCD/CMOS photon counting (shot noise ∝ √signal, read noise, dynamic range,
exposure/ISO), **Bayer** colour filter array + demosaicing, white balance, **gamma** (sRGB
non-linearity — linearize before averaging light), **colour spaces** (RGB, HSV, Lab; luminance
vs chrominance), the imaging pipeline (ISP). Photometric formation: Lambertian reflectance
I = ρ (n · l), specular (Phong), shading/shape-from-shading ([[computer-graphics-rendering]]).

## Images as signals: filtering (Szeliski ch. 3; Torralba–Isola–Freeman part II)
**Linear filtering** = convolution/correlation with a kernel ([[convolutional-neural-networks]]
uses exactly this, learned): box and **Gaussian** blur (separable — O(k) per pixel instead of
O(k²); σ sets scale), **derivative** filters (Sobel, Gaussian derivatives — differentiate a
smoothed image, since differentiation amplifies noise), Laplacian/LoG for blobs, sharpening
(unsharp mask). **Fourier view**: convolution = multiplication of spectra ([[fft]]); blur is a
low-pass filter; **sampling** and **aliasing** — downsample only after low-pass filtering
(Nyquist — [[signals-and-sampling]]); **image pyramids**: Gaussian (blur + subsample) and
**Laplacian** (band-pass differences — multi-scale blending, compression, coarse-to-fine
search). Non-linear filters: median (salt-and-pepper noise), **bilateral** (edge-preserving:
weight by spatial and intensity distance), morphology (erode/dilate). Geometric transforms
(warp by inverse mapping + interpolation), histogram equalization, HDR and tone mapping
([[computational-photography]]).

## Edges, corners, and features — matching keypoints to stitch photos into a panorama (Szeliski ch. 7; Canny 1986; Harris 1988; Lowe 2004)
**Canny**: Gaussian-derivative gradient magnitude and orientation → **non-maximum
suppression** along the gradient (thin edges) → **hysteresis** (high threshold to start,
low to continue) — derived as optimal for detection, localization, single response.
**Harris corners**: the structure tensor M = Σ_w [Iₓ² IₓI_y; IₓI_y I_y²]; two large eigenvalues
= corner (response det M − k·tr² M); rotation-invariant, not scale-invariant. **Scale
space**: detect at extrema over σ of the normalized Laplacian / **difference of Gaussians**
(DoG). **SIFT**: DoG extrema in (x, y, σ) → subpixel refinement, edge rejection →
dominant orientation from a gradient histogram (rotation invariance) → **descriptor**: 4×4
cells × 8 orientation bins = 128-d, normalized (illumination invariance); matched by
nearest neighbour with the ratio test. Successors: SURF, ORB (binary, fast — used in
SLAM), and learned descriptors (SuperPoint) — [[similarity-search-and-lsh]] for large-scale
matching. **Feature matching + RANSAC** (Fischler & Bolles 1981): sample a minimal set
(4 correspondences for a homography), fit, count inliers, repeat; robust to the majority of
matches being wrong — used for panoramas (Szeliski ch. 8: homography warping, blending),
object recognition, and SfM. **HOG** (Dalal & Triggs): gradient orientation histograms over
a dense grid of cells with block normalization + linear SVM ([[kernels-and-support-vector-machines]])
sliding over an image pyramid — the pedestrian detector; deformable part models extended
it. **Viola–Jones**: Haar-like rectangle features computed in O(1) with the **integral
image** (prefix sums in 2D), selected by **AdaBoost** ([[decision-trees-and-ensembles]]), arranged
in an **attentional cascade** so most windows are rejected early — real-time faces in 2001,
still in cameras.

## Segmentation and grouping (Szeliski ch. 7.5; Torralba part V)
Cluster pixels by colour/position (**k-means** — [[k-means-clustering]]; **mean shift** —
mode seeking in feature space); **graph-based**: normalized cuts (spectral —
[[unsupervised-learning-em-and-mixture-models]]), Felzenszwalb–Huttenlocher, **graph cuts**
with MRF energies (data term + smoothness; min-cut/max-flow — [[network-flow]]) for
interactive GrabCut; **superpixels** (SLIC) as a preprocessing unit; active contours/snakes,
watershed. Replaced by FCN/U-Net/Mask R-CNN/SAM for semantic, instance, and panoptic
segmentation ([[convolutional-neural-networks]]) — but MRF/CRF smoothing and the
metrics (IoU, boundary F) persist.

## Motion: optical flow and tracking (Szeliski ch. 9; Lucas & Kanade 1981; Horn & Schunck 1981)
**Brightness constancy** I(x + u, y + v, t + 1) = I(x, y, t) → linearized: Iₓu + I_y v + Iₜ = 0 —
one equation, two unknowns per pixel (the **aperture problem**: only the normal flow is
observable at an edge). **Lucas–Kanade**: assume constant flow in a window, solve least
squares (needs a "corner" — the Harris matrix again), coarse-to-fine on a pyramid for large
motions; **Horn–Schunck**: global smoothness regularizer, variational solution. Feature
tracking (KLT), background subtraction, **Kalman** filtering for tracked objects
([[state-estimation-and-kalman-filters]]), data association (Hungarian matching —
[[network-flow]]), and modern learned flow (FlowNet, **RAFT**: correlation volumes + iterative
GRU updates) and video understanding ([[computer-vision-texts-courses-and-seminal-papers]]).

## Recognition: the deep replacement (Szeliski ch. 5–6)
Bag-of-visual-words (SIFT → k-means codebook → histogram → SVM) was the 2005–2011 recipe;
AlexNet (2012) ended it. Today: classification, detection, segmentation, keypoints, depth,
flow are all CNN/ViT heads on pretrained backbones ([[convolutional-neural-networks]],
[[transformers-and-attention]]), increasingly pretrained without labels
([[self-supervised-and-contrastive-learning]]: CLIP, DINO, MAE) and prompted (SAM, open-
vocabulary detection). The classical layer explains the failures: aliasing from strided
convs (anti-aliased CNNs), lack of rotation/scale invariance (augmentation or equivariant
nets), texture bias, and sensitivity to gamma/colour pipelines between train and deploy.

## Pitfalls
- Downsampling without low-pass filtering (aliasing); averaging gamma-encoded pixels.
- Differentiating an unsmoothed image; a single Canny threshold (no hysteresis).
- Matching features without the ratio test / RANSAC; fitting a homography to a non-planar
  scene or a rotating-only camera assumption violated by translation.
- Lucas–Kanade on large motions without a pyramid; tracking without handling occlusion.
- Evaluating a deep model on images processed by a different ISP than training.

## Related
- [[multiple-view-geometry-and-3d-vision]], [[self-supervised-and-contrastive-learning]],
  [[convolutional-neural-networks]], [[transformers-and-attention]], [[fft]],
  [[signals-and-sampling]], [[kernels-and-support-vector-machines]],
  [[decision-trees-and-ensembles]], [[k-means-clustering]], [[network-flow]],
  [[state-estimation-and-kalman-filters]], [[similarity-search-and-lsh]],
  [[computer-graphics-rendering]], [[computational-photography]].

## Sources
Szeliski 2e ch. 2–3, 5–9 (ToC/site read); Nayar, First Principles lectures; Torralba, Isola & Freeman 2024; Canny 1986; Harris & Stephens 1988; Lowe 2004; Fischler & Bolles 1981; Dalal & Triggs 2005; Viola & Jones 2001; Lucas & Kanade 1981; Horn & Schunck 1981; Teed & Deng 2020 (RAFT).
