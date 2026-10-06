---
title: "Floating-Point Usage on GitHub: A Large-Scale Study of Statically Typed Languages"
authors: "Andrea Gilot, Tobias Wrigstad, Eva Darulova"
date: "2026-04-10"
source: "OOPSLA"
tags: ["query:code-vuln"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2026-04-10（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3798203>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Reasoning about floating\-point arithmetic is notoriously hard\. While static and dynamic analysis techniques or program repair have made significant progress, more work is still needed to make them relevant to real\-world code\. On the critical path to that goal is understanding what real\-world floating\-point code looks like\. To close that knowledge gap, this paper presents the first large\-scale empirical study of floating\-point arithmetic usage across public GitHub repositories\. We focus on statically typed languages to allow our study to scale to millions of repositories\. We follow state\-of the art mining practices including random sampling and filtering based on only intrinsic properties to avoid bias, and identify floating\-point usage by searching for keywords in the source code, and programming language constructs \( e\.g \., loops\) by parsing the code\. Our evaluation supports the claim often made in papers that floating\-point arithmetic is widely used\. Comparing statistics such as size and usage of certain constructs and functions, we find that benchmarks used in literature to evaluate automated reasoning techniques for floating\-point arithmetic are in certain aspects representative of ‘real\-world’ code, but not in all\. We publish a dataset of 10 million real\-world floating\-point functions extracted from our study\. We demonstrate in a case study how it may be used to identify new floating\-point benchmarks and help future techniques for floating\-point arithmetic to be designed and evaluated to match actual users’ expectations\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->