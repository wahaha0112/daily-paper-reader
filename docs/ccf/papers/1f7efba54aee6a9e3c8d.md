---
title: "Look Before You Leap: Context-Sensitive GUI Grounding for Boosting Automated Extended Reality (XR) Testing"
authors: "Shuqing Li, Binchang Li, Yepang Liu, Cuiyun Gao, Jianping Zhang, Shing-Chi Cheung, Michael R. Lyu"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808134>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

In recent years, Extended Reality \(XR\) has emerged as a transformative technology, offering users immersive and interactive experiences across diversified virtual or virtual\-real environments\. Users can interact with XR applications \(apps\) through interactable GUI elements \(IGEs\) on the stereoscopic three\-dimensional \(3D\) graphical user interface \(GUI\)\. IGE constitutes the fundamental element of XR GUI, embodying rich semantic information\. The accurate recognition and precise understanding of these IGEs is instrumental, serving as the foundation of GUI grounding, which can facilitates downstream tasks, including automated XR testing\. A straightforward XR test generator can interact randomly within the app’s 3D environment, making it trapped in uninteractable space and resulting in an ineffective and inefficient testing process\. In contrast, a more intelligent test generator, informed by the accurate locations and semantics of IGEs, can make wiser decisions on interaction targets and orders, forming test sequences that cover more functionalities faster\. The most recent IGE detection approaches in SE are designed for 2D mobile apps and typically train a supervised object detection model based on a large\-scale manually\-labeled GUI dataset, usually with a pre\-defined set of clickable GUI element categories like buttons and spinners\. Such approaches can hardly be applied to IGE detection in XR apps, due to a multitude of challenges including complexities posed by open\-vocabulary and heterogeneous IGE categories, intricacies of context\-sensitive interactability, and the necessities of precise spatial perception and visual\-semantic alignment for accurate IGE detection results\. Thus, it is necessary to embark on the IGE research tailored to XR apps\. In this paper, we propose the first zero\-shot context\-sensitive interactable GUI element detection framework for Extended Reality apps, named Orienter\. Rather than relying on generic visual grounding which fails in 3D environments, Orienter introduces a structured workflow tailored to XR constraints\. It first synthesizes XR\-specific semantic contexts \(e\.g\., global interaction paradigms and 3D spatial properties\) before performing detection\. To overcome severe spatial hallucinations inherent in LMMs, the detection process is iterated within an XR\-constrained reflection loop\. Specifically, Orienter contains three components, including \(1\) Semantic context comprehension for capturing the apps’ GUI context, \(2\) Reflection\-directed IGE candidate detection for identifying and localizing valid GUI elements based on multi\-perspective description guided IGE detection, as well as feedback\-directed reflection, and \(3\) Context\-sensitive interactability classification which integrates semantic contexts for interactability prediction\. To evaluate our approach and facilitate follow\-up research, we construct the first benchmark dataset which contains 1,552 images from 100 industrial\-setting apps on Steam, with 4,470 interactable annotations across 766 semantics categories\. Extensive experiments on the dataset demonstrate that Orienter is more effective than the state\-of\-the\-art GUI element detection approaches, including general or GUI\-automation\-targeted vision language models, and deep learning based models, surpassing their F1 Score by at least 34\.9% and 20\.1× in distinguishing the interactibility and semantics of the IGEs, respectively\. Orienter is beneficial for boosting the performance of automatic testing by isolating the interactable action space from the whole space, regardless of the testing strategies employed\. Experiments demonstrate that Orienter\-guided testing covers 103\.1% more IGEs with 125\.7% more effective interactions than testing without action space isolation\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->