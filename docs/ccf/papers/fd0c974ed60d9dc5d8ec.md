---
title: "Toward Explaining Large Language Models in Software Engineering Tasks"
authors: "Antonio Vitale, Khai-Nguyen Nguyen, Denys Poshyvanyk, Rocco Oliveto, Simone Scalabrino, Antonio Mastropaolo"
date: "2026-08-22"
source: "TOSEM"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-08-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3837084>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Recent progress in Large Language Models \(LLMs\) has substantially advanced the automation of software engineering \(SE\) tasks, enabling complex activities such as code generation and code summarization\. However, the black\-box nature of LLMs remains a major barrier to their adoption in high\-stakes and safety\-critical domains, where explainability and transparency are vital for trust, accountability, and effective human supervision\. Despite increasing interest in explainable AI for software engineering, existing methods lack domain\-specific explanations aligned with how practitioners reason about SE artifacts\. To address this gap, we introduce FeatureSHAP, the first fully automated, model\-agnostic explainability framework tailored to software engineering tasks\. Based on Shapley values, FeatureSHAP attributes model outputs to high\-level input features through systematic input perturbation and task\-specific similarity comparisons, while remaining compatible with both opensource and proprietary LLMs\. We evaluate FeatureSHAP on two bi\-modal SE tasks: code generation and code summarization\. The results show that FeatureSHAP assigns less importance to irrelevant input features and produces explanations with higher fidelity than baseline methods, at a substantially lower computational cost than token\-level alternatives\. A practitioner survey involving 37 participants shows that FeatureSHAP helps practitioners better interpret model outputs and make more informed decisions\. Collectively, FeatureSHAP represents a meaningful step toward practical explainable AI in software engineering\. FeatureSHAP is available at https://github\.com/deviserlab/FeatureSHAP\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->