---
title: "CASCADE: Detecting Inconsistencies between Code and Documentation with Automatic Test Generation"
authors: "Tobias Kiecker, Jan Arne Sparka, Martin Reuter, Albert Ziegler, Lars Grunske"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808175>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Maintaining consistency between code and documentation is a crucial yet frequently overlooked aspect of software development\. Even minor mismatches can confuse API users, introduce new bugs, and increase overall maintenance effort\. This creates demand for automated solutions that can assist developers in identifying code\-documentation inconsistencies\. However, since automatic reports still require human confirmation, false positives carry serious consequences: wasting developer time and discouraging practical adoption\. We introduce CASCADE \(Consistency Analysis for Source Code And Documentation through Execution\), a novel tool for detecting inconsistencies with a strong emphasis on reducing false positives\. CASCADE leverages Large Language Models \(LLMs\) to generate unit tests directly from natural\-language documentation\. Since these tests are derived from the documentation, any failure during execution indicates a potential mismatch between the documented and actual behavior of the code\. To minimize false positives, CASCADE also generates code from the documentation to cross\-check the generated tests\. By design, an inconsistency is reported only when two conditions are met: the existing code fails a test, while the code generated from the documentation passes the same test\. We evaluated CASCADE on a novel dataset of 71 inconsistent and 814 consistent code\-documentation pairs drawn from open\-source Java projects\. Further, we applied CASCADE to additional Java, C\#, and Rust repositories, where we uncovered 13 previously unknown inconsistencies, of which 10 have subsequently been fixed, demonstrating both CASCADE&\#x27;s precision and its applicability to real\-world codebases\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->