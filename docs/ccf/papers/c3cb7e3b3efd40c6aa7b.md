---
title: "Node-Centric Systematic Testing for Distributed Systems"
authors: "Yu Liang, Yu Gao, Wensheng Dou, Wenhan Feng, Zheng Qin, Zhen Tang, Hui Li, Wei Wang, Jun Wei"
date: "2026-07-17"
source: "TOSEM"
tags: ["query:code-vuln"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-07-17（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3831368>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Distributed systems consist of multiple independent nodes that communicate over a network\. Existing testing approaches typically treat a distributed system as a whole and explore nondeterministic event interleavings to uncover bugs\. However, the exponential growth of node state combinations severely limits scalability, making exhaustive testing impractical\. We observe that systematically testing individual node behaviors is sufficient to cover overall system behaviors, while avoiding the combinatorial explosion caused by states irrelevant to the executing node\. Motivated by this insight, we propose node\-centric equivalence , which is orthogonal to existing independence and symmetry equivalences, to identify equivalent state transitions\. We first identify node\-centric equivalence groups among state transitions according to their projected node\-centric behaviors, and then systematically explore each node&\#x27;s unique behaviors without traversing the full interleaving space of distributed systems, while preserving bug detection capability\. Based on node\-centric equivalence, we develop a testing tool, NodeExplore and evaluate NodeExplore on five real\-world distributed systems\. The results show that NodeExplore detects bugs up to 27 \\\(\\times\\\) faster, reduces test execution time by over 98%, and uncovers 11 new bugs, demonstrating its efficiency and practicality\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->