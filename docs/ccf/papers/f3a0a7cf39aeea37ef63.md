---
title: "Dependent Coeffects for Local Sensitivity Analysis"
authors: "Victor Sannier, Patrick Baillot"
date: "2026-01-08"
source: "POPL"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：POPL · CCF-A · 2026-01-08（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3776670>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Differential privacy is a formal definition of privacy that bounds the maximum acceptable information leakage when a query is performed on sensitive data\. To ensure this property, a key technique involves bounding the query’s sensitivity \(how much input variations affect the output\) and adding noise to the result according to this quantity\. While prior work like the Fuzz type system focuses on global sensitivity, many useful queries have infinite global sensitivity, restricting the scope of such approaches\. This limitation can be addressed by considering a more fine\-grained measure: local sensitivity, which quantifies output change for inputs adjacent to a specific dataset\. In this article, we introduce Local Fuzz, a type system with dependent coeffects designed to bound the local sensitivity of programs written in a simple functional language\. We provide a denotational semantics for this system in the category of extended premetric spaces, leveraging the recently introduced construction of a dependently graded comonad\. Finally, we illustrate how Local Fuzz can lead to better differential privacy guarantees than Fuzz, both for mechanisms that rely on global sensitivity and for those that leverage local sensitivity, such as the Propose\-Test\-Release framework\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->