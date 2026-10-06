---
title: "TestTailor: Generating High-Coverage Tests via Path-Proximal Tests with LLMs"
authors: "Xiaoxuan Zhou, Yiling Lou, Jinhao Dong, Dan Hao"
date: "2026-06-30"
source: "FSE"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：FSE · CCF-A · 2026-06-30（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3797140>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Automated unit testing is essential for ensuring software quality\. Achieving high code coverage through automated unit test generation remains challenging, especially for hard\-to\-cover branches guarded by complex or deeply nested conditions\. Traditional search\-based approaches often stagnate at fitness plateaus, while recent LLM\-based techniques provide mostly coarse\-grained prompts, leaving models to guess how to reach uncovered targets\. To address these limitations, we present TestTailor, a neuro\-symbolic framework that exploits fine\-grained, path\-oriented guidance to guide LLM\-based test generation\. The key idea is to exploit path\-proximal tests \(i\.e\., existing test cases whose execution paths closely resemble the target uncovered path\) and to analyze their divergence points\. By combining this analysis with symbolic constraints \(i\.e\., constraints collected from the target uncovered path using symbolic execution\), TestTailor derives actionable path guidance and encodes them into concise prompts that tell the LLM not only what remains uncovered, but also how to reach it\. We evaluate TestTailor on the widely used CODAMOSA benchmark comprising 486 Python modules\. Results show that TestTailor consistently outperforms state\-of\-the\-art baselines, improving statement coverage by 5\.01% and branch coverage by 4\.17% on average compared to the best baseline CoverUp, while incurring only about 40% of CoverUp&\#x27;s API cost\. Against the hybrid LLM\-search\-based technique CODAMOSA, TestTailor achieves even larger gains of 12\.23% and 12\.54% in statement and branch coverage, respectively\. Moreover, TestTailor attains the highest coverage accuracy \(85\.2% vs\. 75\.3% for CoverUp and 63\.8% for TELPA\), and demonstrates robustness across different LLM backbones\. These results highlight that TestTailor transforms vague coverage goals into precise path\-level instructions, enabling LLMs to generate high\-coverage test suites more efficiently and accurately\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->