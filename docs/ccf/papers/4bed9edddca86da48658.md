---
title: "Analyzing Bytes: Pre-Disassembly Static Binary Analysis"
authors: "Huan Nguyen, Soumyakant Priyadarshan, Chencheng Jiang, R. Sekar"
date: "2026-06-08"
source: "PLDI"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：PLDI · CCF-A · 2026-06-08（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808292>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Binary code analysis plays a central role in numerous applications in software security, performance optimization, reverse engineering, and so on\. Existing techniques need to first disassemble binaries into functions in assembly code before an analysis can be performed\. However, disassembly and function identification have proven to be major challenges for complex variable\-length instruction sets such as the x86\. A recent trend has been to use static analysis to improve the accuracy of these tasks\. This raises a chicken\-and\-egg problem: a disassembly is needed for static analysis, but a static analysis is needed for accurate disassembly\! We overcome this problem by developing a novel static analysis approach that can operate before committing to a disassembly\. Our analysis operates on the output of exhaustive disassembly that considers each possible offset in a binary as an instruction, and constructs what is known as a super\-set control\-flow graph \(CFG\)\. The central technical challenge in analyzing this CFG is that it mixes legitimate instructions with unintended ones, causing analysis results from invalid code paths to pollute legitimate ones\. To overcome this challenge, we begin with a key new insight that if we focus on backward analyses, we can ensure accuracy of analysis results at intended instructions even though we have no idea where these intended instructions are\! Moreover, our analysis operates in time that is linear in the size of the binary\. Specifically, in O \( n \) total time, it yields analysis results for every one of the n offsets in an n \-byte binary\. For this task, it is orders of magnitude faster than previous techniques, as the previous techniques typically need to repeat the analysis many times\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->