---
title: "Beyond Language Boundaries: Uncovering Programming Language Families for Code Language Models"
authors: "Shangbo Yun, Xiaodong Gu, Jianghong Huang, Beijun Shen"
date: "2026-06-30"
source: "FSE"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3797138>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

The rapid proliferation of diverse programming languages presents both opportunities and challenges for developing multilingual code LLMs\. While existing techniques often train code LLMs by simply aggregating multilingual code data, few explore the deeper relationships between programming languages and how such relationships can be utilized to optimize both training and inference\. In this work, we investigate two fundamental questions: \(1\) What are the deep linguistic relationships among programming languages? and \(2\) How can these relationships be leveraged to improve multilingual code LLMs? We propose an embedding\-based framework to uncover the latent families of programming languages\. Our approach begins by defining 21 primary linguistic features of programming languages, such as variable definition, control structures, and method declarations, and then employs LLMs to generate feature\-aligned code samples across multiple languages\. By embedding these semantically parallel code snippets from 19 languages, we construct a similarity matrix and perform hierarchical clustering to uncover inherent language relationships\. Our analysis reveals clear hierarchical structures among programming languages\. Closely related languages form well\-defined clusters \(e\.g\., C, C\+\+, Java, and Swift group together\), while Go exhibits as a “lingua franca” with the highest cross\-language similarity\. Building on the uncovered language families, we propose three strategies to enhance multilingual LLM training: transfer learning across linguistically related languages, linguistic proximity\-guided curriculum learning, and centroid\-based intermediary code translation\. Experiments on four code intelligence tasks demonstrate that our methods significantly improve multilingual LLM performance\. This work offers a universal perspective on programming languages and advances more effective strategies for multilingual code LLM training\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->