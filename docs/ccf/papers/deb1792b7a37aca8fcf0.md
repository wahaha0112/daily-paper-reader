---
title: "Statically Analyzing the Dataflow of R Programs"
authors: "Florian Sihler, Matthias Tichy"
date: "2025-10-09"
source: "OOPSLA"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OOPSLA · CCF-A · 2025-10-09（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3763087>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

The R programming language is primarily designed for statistical computing and mostly used by researchers without a background in computer science\. R provides a wide range of dynamic features and peculiarities that are difficult to analyze statically like dynamic scoping and lazy evaluation with dynamic side effects\. At the same time, the R ecosystem lacks sophisticated analysis tools that support researchers in understanding and improving their code\. In this paper, we present a novel static dataflow analysis framework for the R programming language that is capable of handling the dynamic nature of R programs and produces the dataflow graph of given R programs\. This graph can be essential in a range of analyses, including program slicing, which we implement as a proof of concept\. The core analysis works as a stateful fold over a normalized version of the abstract syntax tree of the R program, which tracks \(re\-\)definitions, values, function calls, side effects, external files, and a dynamic control flow to produce one dataflow graph per program\. We evaluate the correctness of our analysis using output equivalence testing on a manually curated dataset of 779 sensible slicing points from executable real\-world R scripts\. Additionally, we use a set of systematic test cases based on the capabilities of the R language and the implementation of the R interpreter and measure the runtimes well as the memory consumption on a set of 4,230 real\-world R scripts and 20,815 packages available on R’s package manager CRAN\. Furthermore, we evaluate the recall of our program slicer, its accuracy using shrinking, and its improvement over the state of the art\. We correctly analyze almost all programs in our equivalence test suite, preserving the identical output for 99\.7 % of the manually curated slicing points\. On average, we require 576 ms to analyze the dataflow and around 213 kB to store the graph of a research script\. This shows that our analysis is capable of analyzing real\-world sources quickly and correctly\. Our slicer achieves an average reduction of 84\.8 % of tokens indicating its potential to improve program comprehension\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->