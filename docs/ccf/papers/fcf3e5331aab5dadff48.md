---
title: "Identifying Multi-parameter Constraint Errors in Python Data Science Library API Documentation"
authors: "Xiufeng Xu, Fuman Xie, Chenguang Zhu, Guangdong Bai, Sarfraz Khurshid, Yi Li"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728945>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Modern AI\- and Data\-intensive software systems rely heavily on data science and machine learning libraries that provide essential algorithmic implementations and computational frameworks\. These libraries expose complex APIs whose correct usage has to follow constraints among multiple interdependent parameters\. Developers using these APIs are expected to learn about the constraints through the provided documentation and any discrepancy may lead to unexpected behaviors\. However, maintaining correct and consistent multiparameter constraints in API documentation remains a significant challenge for API compatibility and reliability\. To address this challenge, we propose MP Checker for detecting inconsistencies between code and documentation, specifically focusing on multi\-parameter constraints\. MP Checker identifies these constraints at the code level by exploring execution paths through symbolic execution and further extracts corresponding constraints from documentation using large language models \(LLMs\)\. We propose a customized fuzzy constraint logic to reconcile the unpredictability of LLM outputs and detect logical inconsistencies between the code and documentation constraints\. We collected and constructed two datasets from four popular data science libraries and evaluated MP Checker on them\. Our tool identified 117 of 126 inconsistent constraints, achieving a recall of 92\.8% and demonstrating its effectiveness at detecting inconsistency issues\. We further reported 14 detected inconsistency issues to the library developers, who have confirmed 11 issues at the time of writing\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->