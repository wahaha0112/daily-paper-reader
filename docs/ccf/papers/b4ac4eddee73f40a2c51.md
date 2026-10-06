---
title: "DeclarUI: Bridging Design and Development with Automated Declarative UI Code Generation"
authors: "Ting Zhou, Yanjie Zhao, Xinyi Hou, Xiaoyu Sun, Kai Chen, Haoyu Wang"
date: "2025-06-19"
source: "FSE"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2025-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3715726>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Declarative UI frameworks have gained widespread adoption in mobile app development, offering benefits such as improved code readability and easier maintenance\. Despite these advantages, the process of translating UI designs into functional code remains challenging and time\-consuming\. Recent advancements in multimodal large language models \(MLLMs\) have shown promise in directly generating mobile app code from user interface \(UI\) designs\. However, the direct application of MLLMs to this task is limited by challenges in accurately recognizing UI components and comprehensively capturing interaction logic\. To address these challenges, we propose DeclarUI, an automated approach that synergizes computer vision \(CV\), MLLMs, and iterative compiler\-driven optimization to generate and refine declarative UI code from designs\. DeclarUI enhances visual fidelity, functional completeness, and code quality through precise component segmentation, Page Transition Graphs \(PTGs\) for modeling complex inter\-page relationships, and iterative optimization\. In our evaluation, DeclarUI outperforms baselines on React Native, a widely adopted declarative UI framework, achieving a 96\.8% PTG coverage rate and a 98% compilation success rate\. Notably, DeclarUI demonstrates significant improvements over state\-of\-the\-art MLLMs, with a 123% increase in PTG coverage rate, up to 55% enhancement in visual similarity scores, and a 29% boost in compilation success rate\. We further demonstrate DeclarUI’ s generalizability through successful applications to Flutter and ArkUI frameworks\. User studies with professional developers confirm that DeclarUI’ s generated code meets industrial\-grade standards in code availability, modification time, readability, and maintainability\. By streamlining app development, improving efficiency, and fostering designer\-developer collaboration, DeclarUI offers a practical solution to the persistent challenges in mobile UI development\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->