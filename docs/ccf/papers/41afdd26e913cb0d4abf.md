---
title: "CLIR: Liveness-Driven and Structure-Aware Fuzzing for the Cranelift Compiler"
authors: "Shangtong Cao, Tianlei Song, Qiuping Yi, Tianyu Chen, Guoai Xu, Ningyu He, Haoyu Wang"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832230>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Modern compilers are complex software systems that must correctly translate high\-level programming languages into machine code across multiple architectures\. Cranelift, a fast and modern compiler backend originally developed for WebAssembly and recently adopted as an experimental backend for Rust, has gained increasing importance due to its superior compilation speed compared to LLVM and comprehensive multi\-architecture support, including x86\-64, AArch64, s390x, and RISCV64\. However, despite decades of development in compiler testing, testing Cranelift still presents unique challenges, including \(1\) constructing valid IR under the strict enforcement of SSA form, \(2\) generating sequences with sufficient computational density to stress backend components, and \(3\) balancing broad backend coverage with efficient root cause analysis across heterogeneous architectures\. To address these challenges, we propose CLIR, a differential testing framework that integrates a syntax\-preserving hierarchical generation strategy to guarantee SSA validity, a liveness\-guided instruction refinement mechanism to maximize computational density, and a diagnosis\-guided cross\-architecture adaptation scheme to facilitate efficient root cause analysis across heterogeneous backends\. Our comprehensive evaluation demonstrates that CLIR substantially outperforms existing state\-of\-the\-art baselines, detecting 8×, 24×, and 8× as many unique bugs as cranelift\-fuzzgen, wasm\-smith, and WASMaker, respectively, while RustSmith uncovered no bugs\. Within 72 hours of testing, CLIR discovered 24 bugs spanning all target architectures, with 21 confirmed and 9 fixed\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->