---
title: "Refined² Environment Classifiers"
authors: "Yuito Murase, Atsushi Igarashi"
date: "2026-10-01"
source: "OOPSLA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3839493>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

MetaML\-style multi\-stage programming \(MSP\) supports quasi\-quotation\-based code generation, runtime execution of generated code, and cross\-stage persistence \(CSP\)\. However, its interaction with computational effects is subtle: mutable state can cause scope extrusion, where generated code escapes the scope of variables on which it depends\. This paper presents a type system for MetaML\-style MSP with mutable state that statically rules out harmful scope extrusion while supporting multi\-level code generation, runtime execution, and a variant of CSP\. Our system builds on refined environment classifiers \(RECs\), a discipline that annotates code types with the variable scopes on which generated code depends\. To scale RECs to the MetaML\-style setting, we refine classifiers so that they track not only variable scopes, but also the scopes of classifiers themselves\. Further, we integrated polymorphism over classifiers, enabling more general and reusable code generation patterns in a multi\-level setting\. For the resulting system, we define an operational semantics via a definitional interpreter and prove type soundness and safety of offline code generation, showing that generated code can be extracted as standalone well\-typed programs\. We provide working implementations and mechanized proofs in Rocq\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->