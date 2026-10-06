---
title: "Memory-Safety Verification of Open Programs with Angelic Assumptions"
authors: "Gourav Takhar, Baldip Bijlani, Prantik Chatterjee, Akash Lal, Subhajit Roy"
date: "2025-10-09"
source: "OOPSLA"
tags: ["query:code-analysis", "query:skill"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2025-10-09（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3763090>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

An open program is one for which the complete source code is not available, which is a reality for real\-world program verification\. Software verification tools tend to assume the worst about any unconstrained behavior and this can yield an enormous number of spurious warnings for open programs\. For any serious verification effort, the engineer must invest time up\-front in building a suitable model \(or mock\) of any missing code, which is time\-consuming and error\-prone\. Inaccuracies in the mocks can lead to incorrect verification results\. In this paper, we demonstrate a technique that is capable of distinguishing between false positives and actual bugs from potential memory\-safety violations in an open program with high accuracy\. Central to the technique is the ability of making angelic assumptions about missing code\. To accomplish this, we first mine a set of idiomatic patterns in buffer\-manipulating programs using a large language model \(LLM\)\. This is complemented by a formal synthesis strategy that performs property\-directed reasoning to select, adapt and instantiate these idiomatic patterns into angelic assumptions on the target program\. Overall, our system, Seeker, guarantees that a program is deemed correct only if it can be verified under a well\-defined set of “trusted” idiomatic patterns\. In our experiments over a set of benchmarks curated from popular open\-source software, our tool Seeker is able to identify 79% of the false positives with zero false negatives\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->