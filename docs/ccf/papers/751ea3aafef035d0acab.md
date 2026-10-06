---
title: "Hunting CUDA Bugs at Scale with cuFuzz"
authors: "Mohamed Tarek Ibn Ziad, Christos Kozyrakis"
date: "2026-04-10"
source: "OOPSLA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2026-04-10（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3798231>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

GPUs play an increasingly important role in modern software\. However, the heterogeneous host\-device execution model and expanding software stacks make GPU programs prone to memory\-safety and concurrency bugs that evade static analysis\. While fuzz\-testing, combined with dynamic error checking tools, offers a plausible solution, it remains underutilized for GPUs\. In this work, we identify three main obstacles limiting prior GPU fuzzing efforts: \(1\) kernel\-level fuzzing leading to false positives, \(2\) lack of device\-side coverage\-guided feedback, and \(3\) incompatibility between coverage and sanitization tools\. We present cuFuzz, the first CUDA\-oriented fuzzer that makes GPU fuzzing practical by addressing these obstacles\. cuFuzz uses whole program fuzzing to avoid false positives from independently fuzzing device\-side kernels\. It leverages NVBit to instrument device\-side instructions and merges the resultant coverage with compiler\-based host coverage\. Finally, cuFuzz decouples sanitization from coverage collection by executing host\- and device\-side sanitizers in separate processes\. cuFuzz uncovers 43 previously unknown bugs \(19 in commercial libraries\) across 14 CUDA programs, including illegal memory accesses, uninitialized reads, and data races\. cuFuzz achieves significantly more discovered edges and unique inputs compared to baseline approaches, especially on closed\-source targets\. Moreover, we quantify the execution time overheads of the different cuFuzz components and add persistent\-mode support to improve the overall fuzzing throughput\. Our results demonstrate that cuFuzz is an effective and deployable addition to the GPU testing toolbox\. cuFuzz is publicly available at https://github\.com/NVlabs/cuFuzz/ \.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->