---
title: Convolutional neural networks — convolution as local, weight-shared linear maps (kernels, stride, padding, channels, receptive fields), pooling, translation equivariance, LeNet → AlexNet → VGG → Inception → ResNet → EfficientNet/ConvNeXt, batch statistics and parameter/FLOP accounting, transfer learning, and the architectures for detection and segmentation
type: concept
section: "6.3"
level: 400
tags: [cnn, convolutional-neural-network, convolution, kernel, filter, stride, padding, channels, feature-maps, receptive-field, weight-sharing, translation-equivariance, pooling, max-pooling, global-average-pooling, 1x1-convolution, dilated-convolution, depthwise-separable, lenet, alexnet, vgg, inception, googlenet, resnet, residual-block, bottleneck, densenet, mobilenet, efficientnet, convnext, imagenet, parameter-count, flops, transfer-learning, fine-tuning, object-detection, faster-rcnn, yolo, segmentation, fcn, u-net, visualization, saliency, adversarial-examples]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: A convolutional layer slides small learned kernels over the input, computing the same dot product at every position — a linear map that is local (each output sees a receptive field), weight-shared (the same filter everywhere, so parameters don't grow with image size), and translation-equivariant (shift the input, the feature map shifts) — producing a stack of channel feature maps whose size is set by kernel size, stride and padding; pooling (max, average; now often strided convolutions) downsamples and adds translation invariance, receptive fields grow with depth so later layers see whole objects, and 1×1 convolutions mix channels cheaply; the architectural history is LeNet (1998), AlexNet (2012: ReLU, dropout, GPUs, ImageNet), VGG (uniform 3×3 stacks — two 3×3 = one 5×5 receptive field with fewer parameters), Inception (parallel multi-scale branches, 1×1 bottlenecks), ResNet (residual blocks, batchnorm, 152 layers, global average pooling replacing giant FC layers), then efficiency (MobileNet's depthwise-separable convolutions, EfficientNet's compound scaling) and ConvNeXt's modernization against vision transformers; pretrained ImageNet backbones transfer to almost every vision task by fine-tuning, and detection (R-CNN family, YOLO, DETR) and segmentation (FCN, U-Net with skip connections, Mask R-CNN) reuse the backbone with task heads.
---
# Convolutional neural networks

**In one sentence.** Replace the dense matrix of an MLP with a small kernel applied at every
position: locality, weight sharing, and translation equivariance are the inductive bias that
made images learnable, and residual connections made it deep.

## The convolution layer (Goodfellow ch. 9; CS231n lecture 5; D2L ch. 7)
Input tensor C_in × H × W; a layer has C_out kernels of size C_in × k × k; output channel c at
position (i, j) = b_c + Σ over the k×k×C_in window of kernel weights × inputs (technically
cross-correlation). Hyperparameters: **kernel size** k (3 dominates), **stride** s (downsample),
**padding** p ("same" keeps size); output size ⌊(H + 2p − k)/s⌋ + 1. Parameters: C_out·(C_in·k² + 1)
— independent of H, W (an MLP on 224×224×3 → 4096 would need 600 M weights per layer);
FLOPs ≈ 2·H_out·W_out·C_out·C_in·k². **Receptive field**: the input region affecting an
output; grows by (k−1) per layer (× stride products) — deep stacks of 3×3 see the whole
image; **dilated** convolutions grow it without parameters. **Translation equivariance**:
conv(shift(x)) = shift(conv(x)) — the symmetry prior (group-equivariant CNNs generalize it
to rotations). **1×1 convolutions**: per-pixel channel mixing (bottlenecks, cheap
nonlinearity). Implementation: im2col + GEMM, Winograd, FFT ([[fft]]) for large kernels, cuDNN
kernels ([[gpu-programming-cuda]]); channels-last memory layout for tensor cores.

## Pooling, normalization, and the classic block
**Max pooling** (2×2, stride 2) halves resolution, adds local invariance, no parameters;
**average pooling**; modern nets prefer strided convs and end with **global average
pooling** (one number per channel → classifier; removes the parameter-heavy FC layers and
lets input size vary). Block: conv → BatchNorm → ReLU (→ pool) — [[neural-network-training]].
Feature hierarchy (visualizations, Zeiler & Fergus 2014): layer 1 = Gabor-like edges and
colour blobs, then textures, parts, objects — [[deep-learning-basics]] on why depth.

## Architectures (CS231n lecture 6; D2L ch. 8)
| Net | Year | Idea | ImageNet top-5 err. |
|---|---|---|---|
| LeNet-5 | 1998 | conv+pool+FC on MNIST; gradient-based learning | — |
| AlexNet | 2012 | 8 layers, ReLU, dropout, augmentation, 2 GPUs; 60 M params | 15.3 % (vs 26 %) |
| VGG-16/19 | 2014 | only 3×3 convs, doubling channels as resolution halves; 138 M params, 15 GFLOPs | 7.3 % |
| GoogLeNet/Inception | 2014 | parallel 1×1/3×3/5×5 branches, 1×1 bottlenecks, auxiliary heads; 5 M params | 6.7 % |
| ResNet-50/101/152 | 2015 | residual blocks x + F(x), bottleneck 1×1-3×3-1×1, BatchNorm; 25 M params for R-50 | 3.6 % |
| DenseNet, ResNeXt, SENet | 2016–17 | dense skips; grouped convs (cardinality); channel attention | ~2–3 % |
| MobileNet, EfficientNet | 2017–19 | depthwise-separable convs (k²+C_out vs k²C_out per channel); compound scaling of depth/width/resolution | mobile/efficiency |
| ConvNeXt | 2022 | ResNet modernized with ViT tricks (7×7 depthwise, LayerNorm, GELU, fewer activations) — matches Swin transformers | |
Lessons: deeper + residual > wider; small kernels stacked; batchnorm everywhere; compute
scales predictably ([[scaling-laws]]); **Vision Transformers** (Dosovitskiy 2020: 16×16
patches as tokens — [[transformers-and-attention]]) overtake CNNs given large pretraining
data, while CNNs keep the edge in data efficiency and on-device inference. Equivalent
accounting: ResNet-50 ≈ 4 GFLOPs/image, 25 M parameters, ~100 MB activations at batch 1
([[roofline-model]]: convs are compute-bound, depthwise convs memory-bound).

## Transfer learning and downstream tasks (CS231n lecture 9)
Pretrained ImageNet (or CLIP/DINO self-supervised — [[self-supervised-and-contrastive-learning]])
backbones: freeze and train a linear head (small data), or **fine-tune** all layers with a
small learning rate (more data); lower layers are generic, higher layers task-specific
([[transfer-learning-and-fine-tuning]]). **Detection**: R-CNN → Fast → **Faster R-CNN**
(region proposal network, RoI pooling, two-stage), **YOLO**/SSD/RetinaNet (one-stage, anchor
grids, focal loss), **DETR** (set prediction with transformers, Hungarian matching —
[[network-flow]]); metrics mAP@IoU. **Segmentation**: **FCN** (convolutionalize the
classifier, upsample), **U-Net** (encoder–decoder with skip connections — medical imaging,
diffusion backbones), DeepLab (atrous convs), **Mask R-CNN** (instance masks), Segment
Anything. **Understanding**: saliency maps, Grad-CAM, feature visualization by optimization,
and **adversarial examples** (imperceptible perturbations flip predictions — Szegedy 2013,
Goodfellow 2014 FGSM; [[ai-safety-and-alignment]]). Vision beyond classification:
[[computer-vision-fundamentals]].

## Pitfalls
- Confusing equivariance (conv) with invariance (pooling/global pooling gives it).
- Miscomputing output sizes/receptive fields; padding asymmetries with even kernels.
- Fine-tuning with the pretraining learning rate (destroys features); forgetting to
  normalize inputs with the pretraining mean/std.
- Comparing architectures without matching FLOPs/params/training recipe (most "SOTA"
  gaps are recipe gaps — Wightman et al. 2021).

## Related
- [[deep-learning-basics]], [[neural-network-training]], [[transformers-and-attention]],
  [[computer-vision-fundamentals]], [[transfer-learning-and-fine-tuning]],
  [[self-supervised-and-contrastive-learning]], [[gpu-programming-cuda]], [[roofline-model]],
  [[fft]], [[network-flow]], [[scaling-laws]], [[ai-safety-and-alignment]].

## Sources
Goodfellow ch. 9 (ToC read); CS231n lectures 5–6, 9 (schedule read); D2L ch. 7–8; Prince ch. 10–11; LeCun et al. 1998; Krizhevsky et al. 2012; Simonyan & Zisserman 2014; Szegedy et al. 2015; He et al. 2015; Howard et al. 2017; Tan & Le 2019; Liu et al. 2022 (ConvNeXt); Zeiler & Fergus 2014.
