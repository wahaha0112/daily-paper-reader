---
title: "LLMGuard : Safeguarding Real-Time Inference for Large Language Models on Edge Devices"
authors: "Yu Sun, Gaojian Xiong, Jianhua Liu, Ziqi Zhang, Jian Cui"
date: "2026-09-16"
source: "TOSEM"
tags: ["query:skill"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-09-16（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3799230>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

TEE\-shielded secure inference offers an efficient solution to protect valuable edge\-deployed models from potential thefts\. Nevertheless, existing methods are lack of theoretical security analysis, failing to achieve the optimal security\. Furthermore, while feasible for small models, existing methods are excessively heavyweight for Large Language Models \(LLM\)\. For LLaMA\-7B, they introduce GB\-level secure memory requirement and hundredfold inference latency, severely compromising real\-time utility\. To solve these problems, we first present a Bayesian theory framework of Model Stealing \(MS\) attacks, which decomposes MS into prior and posterior knowledge leakage\. Based on this framework, LLMGuard is proposed, which presents two components: First, Intrinsic Parameters Shielding is designed to shield all private parameters, preventing prior knowledge leakage\. This approach significantly decreases the secure memory usage and achieves inference speedup\. Second, since OTP is not applicable to LLMs, Random Slices Composition is developed to obfuscate intermediate distributions with no computational overhead, minimizing posterior knowledge leakage efficiently\. Experimental results demonstrate that LLMGuard downgrades model to black\-box inference with negligible accuracy loss, while delivering \\\(43\\times\\\) inference speedup on LLaMA compared to fully shielded methods\. The proposed LLMGuard effectively addresses concerns related to intellectual property theft on edge, boosting the secure deployment of LLMs on untrusted devices\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->