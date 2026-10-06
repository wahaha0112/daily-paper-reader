---
title: "Finding Compiler Bugs through Cross-Language Code Generator and Differential Testing"
authors: "Qiong Feng, Xiaotian Ma, Ziyuan Feng, Marat Akhin, Wei Song, Peng Liang"
date: "2025-10-09"
source: "OOPSLA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2025-10-09（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3763152>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Compilers play a central role in translating high\-level code into executable programs, making their correctness essential for ensuring code safety and reliability\. While extensive research has focused on verifying the correctness of compilers for single\-language compilation, the correctness of cross\-language compilation — which involves the interaction between two languages and their respective compilers — remains largely unexplored\. To fill this research gap, we propose CrossLangFuzzer , a novel framework that introduces a universal intermediate representation \(IR\) for JVM\-based languages and automatically generates cross\-language test programs with diverse type parameters and complex inheritance structures\. After generating the initial IR, CrossLangFuzzer applies three mutation techniques — LangShuffler, FunctionRemoval , and TypeChanger — to enhance program diversity\. By evaluating both the original and mutated programs across multiple compiler versions, CrossLangFuzzer successfully uncovered 10 confirmed bugs in the Kotlin compiler, 4 confirmed bugs in the Groovy compiler, 7 confirmed bugs in the Scala 3 compiler, 2 confirmed bugs in the Scala 2 compiler, and 1 confirmed bug in the Java compiler\. Among all mutators, TypeChanger is the most effective, detecting 11 of the 24 compiler bugs\. Furthermore, we analyze the symptoms and root causes of cross\-compilation bugs, examining the respective responsibilities of language compilers when incorrect behavior occurs during cross\-language compilation\. To the best of our knowledge, this is the first work specifically focused on identifying and diagnosing compiler bugs in cross\-language compilation scenarios\. Our research helps to understand these challenges and contributes to improving compiler correctness in multi\-language environments\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->