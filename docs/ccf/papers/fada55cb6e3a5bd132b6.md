---
title: "U-Turn: Enhancing Incorrectness Analysis by Reversing Direction"
authors: "Flavio Ascari, Roberto Bruni, Roberta Gori, Azalea Raad"
date: "2026-01-08"
source: "POPL"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：POPL · CCF-A · 2026-01-08（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3776688>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

O’Hearn’s Incorrectness Logic \(IL\) has sparked renewed interest in static analyses that aim to detect program errors rather than prove their absence, thereby avoiding false alarms—a critical factor for practical adoption in industrial settings\. As new incorrectness logics emerge to capture diverse error\-related properties, a key question arises: can combining correctness and incorrectness techniques enhance precision, expressiveness, automation, or scalability? Notable frameworks, such as outcome logic, UNTer, local completeness logic, and exact separation logic, unify multiple analyses within a single proof system\. In this work, we adopt a complementary strategy\. Rather than designing a unified logic, we combine IL, which identifies reachable error states, with Sufficient Incorrectness Logic \(SIL\), which finds input states potentially leading to those errors\. As a result, we get a more informative and effective analysis than either logic in isolation\. Rather than sequencing them, our key innovation is reusing heuristic choices from the first analysis to steer the second\. In fact, both IL and SIL rely on under\-approximation and thus their automation legitimizes heuristics that avoid exhaustive path enumeration \(e\.g\., selective disjunct pruning, loop unrolling\)\. Concretely, we instrument the proof rules of the second logic with derivations from the first to inductively guide rule selection and application\. To our knowledge, this is the first rule format enabling such inter\-analysis instrumentation\. This combined analysis aids debugging and testing by revealing both reachable errors and their causes, and opens new avenues for embedding incorrectness insights into scalable, expressive, automated code contracts\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->