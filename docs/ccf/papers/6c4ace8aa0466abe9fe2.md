---
title: "SmartShot: Hunt Hidden Vulnerabilities in Smart Contracts using Mutable Snapshots"
authors: "Ruichao Liang, Jing Chen, Ruochen Cao, Kun He, Ruiying Du, Shuhua Li, Zheng Lin, Cong Wu"
date: "2025-06-19"
source: "FSE"
tags: ["query:code-vuln", "query:code-analysis", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2025-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3715714>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Smart contracts, as Turing\-complete programs managing billions of assets in decentralized finance, are prime targets for attackers\. While fuzz testing seems effective for detecting vulnerabilities in these programs, we identify several significant challenges when targeting smart contracts: \(i\) the stateful nature of these contracts requires stateful exploration, but current fuzzers rely on transaction sequences to manipulate contract states, making the process inefficient; \(ii\) contract execution is influenced by the continuously changing blockchain environment, yet current fuzzers are limited to local deployments, failing to test contracts in real\-world scenarios\. These challenges hinder current fuzzers from uncovering hidden vulnerabilities, i\.e\., those concealed in deep contract states and specific blockchain environments\. In this paper, we present S mart S hot , a mutable snapshot\-based fuzzer to hunt hidden vulnerabilities within smart contracts\. We innovatively formulate contract states and blockchain environments as directly fuzzable elements and design mutable snapshots to quickly restore and mutate these elements\. S mart S hot features a symbolic taint analysis\-based mutation strategy along with double validation to soundly guide the state mutation\. S mart S hot mutates blockchain environments using contract’s historical on\-chain states, providing real\-world execution contexts\. We propose a snapshot checkpoint mechanism to integrate mutable snapshots into S mart S hot ’s fuzzing loops\. These innovations enable S mart S hot to effectively fuzz contract states, test contracts across varied and realistic blockchain environments, and support on\-chain fuzzing\. Experimental results show that S mart S hot is effective to detect hidden vulnerabilities with the highest code coverage and lowest false positive rate\. S mart S hot is 4\.8× to 20\.2× faster than state\-of\-the\-art tools, identifying 2,150 vulnerable contracts out of 42,738 real\-world contracts which is 2\.1× to 13\.7× more than other tools\. S mart S hot has demonstrated its real\-world impact by detecting vulnerabilities that are only discoverable on\-chain and uncovering 24 0\-day vulnerabilities in the latest 10,000 deployed contracts\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->