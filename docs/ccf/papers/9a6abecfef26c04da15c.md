---
title: "Lost in Translation: Enabling Confused Deputy Attacks on EDA Software with TransFuzz"
authors: "Flavien Solt, Kaveh Razavi"
date: "2025"
source: "USENIX Security"
tags: ["query:code-vuln", "query:code-analysis"]
pdf: "https://www.usenix.org/system/files/usenixsecurity25-solt.pdf"
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：USENIX Security · CCF-A · 2025（year 精度）

[出版社 / 官方论文页面](<https://www.usenix.org/conference/usenixsecurity25/presentation/solt>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

We introduce MIRTL, a confused deputy attack on EDA software such as simulators or synthesizers\. MIRTL relies on gadgets that exploit vulnerabilities in the EDA software&\#x27;s translation of RTL to lower\-level representations\. Invisible to white\-box testing and verification methods, MIRTL gadgets harden traditional hardware trojans, enabling unprecedentedly stealthy attacks\. To discover translation bugs, our new fuzzer, called TRANSFUZZ, generates randomized RTL designs containing many operators with complex interconnections for triggering translation bugs\. The expressiveness of RTL, however, makes the construction of a golden RTL model for detecting deviations due to translation bugs challenging\. To address this, TRANSFUZZ relies on comparing signal outputs from multiple RTL simulators for detecting vulnerabilities\. TRANSFUZZ uncovers 20 translation vulnerabilities among 31 new bugs \(25 CVEs\) in four popular open\-source EDA applications\. We show how MIRTL gadgets harden traditional backdoors against white\-box countermeasures and demonstrate a real\-world instance of a MIRTL\-hardened backdoor in the CVA6 RISC\-V core\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->