---
title: "AlphaTrans: A Neuro-Symbolic Compositional Approach for Repository-Level Code Translation and Validation"
authors: "Ali Reza Ibrahimzada, Kaiyao Ke, Mrigank Pawagi, Muhammad Salman Abid, Rangeet Pan, Saurabh Sinha, Reyhaneh Jabbarvand"
date: "2025-06-19"
source: "FSE"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2025-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3729379>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Code translation transforms programs from one programming language \(PL\) to another\. One prominent use case is application modernization to enhance maintainability and reliability\. Several rule\-based transpilers have been designed to automate code translation between different pairs of PLs\. However, the rules can become obsolete as the PLs evolve and cannot generalize to other PLs\. Recent studies have explored the automation of code translation using Large Language Models \(LLMs\)\. One key observation is that such techniques may work well for crafted benchmarks but fail to generalize to the scale and complexity of real\-world projects with inter\- and intra\-class dependencies, custom types, PL\-specific features, etc\. We propose AlphaTrans , a neuro\-symbolic approach to automate repository\-level code translation\. AlphaTrans translates both source and test code, and employs multiple levels of validation to ensure the translation preserves the functionality of the source program\. To break down the problem for LLMs, AlphaTrans leverages program analysis to decompose the program into fragments and translates them in the reverse call order \. We leveraged AlphaTrans to translate ten real\-world open\-source projects consisting of ⟨836, 8575, 2719⟩ \(application and test\) classes, \(application and test\) methods, and unit tests\. AlphaTrans breaks down these projects into 17874 fragments and translates the entire repository\. 96\.40 % of the translated fragments are syntactically correct, and AlphaTrans validates the translations’ runtime behavior and functional correctness for 27\.03 % and 25\.14 % of the application method fragments\. On average, integrated translation and validation takes 34 hours \(min=3, max=121\) to translate a project, showing its scalability in practice\. For the syntactically or semantically incorrect translations, AlphaTrans generates a report including existing translation, stack trace, test errors, or assertion failures\. We provided these artifacts to two developers to fix the translation bugs in four projects\. They fixed the issues in 20\.1 hours on average \(5\.5 hours for the smallest and 34 hours for the largest project\) and achieved all passing tests\. Without AlphaTrans , translating and validating such big projects could take weeks, if not months\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->