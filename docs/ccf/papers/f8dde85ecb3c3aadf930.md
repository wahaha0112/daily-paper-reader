---
title: "Enhancing Smart Contract Security Analysis with Execution Property Graphs"
authors: "Kaihua Qin, Zhe Ye, Zhun Wang, Weilin Li, Liyi Zhou, Chao Zhang, Dawn Song, Arthur Gervais"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:code-vuln", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728924>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Smart contract vulnerabilities have led to significant financial losses, with their increasing complexity rendering outright prevention of hacks increasingly challenging\. This trend highlights the crucial need for advanced forensic analysis and real\-time intrusion detection, where dynamic analysis plays a key role in dissecting smart contract executions\. Therefore, there is a pressing need for a unified and generic representation of smart contract executions, complemented by an efficient methodology that enables the modeling and identification of a broad spectrum of emerging attacks We introduce C lue , a dynamic analysis framework specifically designed for the Ethereum virtual machine\. Central to C lue is its ability to capture critical runtime information during contract executions, employing a novel graph\-based representation, the Execution Property Graph\. A key feature of C lue is its innovative graph traversal technique, which is adept at detecting complex attacks, including \(read\-only\) reentrancy and price manipulation\. Evaluation results reveal C lue ’s superior performance with high true positive rates and low false positive rates, outperforming state\-of\-the\-art tools\. Furthermore, C lue ’s efficiency positions it as a valuable tool for both forensic analysis and real\-time intrusion detection\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->