---
title: "Revisiting Graph Representations for ML-Based Binary Code Similarity Detection: A Systematic Study"
authors: "Tengteng Yang, Yikun Hu, Jican Zhang, Lei Xue, Ming Fan, Liang Zhang"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-vuln", "query:malware"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832258>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Binary Code Similarity Detection \(BCSD\) is a foundational capability in software security, underpinning critical applications ranging from vulnerability detection to malware analysis\. While recent tools based on Machine Learning \(ML\) have achieved significant performance improvements, their efficacy is heavily contingent upon the underlying code representation\. Through a systematic literature review of ML\-based BCSD papers, we find that existing approaches typically leverage linear sequences or adopt graph\-based representations, with the latter constituting the majority \(77%\)\. Despite this prevalence, there is no consensus on which graph representation yields superior effectiveness\. Existing works usually couple graph construction with customized learning backbones and evaluate them on inconsistent benchmarks\. This makes isolating the representation&\#x27;s impact difficult\. Consequently, determining which graph topologies most effectively capture robust binary\-code semantics under controlled and comparable evaluation settings remains an open problem\. In this paper, we present a systematic study of graph representations for ML\-based BCSD to bridge this gap\. Specifically, we implement a modular evaluation framework that decouples graph construction from model training\. Using this framework, we systematically evaluate seven representative graph representations, finding that no single representation is universally dominant, that distinct topologies exhibit unique strengths depending on the evaluation scenario, and that their rankings are largely backbone\-stable despite varying absolute performance\. We further investigate their combination effectiveness in N\-day vulnerability detection and employ a tailored post\-hoc analysis tool to study model\-level structural reliance\. The results show that DFG, PDG, and SOG subgraph pairs more often preserve trained models&\#x27; similarity scores under pruning, while several other representations are more sensitive to structural reduction\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->