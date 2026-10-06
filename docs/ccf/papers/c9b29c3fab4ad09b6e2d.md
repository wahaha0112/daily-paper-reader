---
title: "Assessing and Improving Prompting Large Language Models for Software Vulnerability Analysis"
authors: "Yu Nong, Guangbei Yi, Mohammed Aldeen, Long Cheng, Hongxin Hu, Haipeng Cai"
date: "2026-06-19"
source: "TOSEM"
tags: ["query:code-vuln", "query:skill"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3821416>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Large language models \(LLMs\) have demonstrated potential in diverse domains including software analysis\. Yet there is a lack of systematic assessment of how LLMs perform in comparison to various extant approaches, and how LLMs may be improved , for software vulnerability analysis, via prompt engineering\. In this paper, we present a comprehensive, large\-scale empirical study of ten LLMs with seven prompting strategies versus nine traditional \(five code\-analysis\- and four deep\-learning\-based\) techniques on three vulnerability analysis tasks \(detection, classification, and repair\) against five real\-world datasets \(8,000\+ C/C\+\+ samples, including a zero\-day dataset\)\. We show that, with existing prompting strategies, LLMs often struggle with practical vulnerability analysis and underperform the traditional approaches\. Via in\-depth case analysis, we reveal that the evaluated LLMs frequently suffer from incorrect reasoning\. Based on these findings, we improve the prompting with a vulnerability\-specific adaptation of chain\-of\-thought \(CoT\), named Vulnerability\-Semantics\-guided Prompting \(VSP\)\. Our results show that VSP improves the performance of some of the LLMs in certain configurations across the three tasks\. VSP also helps mitigate the reasoning limitations for some of the evaluated LLMs\. For vulnerability detection on unseen data, improvements are limited or marginal for some models\. We further identify seven common challenges that led to the LLMs’ incorrect answers in these tasks and provide actionable recommendations to help mitigate them\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->