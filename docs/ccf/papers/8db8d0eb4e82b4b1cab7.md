---
title: "GPU-Accelerated Flow-Sensitive Pointer Analysis for C/C++ Programs"
authors: "Jiaqi He, Karim Ali"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-vuln"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808145>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Flow\-sensitive pointer analysis offers highly precise results that are essential for various security analyses, bug detection tools, and compiler optimizations\. However, its high computational cost often leads to prohibitively long analysis times, especially for large, real\-world programs\. Despite decades of research, state\-of\-the\-art algorithms still struggle to achieve acceptable performance at industrial scale, forcing developers to choose less precise alternatives\. To overcome these limitations, we present GPA, a GPU\-accelerated flow\-sensitive pointer analysis for C/C\+\+ programs\. To maximize hardware utilization, GPA dynamically balances computation by combining the massive parallelism of GPUs with a graph neural network that predicts per\-variable workloads\. Compared to state\-of\-the\-art CPU\-based analyses, GPA improves runtime performance by a factor of 1\.3× to 14× on large programs \(i\.e\., ≥275 KLOC LLVM IR\) without sacrificing precision\. However, on most small programs \(i\.e\., &lt;100 KLOC LLVM IR\) and some medium ones \(i\.e\., 100–275 KLOC LLVM IR\), traditional CPU implementations run faster due to the memory management overhead on GPUs that GPA incurs\. By making the computation of highly precise pointer information more tractable, GPA enables running analyses and developer tools that were previously infeasible on large codebases\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->