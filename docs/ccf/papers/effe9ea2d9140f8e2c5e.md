---
title: "Detecting Smart Contract State-Inconsistency Bugs via Flow Divergence and Multiplex Symbolic Execution"
authors: "Yinxi Liu, Wei Meng, Yinqian Zhang"
date: "2025-06-19"
source: "FSE"
tags: ["query:code-vuln", "query:code-analysis", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2025-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3715712>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Ethereum smart contracts determine state transition results not only by the previous states, but also by a mutable global state consisting of storage variables\. This has resulted in state\-inconsistency bugs, which grant an attacker the ability to modify contract states either through recursive function calls to a contract \(reentrancy\), or by exploiting transaction order dependence \(TOD\)\. Current studies have determined that identifying data races on global storage variables can capture all state\-inconsistency bugs\. Nevertheless, eliminating false positives poses a significant challenge, given the extensive number of execution paths that could potentially cause a data race\. For simplicity, existing research considers a data race to be vulnerable as long as the variable involved could have inconsistent values under different execution orders \. However, such a data race could be benign when the inconsistent value does not affect any critical computation or decision\-making process in the program\. Besides, the data race could also be infeasible when there is no valid state in the contract that allows the execution of both orders\. In this paper, we aim to appreciably reduce these false positives without introducing false negatives\. We present DivertScan , a precise framework to detect exploitable state\-inconsistency bugs in smart contracts\. We first introduce the use of flow divergence to check where the involved variable may flow to\. This allows DivertScan to precisely infer the potential effects of a data race and determine whether it can be exploited for inducing unexpected program behaviors\. We also propose multiplex symbolic execution to examine different execution orders in one time of solving\. This helps DivertScan to determine whether a common starting state could potentially exist\. To address the scalability issue in symbolic execution, DivertScan utilizes an overapproximated pre\-checking and a selective exploration strategy\. As a result, it only needs to explore a limited state space\. DivertScan significantly outperformed state\-of\-the\-art tools by improving the precision rate by 20\.72% to 74\.93% while introducing no false negatives\. It also identified five exploitable real\-world vulnerabilities that other tools missed\. The detected vulnerabilities could potentially lead to a loss of up to $68\.2M, based on trading records and rate limits\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->