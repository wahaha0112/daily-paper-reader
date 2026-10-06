---
title: "Defusing Logic Bombs in Symbolic Execution with LLM-Generated Ghost Code"
authors: "Dimitrios Stamatios Bouras, Sergey Mechtaev"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832126>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Symbolic execution is a powerful program analysis technique, but its effectiveness is fundamentally limited by solver\-hostile program fragments, complex numerical reasoning, and unbounded heap structures\. Recent work proposed replacing constraint solvers with large language models \(LLMs\) to bypass these limitations, but such approaches struggle to analyze real\-world codebases, where deep execution paths require globally consistent reasoning across many interacting constraints\. We present Gordian, a hybrid symbolic execution framework that uses LLMs selectively to generate lightweight ghost code that aids an SMT solver in handling solver\-hostile code fragments, while preserving its precise, global reasoning capability\. In particular, we propose three types of ghost code: \(1\) inversion of difficult code fragments with iterative bidirectional constraint propagation, \(2\) modeling via solver\-friendly surrogates while preserving relevant behavior, and \(3\) semantic partitioning of unbounded heap spaces\. We implemented Gordian on top of the KLEE symbolic execution engine and evaluated it on synthetic “logic bombs” capturing distinct symbolic reasoning challenges, a popular mathematical library FDLibM, and four structured\-input programs \(libexpat, jq, bc and libyaml\)\. Across benchmarks, Gordian improves coverage by 28\.5–115\.2% over traditional symbolic execution baseline and by 74\.1–189\.8% over LLM\-based symbolic execution baselines, while reducing LLM token usage by an average of 91–96%\. This highlights the practicality and effectiveness of this approach in real\-world settings\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->