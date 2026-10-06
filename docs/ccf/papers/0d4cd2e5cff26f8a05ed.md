---
title: "The Fix Is Right at Hand: Fixing Incompatibility Errors Guided by Library Knowledge for Automatic Library Upgrade"
authors: "Zhuotong Zhou, Susheng Wu, Junpeng Zhao, Bihuan Chen, YenQin Hoo, Yiheng Huang, Yiheng Cao, Xin Peng"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:supply-chain"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832116>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Third\-party libraries \(TPLs\) play critical roles in modern software development\. Upgrading them is crucial for enhanced security and functionality, but often introduces incompatibility errors, caused by breaking changes in library APIs, in client code\. Existing approaches rely on predefined migration patterns or API recommendation heuristics, which suffer from limited pattern coverage and ignore the usage context of broken API, leading to incorrect or incomplete fixes\. To address these limitations, we propose Librarian, a novel LLM\-based approach to automatically fix incompatibility errors when upgrading a dependent library in a client project\. The core idea of Librarian is to extract context\-aware fix hints from the library codebase, serving as semantic few\-shot examples, enabling LLM to generate fixes without relying on predefined patterns\. Since LLM may generate an incorrect or incomplete fix, Librarian performs fix refinement based on compilation feedback from the client project\. Our evaluation has demonstrated that Librarian achieves a fixing success rate of 84\.2%, outperforming the state\-of\-the\-arts by at least 45\.3%\. Our evaluation has also indicated the practical usefulness of Librarian in fixing incompatibility errors in 32 real\-world projects\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->