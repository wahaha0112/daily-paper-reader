---
title: "KRAKEN: Program-Adaptive Parallel Fuzzing"
authors: "Anshunkang Zhou, Heqing Huang, Charles Zhang"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728882>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Parallel fuzzing, which utilizes multicore computers to accelerate the fuzzing process, has been widely used in industrial\-scale software defect detection\. However, specifying efficient parallel fuzzing strategies for programs with different characteristics is challenging due to the difficulty of reasoning about fuzzing runtime statically\. Existing efforts still use pre\-defined tactics for various programs, resulting in suboptimal performance\. In this paper, we propose Kraken , a new program\-adaptive parallel fuzzer that improves fuzzing efficiency through dynamic strategy optimization\. The key insight is that the inefficiency in parallel fuzzing can be observed during runtime through various feedbacks, such as code coverage changes, which allows us to adjust the adopted strategy to avoid inefficient path searching, thus gradually approximating the optimal policy\. Based on the above insight, our key idea is to view the task of finding the optimal strategy as an optimization problem and gradually approach the best program\-specific strategy on the fly by maximizing certain objective functions\. We have implemented Kraken in C/C\+\+ and evaluated it on 19 real\-world programs against 8 state\-of\-the\-art parallel fuzzers\. Experimental results show that Kraken can achieve 54\.7% more code coverage and find 70\.2% more bugs in the given time\. Moreover, Kraken has found 192 bugs in 37 popular open\-source projects, and 119 of them are assigned with CVE IDs\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->