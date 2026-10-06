---
title: "WITFuzz: Validity-Preserving Greybox Fuzzing for WebAssembly Interface Type Binding Generators"
authors: "Hanqin Guan, Ningyu He, Shangtong Cao, Yifeng Cai, Yao Guo, Ding Li"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832281>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Modern build pipelines often rely on code generation to turn constraint\-rich interface specifications into artifacts for target programming languages\. In the WebAssembly component model, binding generators \(bindgens\) follow this pattern by translating WebAssembly Interface Types \(WIT\) packages into language\-specific bindings that are later compiled with application code\. This bindgen step already targets more than ten language ecosystems, and the Rust wit\-bindgen crate alone has accumulated tens of millions of downloads\. Yet a WIT package may pass WIT validation but still break this build pipeline: bindgens may crash or hang during generation \(Phase I\), or downstream toolchains may reject the generated bindings even when generation succeeds \(Phase II\)\. Testing bindgens at scale is challenging because WIT is strongly typed and constraint\-rich, and Phase II failures require language\-specific checking\. We present WITFuzz, a validity\-preserving greybox fuzzer for WIT bindgens\. WITFuzz mutates resolved WIT abstract syntax trees via structure\-aware rewrites expressed in a small domain\-specific language, and propagates correlated updates to maintain WIT validity\. When coverage plateaus, WITFuzz expands its strategy pool online using coverage\-guided, LLM\-assisted DSL synthesis, admitting only strategies that pass local validation\. WITFuzz further uses a build\-aware, multi\-layer oracle that combines in\-loop checks with selective asynchronous compilation/typechecking of generated bindings to capture non\-crashing build breakers\. Across 12 bindgens, WITFuzz improves average edge coverage by 8\.3% over standalone wit\-smith\. It uncovers 40 previously unknown Phase I and Phase II build\-breaking bugs, including 35 that are missed by all external baselines\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->