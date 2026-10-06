---
title: "Towards More Realistic Assertion Generation under Mixed-Assertion Scenario"
authors: "Hongyan Li, Kunpeng E, Weifeng Sun, Quanjun Zhang, Meng Yan"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-vuln"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832214>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Unit testing is essential for software quality assurance, where a test case typically consists of a test prefix and an oracle, expressed as assertions\. In practice, crafting high\-quality assertions is non\-trivial and time\-consuming, as it requires developers to reason carefully about program states and expected behaviors\. While recent advances in Large Language Models \(LLMs\) have shown promise for automating assertion generation \(AG\), current AG methods often rely on two unrealistic assumptions: \(1\) the Single\-Assertion Formulation \(A1\), which assumes tests contain only one assertion, and \(2\) the Known\-Position Formulation \(A2\), which treats AG as a &quot;fill\-in\-the\-blanks&quot; task with pre\-defined insertion points\. Despite being widely adopted, the realism and implications of these assumptions have not been systematically examined\. This paper revisits AG under a realistic Mixed\-Assertion Scenario, where tests may contain one or multiple assertions and insertion positions are unavailable at inference time\. To examine A1, we first conduct a large\-scale empirical study of 358,117 developer\-written tests from 7,061 projects\. The results show that multi\-assertion tests are prevalent, accounting for 40\.32% of all tests and appearing in 92\.87% of projects\. Through manual analysis, we derive a taxonomy comprising ten fine\-grained assertion patterns, showing that assertions in multi\-assertion tests are rarely independent checks \(4\.69%\) and instead coordinate to validate a unified test objective\. To examine A2, we remove ground\-truth insertion cues and observe substantial performance degradation, with Exact Match dropping by 11\.80%\-\-23\.18% overall\. This suggests that position cues affect not only where assertions are placed, but also the quality of what to assert\. Motivated by these findings, we propose DA\-AG, a two\-stage framework designed for the realistic Mixed\-Assertion Scenario with unknown insertion positions\. In the first stage, it predicts assertion insertion positions to construct an assertion skeleton with explicit insertion cues\. In the second stage, it generates assertion content conditioned on the resulting skeleton and retrieved exemplar assertion sequences\. Extensive experiments across 13 diverse LLMs show that DA\-AG consistently outperforms the corresponding one\-stage baselines, which directly generate the completed test from the focal method and raw test prefix\. DA\-AG improves Exact Match by 32\.24%\-\-78\.08% and CodeBLEU by 2\.80%\-\-8\.63%, increases real\-bug detection on Defects4J by 4\-\-37 exposed bugs and 5\-\-21 unique exposed bugs, and further improves other execution\-based metrics, including compilability, bug\-finding quality, and mutation scores\. Moreover, DA\-AG outperforms closed\-source LLMs evaluated in a prompt\-only setting without task\-specific fine\-tuning \(e\.g\., GPT\-4o and Claude\-3\.5\) in similarity\-based quality and real\-bug detection\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->