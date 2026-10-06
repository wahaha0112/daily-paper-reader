---
title: "IRepair: An Intent-Aware Approach to Repair Data-Driven Errors in Large Language Models"
authors: "Sayem Mohammad Imtiaz, Astha Singh, Fraol Batole, Hridesh Rajan"
date: "2025-06-19"
source: "FSE"
tags: ["query:skill"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2025-06-19（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3715775>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Not a day goes by without hearing about the impressive feats of large language models \(LLMs\), and equally, not a day passes without hearing about their challenges\. LLMs are notoriously vulnerable to biases in their dataset, leading to issues such as toxicity, harmful responses, and factual inaccuracies\. While domain\-adaptive training has been employed to mitigate these issues, these techniques often address all model parameters indiscriminately during the repair process, resulting in poor repair quality and reduced model versatility\. In this paper, drawing inspiration from fault localization via program slicing, we introduce a novel dynamic slicing\-based intent\-aware LLM repair strategy, IRepair \. This approach selectively targets the most error\-prone sections of the model for repair\. Specifically, we propose dynamically slicing the model’s most sensitive layers that require immediate attention, concentrating repair efforts on those areas\. This method enables more effective repairs with potentially less impact on the model’s overall performance by altering a smaller portion of the model\. Furthermore, dynamic selection allows for a more nuanced and precise model repair compared to a fixed selection strategy\. We evaluated our technique on three models from the GPT2 and GPT\-Neo families, with parameters ranging from 800M to 1\.6B, in a toxicity mitigation setup\. Our results show that IRepair repairs errors 43\.6% more effectively while causing 46% less disruption to general performance compared to the closest baseline, direct preference optimization \. Our empirical analysis also reveals that errors are more concentrated in a smaller section of the model, with the top 20% of layers exhibiting 773% more error density than the remaining 80%\. This highlights the need for selective repair\. Additionally, we demonstrate that a dynamic selection approach is essential for addressing errors dispersed throughout the model, ensuring a robust and efficient repair\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->