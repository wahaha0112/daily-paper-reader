---
title: "ALMOND: Learning an Assembly Language Model for 0-Shot Code Obfuscation Detection"
authors: "Xuezixiang Li, Sheng Yu, Heng Yin"
date: "2025-06-22"
source: "ISSTA"
tags: ["query:malware"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2025-06-22（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3728886>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Code obfuscation is a technique used to protect software by making it difficult to understand and reverse engineer\. However, it can also be exploited for malicious purposes such as code plagiarism or developing malicious programs\. Learning\-based techniques have achieved great success with the help of supervised learning and labeled training sets\. However, when faced with real\-life environments involving privately developed and undisclosed obfuscators, these supervised learning methods often raise concerns about generalizability and robustness when facing unseen and unknown classes of obfuscation techniques\. This paper presents ALMOND, a novel zero\-shot approach for detecting code obfuscation in binary executables\. Unlike previous supervised learning methods, ALMOND does not require labeled obfuscated samples for training\. Instead, it leverages a language model pre\-trained only on unobfuscated assembly code to identify the linguistic deviations introduced by obfuscation\. The key innovation is the use of &quot;error\-perplexity&quot; as a detection metric, which focuses on tokens the model fails to predict\. Continuous Error Perplexity further enhances this to capture consecutive prediction errors characteristic of obfuscated sequences\. Experiments show ALMOND achieves 96\.3% accuracy on unseen obfuscation methods, outperforming supervised baselines\. On real\-world malware samples, it demonstrates an AUC of 0\.869 and significantly outperforms the supervise\-learning baseline\. Our Dataset, pre\-trained model, and code of evaluation will be available at https://github\.com/palmtreemodel/ALMOND

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->