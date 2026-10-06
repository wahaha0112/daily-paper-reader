---
title: "SureDistrib: Verifying Almost-Sure Termination of Composite Asynchronous Byzantine Protocols"
authors: "Longfei Qiu, Jingqi Xiao, Ji-Yong Shin, Zhong Shao"
date: "2026-06-08"
source: "PLDI"
tags: []
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：PLDI · CCF-A · 2026-06-08（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808293>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Consensus algorithms play a central role in many distributed systems, including blockchains\. The most practical consensus algorithms are based on the partial synchrony model\. While partially synchronous protocols are relatively simple, they cannot maintain liveness when the message delivery latency is uncertain\. Asynchronous protocols do not rely on bounded latency to maintain liveness, but they are much more difficult to understand and implement, being usually described as a composition of several layers of algorithms\. Moreover, due to the FLP impossibility theorem, they only provide probabilistic liveness guarantees\. These factors make the correctness of asynchronous protocols challenging to verify, and there have been liveness bugs in these protocols that remain unnoticed for years\. We introduce SureDistrib, a formal framework for specifying and verifying probabilistic safety and liveness properties of asynchronous distributed protocols\. Our framework supports specifying probabilistic algorithms that depend on other probabilistic functionalities, such as binary agreement algorithms depending on common coins\. We define refinement relations for such systems, and prove composition lemmas that replace the underlay functionality with an implementation, so that the composed system refines the original system with an abstract underlay\. Based on our framework, we give the first mechanized proof that an asynchronous byzantine fault\-tolerant binary agreement algorithm terminates with probability 1 \(“almost\-sure termination”\)\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->