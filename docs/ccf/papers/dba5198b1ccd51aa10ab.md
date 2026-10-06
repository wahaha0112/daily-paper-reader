---
title: "ExplorIt : Simulation-based Fuzzing for Autonomous Driving Systems via Multi-Agent Interaction Modeling"
authors: "Bufan Gao, Zongan Huang, Jiarun Dai, Kairui Yang, Yixing Luo, Yingjie Fu, Yuan Zhang, Min Yang, Tao Xie"
date: "2026-07-28"
source: "TOSEM"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-07-28（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832778>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Fuzzing\-based simulation testing has become a fundamental technique for assessing the safety of autonomous driving systems \(ADS\)\. It operates by iteratively mutating simulation scenario configurations, scheduling scenario execution, and monitoring ADS\-involved accidents\. However, existing ADS fuzzers commonly rely on simplistic criticality metrics \(e\.g\., inter\-vehicle distance\) for prioritizing critical scenarios during fuzzing, and lack deterministic guidance about how these heuristic\-based critical scenarios should be further mutated to finally induce ADS\-responsible accidents\. Therefore, these existing fuzzers would inevitably miss truly critical driving scenarios or report various non\-ADS\-responsible accidents\. To address these limitations, our key insight hints that EGO\-to\-NPC interactions \(i\.e\., those recorded during the execution of a given scenario\) offer comprehensive spatial\-temporal information for reliable selection of critical scenarios and deterministic scenario mutation\. Following this insight, we propose ExplorIt , a simulation\-based ADS fuzzer enhanced with systematic formalization of interaction behaviors\. Specifically, ExplorIt formalizes the runtime EGO\-to\-NPC interactions through drivable area estimation\. That is, vehicles that share overlapped driving areas are considered to have interactive relationships\. Under this modeling, ExplorIt can then deterministically mutate scenarios to curate more critical interactions by making EGO and NPC head for shared drivable areas\. Extensive experiments on Apollo 8\.0 demonstrate ExplorIt ’s effectiveness, revealing 6\.7 times more unique ADS\-responsible accidents than baseline tools \(i\.e\., DriveFuzz, SAMOTA, and AutoFuzz\)\. Moreover, 83\.2% of the reported accidents are ADS\-responsible, compared to just 16\.8% with baseline tools\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->