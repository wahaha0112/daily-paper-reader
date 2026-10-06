---
title: "MetaRCA: A Generalizable Root Cause Analysis Framework for Cloud-Native Systems Powered by Meta Causal Knowledge"
authors: "Shuai Liang, Pengfei Chen, Bozhe Tian, Gou Tan, Maohong Xu, Youjun Qu, Yahui Zhao, Yiduo Shang, Chongkang Tan"
date: "2026-06-30"
source: "FSE"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3797069>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

The dynamics and complexity of cloud\-native systems present significant challenges for Root Cause Analysis \(RCA\)\. While causality\-based RCA methods have shown significant progress in recent years, their practical adoption is fundamentally limited by three intertwined challenges: poor scalability against system complexity, brittle generalization across different system topologies, and inadequate integration of domain knowledge\. These limitations create a vicious cycle, hindering the development of robust and efficient RCA solutions\. This paper introduces MetaRCA, a generalizable RCA framework for cloud\-native systems\. MetaRCA first constructs a Meta Causal Graph \(MCG\) offline, a reusable knowledge base defined at the metadata level\. To build the MCG, we propose an evidence\-driven algorithm that systematically fuses knowledge from Large Language Models \(LLMs\), historical fault reports, and observability data\. When a fault occurs, MetaRCA performs a lightweight online inference by dynamically instantiating the MCG into a localized graph based on the current context, and then leverages real\-time data to weight and prune causal links for precise root cause localization\. Evaluated on 252 public and 59 production failures, MetaRCA demonstrates state\-of\-the\-art performance\. It surpasses the strongest baseline by 29 percentage points in service\-level and 48 percentage points in metric\-level accuracy\. This performance advantage widens as system complexity increases, with its overhead scaling near\-linearly\. Crucially, MetaRCA shows robust cross\-system generalization, maintaining over 80% accuracy across diverse systems\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->