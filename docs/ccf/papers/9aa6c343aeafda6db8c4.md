---
title: "Detecting Code-Comment Inconsistencies in Smart Contracts by Combining LLM and Program Analysis"
authors: "Jiashuo Zhang, Jiachi Chen, Ting Zhang, Yue Li, Daoyuan Wu, Yanlin Wang, Jianbo Gao, Ting Chen, Zhong Chen"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-analysis", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808112>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Smart contracts have attracted rapid development and widespread application\. Due to the complexity of real\-world smart contracts, it is error\-prone to correctly enforce all intended functionalities in code implementations, resulting in unintended functional behaviors and security issues in practice\. Code\-comment inconsistency detection has emerged as an important solution to these issues, which leverages the redundant functional specifications in comments to detect code implementations that violate developers&\#x27; intentions\. However, existing inconsistency detection solutions are typically pattern\-based and limited to fixed types of inconsistencies, which prevents them from detecting the diverse inconsistencies between real\-world code implementations and casually written comments\. To bridge the gap, this paper presents SmartComment, the first technique that combines LLMs with program analysis techniques for detecting code\-comment inconsistencies in smart contracts\. SmartComment introduces an LLM\-driven workflow which simulates real\-world interactions between code reviewers and developers to identify inconsistencies\. It incorporates various program analysis techniques into the workflow, including comment propagation and code context extraction for generating input context for inconsistency detection, as well as program variant generation and differential analysis for inconsistency confirmation\. Our evaluation results show that SmartComment detects 203 valid inconsistencies from a dataset of 1,000 real\-world contracts with a precision of 79\.9%, highlighting its effectiveness in detecting prevalent and diverse real\-world inconsistencies\. Compared to previous work, SmartComment achieves both higher precision and recall, detecting over 90% of inconsistencies that existing methods fail to identify\. Furthermore, an ablation experiment demonstrates the effectiveness of incorporating program analysis techniques into SmartComment, improving the F1\-score from 58\.7% to 81\.3%\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->