---
title: "Recurrence Sets for Proving Fair Non-termination under Axiomatic Memory Consistency Models"
authors: "Thomas Haas, Roland Meyer, Hernán Ponce de León, Andrés Lomelí Garduño"
date: "2026-01-08"
source: "POPL"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：POPL · CCF-A · 2026-01-08（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3776687>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Recurrence sets characterize non\-termination in sequential programs\. We present a generalization of recurrence sets to concurrent programs that run on weak memory models\. Sequential programs have operational semantics in terms of states and transitions, and classical recurrence sets are defined as sets of states that are existentially closed under transitions\. Concurrent programs have axiomatic semantics in terms of executions, and our new recurrence sets are defined as sets of executions that are existentially closed under extensions\. The semantics of concurrent programs is not only affected by the memory model, but also by fairness assumptions about its environment, be it the scheduler or the memory subsystems\. Our new recurrence sets are formulated relative to such fairness assumptions\. We show that our recurrence sets are sound for proving fair non\-termination on all practical memory models, and even complete on many\. To turn our theory into practice, we develop a new automated technique for proving fair non\-termination in concurrent programs on weak memory models\. At the heart of this technique is a finite representation of recurrence sets in terms of execution\-based lassos\. We implemented a lasso\-finding algorithm in Dartagnan, and evaluated it on a number of programs running under CPU and GPU memory models\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->