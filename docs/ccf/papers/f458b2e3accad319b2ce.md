---
title: "From Stochastic to Semantic: Advanced Attribute-Guided Compiler Testing"
authors: "Jiangchang Wu, Yibiao Yang, Maolin Sun, Qingyang Li, Kang Chen, Lei Xu, Yuming Zhou"
date: "2026-09-17"
source: "TOSEM"
tags: ["query:code-vuln"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-09-17（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3793554>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Compiler testing is critically important, as compilers serve as the foundational infrastructure in system software development\. A comprehensive exploration of the compilation space is essential for uncovering bugs in compilers\. Existing methods primarily involve the utilization of various compilation options alongside test programs as inputs for stress\-testing compilers\. However, these compilation options are typically applied uniformly across all program elements—such as functions and variables, by default, limiting the ability to thoroughly explore the compilation space\. In programming languages like C and C\+\+, attributes such as the \_\_attribute\_\_\(\(always\_inline\)\) directive provide a mechanism for programmers to specify additional information for specific code elements to the compiler\. These attributes allow for precise control over the compilation process, such as enforcing constraints and customizing optimization passes for particular elements\. This flexibility in specifying attributes offers opportunities to investigate previously unexamined areas within compilers\. Unfortunately, few studies have leveraged attributes for compiler testing\. To this end, we propose Atlas , an attribute\-guided approach that strategically inserts attributes into test programs to facilitate a more thorough exploration of the compilation space\. Our key insight is that attributes specified for individual program elements can provide a more flexible means of exploring the compilation space\. Our extensive experiments on GCC and LLVM demonstrate the superiority of Atlas over baseline testing techniques that do not employ attributes, particularly in terms of bug detection and code coverage\. Furthermore, Atlas has led to the discovery of 97 unique bugs in GCC and LLVM, 73 of which have already been confirmed or fixed, showcasing its practical utility\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->