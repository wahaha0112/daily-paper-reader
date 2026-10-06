---
title: "An Empirical Study of False Negatives and Positives of Static Code Analyzers From the Perspective of Historical Issues"
authors: "Han Cui, Jingjing Liang, Menglei Xie, Jiahao Peng, Ting Su, Chengyu Zhang, Shin Hwei Tan"
date: "2026-09-30"
source: "TOSEM"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-09-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3849701>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Static code analyzers are widely used to help find program flaws\. However, in practice the effectiveness and usability of such analyzers is affected by the problems of false negatives \(FNs\) and false positives \(FPs\)\. This paper aims to investigate the FNs and FPs of such analyzers from a new perspective, i\.e\. , examining the historical issues of FNs and FPs of these analyzers reported by their maintainers, users and researchers in their issue repositories — each of these issues manifested as a FN or FP of these analyzers in the history and has already been confirmed and fixed by the analyzers’ developers\. To this end, we conduct the first systematic study on a broad range of 1257 historical issues of FNs/FPs from four popular rule\-based static code analyzers for Java \( i\.e\. , PMD , SpotBugs , SonarQube , and ErrorProne \)\. All these issues have been confirmed and fixed by the developers\. We investigated these issues’ root causes and the characteristics of the corresponding issue\-triggering programs\. It reveals several new interesting findings and implications on mitigating FNs and FPs\. Furthermore, guided by some findings of our study, we designed a metamorphic testing strategy to find FNs and FPs\. This strategy successfully found 15 new issues of FNs/FPs, 12 of which have been confirmed and 9 have already been fixed by the developers\. Our further manual investigation of the studied analyzers revealed one rule specification issue and additional three FNs/FPs due to the weaknesses of the implemented static analysis\. We have made all the artifacts \(datasets and tools\) publicly available at https://zenodo\.org/doi/10\.5281/zenodo\.11525129 \.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->