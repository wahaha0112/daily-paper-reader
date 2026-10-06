---
title: "Extraction and Mutation at a High Level: Template-Based Fuzzing for JavaScript Engines"
authors: "Wai Kin Wong, Dongwei Xiao, Cheuk Tung Lai, Yiteng Peng, Daoyuan Wu, Shuai Wang"
date: "2025-10-09"
source: "OOPSLA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2025-10-09（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3763154>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

JavaScript \(JS\) engines implement complex language semantics and optimization strategies to support the dynamic nature of JS, making them difficult to test thoroughly and prone to subtle, security\-critical bugs\. Existing fuzzers often struggle to generate diverse and valid test cases\. They either rely on syntax\-level mutations that lack semantic awareness or perform limited, local mutations on concrete code, thus failing to explore deeper, more complex program behaviors\. This paper presents TemuJs , a novel fuzzing framework that performs extraction and mutation at a high level, operating on abstract templates derived from real\-world JS programs\. These templates capture coarse\-grained program structures with semantic placeholders, enabling semantics\-aware mutations that preserve the high\-level intent of the original code while diversifying its behavior\. By decoupling mutation from concrete syntax and leveraging a structured intermediate representation for the templates, TemuJs explores a broader and more meaningful space of program behaviors\. Evaluated on three major JS engines, namely, V8, SpiderMonkey, and JavaScriptCore, TemuJs discovers 44 bugs and achieves a 10\.3% relative increase in edge coverage compared to state\-of\-the\-art fuzzers on average\. Our results demonstrate the efficacy of high\-level, template\-mutation fuzzing in testing JS engines\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->