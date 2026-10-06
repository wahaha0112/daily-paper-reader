---
title: "Decomposing Ponzi Schemes: Multi-aspect Lifecycle Analysis for Detecting Fraudulent Smart Contracts"
authors: "Yizhou Chen, Zeyu Sun, Guoqing Wang, Dan Hao"
date: "2026-09-30"
source: "TOSEM"
tags: ["query:code-analysis", "query:skill", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-09-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3830472>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Smart contracts have enabled decentralized financial applications, enabling trustless and transparent asset management\. However, their programmability also expands the attack surface, allowing adversaries to encode fraudulent economic behaviors directly into contract logic\. Among these threats, Smart Contract Ponzi Schemes \(SCPS\) represent a particularly harmful class of on\-chain financial fraud, in which malicious developers mimic legitimate decentralized finance applications to extract unlawful value from users\. Existing detection approaches using static analysis or deep learning often fail to capture SCPC\-specific behaviors, while LLMs suffer from hallucinations and lack supervision\. To address these limitations, we propose PonziLicle, a novel framework that enhances SCPC detection by systematically modeling the lifecycle behaviors of Ponzi schemes\. Specifically, we analyze the typical life cycle of SCPCs and identify five behavioral perspectives that are closely tied to their structure: fund flow, profit logic, referral mechanism, withdrawal control, and camouflaged naming\. For each perspective, we design tailored prompts and utilize LLMs to generate fine\-grained, perspective\-specific code explanations\. To mitigate hallucinations, we employ static analysis to extract reliable, contract\-level signals aligned with these perspectives, which are then used to calibrate and refine the LLM\-generated explanations\. Finally, we integrate the smart contract source code, static signals, and calibrated explanations to train a deep learning classifier for SCPC detection\. Experimental results on 6,946 real\-world smart contracts show that PonziLicle outperforms 7 state\-of\-the\-art SCPC detection methods, achieving an F1\-score of 0\.958, with an increase of 10\.26% to 122\.31%\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->