---
title: "Validating LLM-Generated SQL Queries through Metamorphic Prompting"
authors: "Li Lin, Qinglin Zhu, Jintai Hong, Chong Wang, Yang Liu, Rongxin Wu"
date: "2026-06-30"
source: "FSE"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3797146>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Large Language Models \(LLMs\) can translate natural language \(NL\) into SQL, enabling non\-experts to query databases via conversational interfaces\. However, the generated SQL often contains intent\-violating hallucinations —queries that are syntactically valid and executable, yet semantically misaligned with the user’s question\. These failures are especially risky in real\-world settings where users cannot verify the correctness\. In this paper, we propose MRSQLGen, a framework for detecting intent\-violating hallucinations, built on the metamorphic prompting paradigm\. MRSQLGen rewrites the input prompt using task\-specific transformation rules derived from a hallucination taxonomy, and validates the generated SQL by checking behavioral consistency across multiple executions\. Each transformation is associated with a metamorphic relationship \(MR\) that defines the expected relation between results; discrepancies are aggregated through a majority\-vote strategy to robustly flag hallucinations without ground\-truth SQL\. We evaluate MRSQLGen on two benchmarks \(Spider and Bird\) using five representative LLMs, including GPT\-4o\. Experimental results demonstrate that MRSQLGen consistently outperforms state\-of\-the\-art hallucination detection techniques, achieving higher precision and recall in detecting hallucinated SQL queries\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->