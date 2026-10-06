---
title: "Encode the ∀∃ Relational Hoare Logic into Standard Hoare Logic"
authors: "Shushu Wu, Xiwei Wu, Qinxiang Cao"
date: "2025-10-09"
source: "OOPSLA"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2025-10-09（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3763138>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Verifying a real\-world program’s functional correctness can be decomposed into \(1\) a refinement proof showing that the program implements a more abstract high\-level program and \(2\) an algorithm correctness proof at the high level\. Relational Hoare logic serves as a powerful tool to establish refinement but often necessitates formalization beyond standard Hoare logic\. Particularly in the nondeterministic setting, the ∀∃ relational Hoare logic is required\. Existing approaches encode this logic into a Hoare logic with ghost states and invariants, yet these extensions significantly increase formalization complexity and soundness proof overhead\. This paper proposes a generic encoding theory that reduces the ∀∃ relational Hoare logic to standard \(unary\) Hoare logic\. Precisely, we propose to redefine the validity of relational Hoare triples while preserving the original proof rules and then encapsulate the ∀∃ pattern within assertions\. We have proved that the validity of encoded standard Hoare triples is equivalent to the validity of the desired relational Hoare triples\. Moreover, the encoding theory demonstrates how common relational Hoare logic proof rules are indeed special cases of standard Hoare logic proof rules, and relational proof steps correspond to standard proof steps\. Our theory enables standard Hoare logic to prove ∀∃ relational properties by defining a predicate Exec , without requiring modifications to the logic framework or re\-verification of soundness\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->