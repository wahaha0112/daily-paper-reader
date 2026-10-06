---
title: "Paralegal: Practical Static Analysis for Privacy Bugs"
authors: "Justus Adam, Carolyn Zech, Livia Zhu, Sreshtaa Rajesh, Nathan Harbison, Mithi Jethwa, Will Crichton, Shriram Krishnamurthi, Malte Schwarzkopf"
date: "2025"
source: "OSDI"
tags: ["query:code-analysis"]
pdf: "https://www.usenix.org/system/files/osdi25-adam.pdf"
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OSDI · CCF-A · 2025（year 精度）

[出版社 / 官方论文页面](<https://www.usenix.org/conference/osdi25/presentation/adam>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Finding privacy bugs in software today usually requires onerous manual audits\. Code analysis tools could help, but existing tools aren’t sufficiently practical and ergonomic to be used\. Paralegal is a static analysis tool to find privacy bugs in Rust programs\. Key to Paralegal’s practicality is its distribution of work between the program analyzer, privacy engineers, and application developers\. Privacy engineers express a high\-level privacy policy over markers, which application developers then apply to source code entities\. Paralegal extracts a Program Dependence Graph \(PDG\) from the program, leveraging Rust’s ownership type system to model the behavior of library code\. Paralegal augments the PDG with the developers’ markers and checks privacy policies against the marked PDG\. In an evaluation on eight real\-world applications, Paralegal found real privacy bugs, including two previously unknown ones\. Paralegal supports a broader range of policies than information flow control \(IFC\) and CodeQL, a widely\-used code analysis engine\. Paralegal is fast enough to deploy interactively, and its markers are easy to maintain as code evolves\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->