---
title: "Compositional Shape Analysis with Shared Abduction and Biabductive Loop Acceleration"
authors: "Florian Sextl, Adam Rogalewicz, Tomáš Vojnar, Florian Zuleger"
date: "2026-08-29"
source: "TOPLAS"
tags: ["query:code-vuln", "query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOPLAS · CCF-A · 2026-08-29（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3844730>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Biabduction\-based shape analysis is a compositional verification and analysis technique that can prove memory safety in the presence of complex, linked data structures\. Despite its usefulness, several open problems persist for this kind of analysis; two of which we address in this paper\. On the one hand, the original analysis is path\-sensitive but cannot combine safety requirements for related branches\. This causes the analysis to require additional soundness checks and decreases the analysis’ precision\. We extend the underlying symbolic execution and propose a framework for shared abduction where a common pre\-condition is maintained for related computation branches\. On the other hand, prior implementations lift loop acceleration methods from forward analysis to biabduction analysis by applying them separately on the pre\- and post\-condition, which can lead to imprecise or even unsound acceleration results that do not form a loop invariant\. In contrast, we propose biabductive loop acceleration , which explicitly constructs and checks candidate loop invariants\. For this, we also introduce a novel heuristic called shape extrapolation \. This heuristic takes advantage of locality in the handling of list\-like data structures \(which are the most common data structures found in low\-level code\) and jointly accelerates pre\- and post\-conditions by extrapolating the related shapes\. In addition to making the analysis more precise, our techniques also make biabductive analysis more efficient since they are sound in just one analysis phase\. In contrast, prior techniques always require two phases \(as the first phase can produce contracts that are unsound and must hence be verified\)\. We experimentally confirm that our techniques improve on prior techniques; both in terms of precision and runtime of the analysis\. This work extends the conference paper \[32\]\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->