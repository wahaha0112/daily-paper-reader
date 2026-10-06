---
title: "xFUZZ: A Flexible Framework for Fine-Grained, Runtime-Adaptive Fuzzing Strategy Composition"
authors: "Dongsong Yu, Yiyi Wang, Chao Zhang, Yang Lan, Zhiyuan Jiang, Shuitao Gan, Zheyu Ma, Wende Tan"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:code-vuln", "query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728873>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Fuzzing is one of the most efficient techniques for detecting vulnerabilities in software\. Existing approaches struggle with performance inconsistencies across different targets and rely on rigid, coarse\-grained fuzzing strategy composition, limiting the flexibility to adaptively combine the strengths of different fuzzing strategies at runtime\. To address these challenges, we present xFUZZ , a flexible and extensible fuzzing framework supporting fine\-grained, runtime\-adaptive strategy composition\. xFUZZ integrates popular input scheduling and mutation scheduling strategies as fine\-grained, independently switchable plugins, allowing users to adaptively replace any plugins throughout the fuzzing campaign\. Furthermore, we introduce an adaptive algorithm based on Sliding\-Window Thompson Sampling, which dynamically selects the optimal composition of the fuzzing strategy during the fuzzing campaign\. Experimental results show that xFUZZ outperforms state\-of\-the\-art fuzzers by achieving a 10\.07% increase in unique vulnerability discovery and a 4\.94% improvement in code coverage\. Notably, xFUZZ is the first to detect 21 out of 37 vulnerabilities in the test suite, establishing its effectiveness across varied targets\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->