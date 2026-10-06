---
title: "CONCUR: Benchmarking LLMs for Concurrent Code Generation"
authors: "Jue Huang, Tarek Mahmud, Corina S. Pasareanu, Guowei Yang"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832286>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Leveraging Large Language Models \(LLMs\) for code generation has increasingly emerged as a common practice in the domain of software engineering\. Relevant benchmarks have been established to evaluate the code generation capabilities of LLMs\. However, existing benchmarks focus primarily on sequential code, lacking the ability to effectively evaluate LLMs on concurrent code generation\. Compared to sequential code, concurrent code exhibits greater complexity and possesses unique types of bugs, such as deadlocks and race conditions, that do not occur in sequential code\. Therefore, a benchmark for evaluating sequential code generation cannot be useful for evaluating concurrent code generation with LLMs\. To address this gap, we designed a benchmark CONCUR specifically aimed at evaluating the capability of LLMs to generate concurrent code\. CONCUR consists of a base set of 43 concurrency problems derived from a standard concurrency textbook, together with 72 validated mutant variants, resulting in 115 total problems\. The base problems serve as the semantic core of the benchmark, while the mutants expand linguistic and structural diversity\. We conducted an evaluation of a range of LLMs on CONCUR, highlighting limitations of current models\. Overall, our work provides a novel direction for evaluating the capability of LLMs to generate code with focus on concurrency\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->