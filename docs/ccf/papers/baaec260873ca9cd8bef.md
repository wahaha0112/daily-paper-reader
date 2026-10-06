---
title: "SymWeb: Feedback-Driven Context Exploration and Context-Aware Symbolic Execution for Browser-Embedded WebAssembly Vulnerability Detection"
authors: "Yuanpeng Wang, Yeqi Fu, Zhineng Zhong, Zhenkai Liang, Ding Li, Yao Guo, Xiangqun Chen"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-vuln", "query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832163>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Browser\-deployed WebAssembly \(Wasm\) modules often inherit memory\-safety bugs from C and C\+\+\-style code, yet exploiting, and even reaching, these bugs in the Web threat model is fundamentally context\-dependent\. JavaScript \(JS\) controls the exported\-call schedule and constructs the Wasm entry state, including arguments, globals, and linear\-memory layouts, from attacker\-influenced web inputs\. This makes both Wasm\-only analysis, which assumes static initial states, and prior browser\-based testing such as Wemby ineffective\. Wemby generates a fixed, Wasm\-agnostic context pool and then only mutates Wasm parameters, which limits its ability to systematically reach deeper, Wasm\-relevant contexts and gated behaviors\. We present SymWeb, a feedback\-driven closed\-loop system that links external inputs to browser\-reachable JS\-induced Wasm contexts and then to context\-aware Wasm symbolic execution\. SymWeb couples an Feedback\-driven Context Generator with an Context\-Aware Wasm Symbolic Executor\. The Feedback\-driven Context Generator performs binary rewriting for ASan\-like checks and observability, collects contexts in the browser, and uses Influence\-guided Mutation to steer web inputs\. The symbolic executor clusters and symbolizes contexts, performs coverage\-guided symbolic execution under reachable entry states, and returns actionable constraints to steer the next online round\. We evaluate SymWeb on 30 real\-world Wasm\-enabled websites\. Under our Web threat model, SymWeb verifies 17 exploitable vulnerabilities and achieves 72\.8% average Wasm basic\-block coverage\. Compared to the browser\-based baseline Wemby, SymWeb finds 8 more verified vulnerabilities and improves coverage by 19\.9 percentage points\. Compared to the Wasm\-only baseline WASEM, SymWeb finds 14 more verified vulnerabilities and improves coverage by 40\.4 percentage points\. Overall, these results show that closing the loop between browser\-reachable context generation and context\-aware Wasm analysis substantially improves both vulnerability\-finding effectiveness and exploration depth in real Web environments\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->