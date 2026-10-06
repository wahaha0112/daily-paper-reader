---
title: "DamFlow: Preventing a Flood of Irrelevant Data Flows in Android Apps"
authors: "Marco Alecci, Jordan Samhi, Marc Miltenberger, Steven Arzt, Tegawendé F. Bissyandé, Jacques Klein"
date: "2026-07-11"
source: "TOSEM"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-07-11（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3772002>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

State\-of\-the\-art tools like FlowDroid have been proposed to detect data leaks in Android apps, but two main challenges persist: ① false alarms and ② undetected data leaks\. One contributing factor to these challenges is that a tool such as FlowDroid relies on pre\-defined lists of privacy\-sensitive source and sink API methods\. Generating such lists is complex; incomplete or inaccurate lists result in both false alarms \(i\.e\., irrelevant data flows\) and undetected data leaks\. Additionally, data leaks are highly context\-dependent\. For instance, GPS data flowing from a navigation app is expected, but the same flow in a calculator app is suspicious\. Even when FlowDroid identifies a source\-to\-sink path, it may not be relevant to privacy analysis, further increasing false alarms\. To tackle these issues, we propose a novel approach named DamFlow, which, by combining backward taint analysis with context\-aware anomaly detection, prevents a “flood” of irrelevant data flows while at the same time finding data leaks missed by existing approaches\. Our evaluation demonstrates that DamFlow significantly reduces reported leaks per app while uncovering previously undetected leaks, enhancing FlowDroid’s practicality for real\-world data leak detection\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->