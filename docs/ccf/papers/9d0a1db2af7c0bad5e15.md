---
title: "PipeThreader: Software-Defined Pipelining for Efficient DNN Execution"
authors: "Yu Cheng, Lei Wang, Yining Shi, Yuqing Xia, Lingxiao Ma, Jilong Xue, Yang Wang, Zhiwen Mo, Feiyang Chen, Fan Yang, Mao Yang, Zhi Yang"
date: "2025"
source: "OSDI"
tags: []
pdf: "https://www.usenix.org/system/files/osdi25-cheng.pdf"
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：OSDI · CCF-A · 2025（year 精度）

[出版社 / 官方论文页面](<https://www.usenix.org/conference/osdi25/presentation/cheng>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

To effectively utilize heterogeneous specialized hardware units in modern GPUs, such as TensorCores and Tensor Memory Accelerators, this paper introduces PipeThreader, a new DNN compiler\. PipeThreader proposes shifting scheduling functionality from hardware to software so as to enable more efficient and sophisticated computation pipelining with minimal manual effort\. This is achieved through sTask\-graph, a new DNN computation abstraction, a hierarchical hardware abstraction that captures the capabilities of specialized units, and new scheduling primitives\. As a result, PipeThreader can discover efficient pipeline scheduling for well\-studied DNN architectures like FlashAttention, achieving comparable or even superior performance\. Additionally, it can uncover novel pipeline schemes for emerging models like Mamba2, delivering significantly better performance compared to state\-of\-the\-art hand\-crafted implementations\. The code is open\-sourced at https://github\.com/tile\-ai/tilelang \.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->