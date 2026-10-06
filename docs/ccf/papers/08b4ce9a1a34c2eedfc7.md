---
title: "VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns"
authors: "Jia Li, Zhuangbin Chen, Yuxin Su, Michael R. Lyu"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-vuln", "query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3808117>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

The increasing prevalence of software vulnerabilities highlights the need for effective Automatic Vulnerability Repair \(AVR\) tools\. While LLM\-based approaches are promising, they struggle to incorporate structured security knowledge from sources like CWE and NVD\. Current methods either use this information superficially by concatenating the CWE\-ID into the input prompt, yielding negligible benefits, or rely on few\-shot learning with rigid, non\-generalizable examples, which limits their effectiveness in real\-world scenarios\. To address this gap, we propose VulKey, an LLM\-based AVR framework that leverages a hierarchical abstraction of expert knowledge to guide patch generation\. Our novel three\-level abstraction formulates repair strategies in terms of CWE type, syntactic actions, and semantic key elements\. This approach captures the essence of a security fix with greater generality than concrete examples and more semantic richness than traditional syntax\-based templates, overcoming the coverage limitations of prior methods\. VulKey is implemented as a two\-stage pipeline: first, expert knowledge matching predicts an appropriate repair pattern for the vulnerability; second, repair code generation uses a pattern\-guided, fine\-tuned LLM to produce secure patches\. On the real\-world C/C\+\+ dataset PrimeVul, VulKey achieves 31\.5% repair accuracy, surpassing the best baseline by 7\.6% and outperforming leading tools such as VulMaster and GPT\-5\. Moreover, VulKey demonstrates cross\-language and cross\-model generalizability, with state\-of\-the\-art performance on the Java benchmark Vul4J\. These results underscore the importance of structured expert knowledge in advancing AVR effectiveness\. Our work demonstrates that explicitly modeling and integrating expert security knowledge through hierarchical patterns is a crucial step toward building more effective and reliable AVR tools\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->