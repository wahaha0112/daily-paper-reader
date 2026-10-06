---
title: "OBsmith: LLM-Powered JavaScript Obfuscator Testing"
authors: "Shan Jiang, Chenguang Zhu, Sarfraz Khurshid"
date: "2026-04-10"
source: "OOPSLA"
tags: ["query:code-analysis", "query:skill"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2026-04-10（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3798204>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

JavaScript obfuscators are widely deployed to protect intellectual property and resist reverse engineering, yet their correctness has been largely overlooked compared to performance and resilience\. Existing evaluations typically measure resistance to deobfuscation, leaving the critical question of whether obfuscators preserve program semantics unanswered\. Incorrect transformations can silently alter functionality, compromise reliability, and erode security\-undermining the very purpose of obfuscation\. To address this gap, we present OBsmith, a novel framework to systematically test JavaScript obfuscators using large language models \(LLMs\)\. OBsmith leverages LLMs to generate program sketches\-abstract templates capturing diverse language constructs, idioms, and corner cases\-which are instantiated into executable programs and subjected to obfuscation under different configurations\. Besides LLM\-powered sketching, OBsmith also employs a second source: automatic extraction of skeletons from real programs\. This extraction path enables more focused testing of project\-specific features and lets developers inject domain knowledge into the resulting test cases\. OBsmith uses two techniques to derive test oracles: \(i\) reference\-oriented equivalence testing, which takes the original program as reference oracle \(ground truth\) and checks whether the obfuscated version preserves equivalent functionality, and \(ii\) metamorphic testing, which applies semantics\-preserving transformations to the original program and checks if obfuscation violates expected behavior\. We evaluate OBsmith on two widely used obfuscators, Obfuscator\.IO and JS\-Confuser, generating 600 sketches using six popular LLMs\. OBsmith fills these sketches and generates over 3,000 candidate programs and obfuscates them across seven obfuscation configurations\. OBsmith uncovers 11 previously unknown correctness bugs\. Under an equal program budget, five general purpose state\-of\-the\-art JavaScript fuzzers \(FuzzJIT, Jsfunfuzz, Superion, DIE, Fuzzilli\) failed to detect these issues, highlighting OBsmith&\#x27;s complementary focus on obfuscation\-induced misbehavior\. An ablation shows that all components except our generic MRs contribute to at least one bug class; the negative MR result suggests the need for obfuscator\-specific metamorphic relations\. Our results also seed a discussion on how to balance obfuscation presets and performance cost\. We envision OBsmith as an important step towards automated testing and quality assurance of obfuscators and other semantic\-preserving toolchains\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->