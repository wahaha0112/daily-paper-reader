---
title: "Compiling by Proving in \\({\\mathbb{K}}\\) : From All-Path Reachability Proofs to Single-Step Semantic Rules"
authors: "Jianhong Zhao, Everett Hildenbrandt, Juan Conejero, Yongwang Zhao"
date: "2026-07-28"
source: "TOSEM"
tags: ["query:code-analysis", "query:smart-contract"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：TOSEM · CCF-A · 2026-07-28（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3828756>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

The \\\(\{\\mathbb\{K\}\}\\\) framework generates language tools from formal semantics and hosts comprehensive semantics for real\-world languages including C, Java, JavaScript, and the Ethereum Virtual Machine, with industrial adoption in blockchain verification\. However, the generated executors interpret programs by applying semantic rules step by step, causing performance overhead that limits practical scalability\. We present compiling by proving , a language\-agnostic mechanism that eliminates this overhead\. Given a code unit, we use symbolic execution to prove that its specification holds across all execution paths, generating a proof graph that encodes the complete input\-output behavior\. We compile this proof graph into a single\-step rule that directly maps inputs to outputs, replacing step\-by\-step interpretation with one\-step execution\. Because the pipeline is language\-agnostic, it benefits any language formalized in \\\(\{\\mathbb\{K\}\}\\\) \. We evaluate on EVM and Rust MIR semantics, showing speedups in concrete and symbolic execution, and demonstrate applications to semantic equivalence verification and compositional smart contract verification\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->