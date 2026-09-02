---
title: Computer vision texts, courses and seminal papers — Szeliski's Computer Vision: Algorithms and Applications (free), Hartley & Zisserman's Multiple View Geometry, Torralba–Isola–Freeman's Foundations of Computer Vision, Prince's CV: Models, Learning and Inference (free); CS231n, Michigan EECS 498, Nayar's First Principles of Computer Vision; Marr, Canny, SIFT, Viola–Jones, HOG, R-CNN → Faster R-CNN, YOLO, FCN, U-Net, ViT, CLIP, NeRF, SAM, Stable Diffusion
type: source
section: "6.5"
level: 400
tags: [szeliski, hartley-zisserman, multiple-view-geometry, torralba, isola, freeman, foundations-of-computer-vision, prince, cs231n, eecs-498, nayar, first-principles-of-computer-vision, marr, canny, lowe, sift, viola-jones, dalal-triggs, hog, girshick, r-cnn, faster-r-cnn, redmon, yolo, long, fcn, ronneberger, u-net, dosovitskiy, vit, radford, clip, mildenhall, nerf, kirillov, sam, segment-anything, rombach, stable-diffusion]
sources: []
authors: [Richard Szeliski, Richard Hartley, Andrew Zisserman, Antonio Torralba, Phillip Isola, William Freeman, Simon Prince, Shree Nayar, David Marr, John Canny, David Lowe, Paul Viola, Michael Jones, Navneet Dalal, Bill Triggs, Ross Girshick, Joseph Redmon, Jonathan Long, Olaf Ronneberger, Alexey Dosovitskiy, Alec Radford, Ben Mildenhall, Alexander Kirillov, Robin Rombach]
year: 2022
institution: various
url: https://szeliski.org/Book/
license: mixed (Szeliski and Prince free; H&Z and Torralba et al. commercial)
format: pdf
summary: Szeliski's Computer Vision: Algorithms and Applications (2nd ed. 2022, free; adopted by Cornell, MIT, CMU, Berkeley, Brown, Georgia Tech, Michigan courses) covers image formation, image processing (filtering, pyramids, geometric transforms), model fitting and optimization, deep learning, recognition (classification, detection, segmentation), feature detection and matching, image alignment and stitching, motion estimation, computational photography, structure from motion and SLAM, depth estimation, 3D reconstruction, and image-based rendering; Hartley & Zisserman is the reference for projective geometry, camera models, epipolar geometry, and bundle adjustment; Torralba, Isola & Freeman (2024) is the modern MIT text mixing signal processing, learning and generative models; Prince's earlier book is the probabilistic view; Nayar's First Principles lecture series is the physics of image formation; and the seminal papers run from Marr's levels of analysis and Canny's optimal edge detector through hand-designed features (SIFT's scale-invariant keypoints, Viola–Jones cascades with Haar features and AdaBoost, HOG + linear SVM for pedestrians) to the deep era — R-CNN/Fast/Faster R-CNN, YOLO, FCN and U-Net for dense prediction, ViT, CLIP's contrastive image–text pretraining, NeRF's neural radiance fields for view synthesis, Segment Anything's promptable segmentation foundation model, and Stable Diffusion's latent text-to-image generation.
---
# Computer vision: texts, courses, and seminal papers

## What they are
- **Szeliski** (2e 2022, free PDF; the book's site lists ~15 university courses using it):
  1 introduction; 2 image formation (geometric primitives and transforms, photometric
  image formation, the digital camera); 3 image processing (point operators, linear
  filtering, non-linear filtering, Fourier transforms, pyramids and wavelets, geometric
  transformations); 4 model fitting and optimization (least squares, robust statistics,
  MRFs); 5 deep learning (supervised learning, CNNs, more complex models); 6 recognition
  (instance recognition, image classification, object detection, semantic segmentation,
  video understanding, vision and language); 7 feature detection and matching (points,
  edges, contours, lines, segmentation); 8 image alignment and stitching; 9 motion
  estimation (translational alignment, parametric motion, optical flow, layered motion);
  10 computational photography (HDR, super-resolution, denoising, matting, texture
  synthesis); 11 structure from motion and SLAM; 12 depth estimation (epipolar geometry,
  stereo, multi-view stereo, monocular depth); 13 3D reconstruction; 14 image-based
  rendering (light fields, NeRF).
- **Hartley & Zisserman, Multiple View Geometry** (2e 2004): projective geometry, camera
  models and calibration, the fundamental and essential matrices, triangulation,
  homographies, trifocal tensor, bundle adjustment, RANSAC — the mathematical core of 3D
  vision. **Torralba, Isola & Freeman, Foundations of Computer Vision** (2024): images as
  signals, filters, learning, neural nets, 3D, generative models, sequences, and the
  "vision for" applications. **Prince** (2012, free): probabilistic models throughout.
- **Courses**: **CS231n** ([[deep-learning-texts-courses-and-seminal-papers]]); **Michigan
  EECS 498/598** (Johnson — CS231n's deeper successor); **Nayar, First Principles of
  Computer Vision** (Columbia; YouTube — image formation, lenses, sensing, features,
  stereo, motion, shape from shading, the physics before the learning); UCF CAP5415,
  Georgia Tech CS4476 (Hays), UIUC CS543.
- **Seminal**: Marr 1982 (*Vision*: computational / algorithmic / implementational
  levels; primal sketch → 2½-D sketch → 3D model); Canny 1986 (edge detection as
  optimization: Gaussian derivative, non-maximum suppression, hysteresis); Lowe 2004
  (**SIFT**: DoG scale-space extrema, orientation histograms — invariant keypoints for
  matching, the basis of panoramas and SfM); Viola & Jones 2001 (real-time face detection:
  integral images, Haar features, AdaBoost, attentional cascade); Dalal & Triggs 2005
  (**HOG** + linear SVM — the pre-deep detector); Girshick et al. 2014–15 (**R-CNN** → Fast →
  **Faster R-CNN** with region proposal networks); Redmon et al. 2016 (**YOLO**: single-shot
  detection as regression); Long et al. 2015 (**FCN**: end-to-end dense prediction);
  Ronneberger et al. 2015 (**U-Net**); Dosovitskiy et al. 2020 (**ViT**); Radford et al. 2021
  (**CLIP**: 400 M image–text pairs, contrastive pretraining, zero-shot classification by
  prompt); Mildenhall et al. 2020 (**NeRF**: an MLP mapping (x, direction) → (colour,
  density), rendered by volume integration, trained from posed images); Kirillov et al. 2023
  (**Segment Anything**: promptable segmentation trained on 1 B masks); Rombach et al. 2022
  (**Stable Diffusion** — [[deep-generative-models]]).

## Key ideas → pages
[[computer-vision-fundamentals]], [[multiple-view-geometry-and-3d-vision]],
[[self-supervised-and-contrastive-learning]], [[convolutional-neural-networks]] (detection
and segmentation architectures), [[transformers-and-attention]] (ViT),
[[deep-generative-models]] (diffusion, NeRF-adjacent).

## What they add
Szeliski for everything classical and its deep replacements side by side; H&Z when the
problem is geometry; Nayar for the physics; the paper list shows the field's arc from
hand-designed invariances (SIFT, HOG) to learned ones (CNNs), to learned from language
(CLIP) and to learned 3D representations (NeRF).
