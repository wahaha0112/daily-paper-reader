---
title: "Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles"
authors: "Davide Molinelli, Alberto Martin-Lopez, Elliott Zackrone, Beyza Eken, Michael D. Ernst, Mauro Pezzè"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728960>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

This paper presents Tratto, a neuro\-symbolic approach that generates assertions \(boolean expressions\) that can serve as axiomatic oracles, from source code and documentation\. The symbolic module of Tratto takes advantage of the grammar of the programming language, the unit under test, and the context of the unit \(its class and available APIs\) to restrict the search space of the tokens that can be successfully used to generate valid oracles\. The neural module of Tratto uses transformers fine\-tuned for both deciding whether to output an oracle or not and selecting the next lexical token to incrementally build the oracle from the set of tokens returned by the symbolic module\. Our experiments show that Tratto outperforms the state\-of\-the\-art axiomatic oracle generation approaches, with 73% accuracy, 72% precision, and 61% F1\-score, largely higher than the best results of the symbolic and neural approaches considered in our study \(61%, 62%, and 37%, respectively\)\. Tratto can generate three times more axiomatic oracles than current symbolic approaches, while generating 10 times less false positives than GPT4 complemented with few\-shot learning and Chain\-of\-Thought prompting\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->