---
title: "Generating Project-Specific Test Cases with Requirement Validation Intention"
authors: "Binhang Qi, Yun Lin, Xinyi Weng, Yuhuan Huang, Chenyan Liu, Hailong Sun, Zhi Jin, Jin Song Dong"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832181>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Test cases are valuable assets for maintaining software quality\. State\-of\-the\-art automated test generation techniques typically focus on maximizing program branch coverage or translating focal methods into test code\. However, in contrast to branch coverage or code\-to\-test translation, practical tests are written out of the need to validate whether a requirement has been fulfilled\. Specifically, a test usually reflects a developer’s validation intention for a particular scenario of a program function, regarding \(1\) what is the test scenario of a program function? and \(2\) what is the expected behavior under such a scenario? Without taking such intention into account, generated tests are less likely to be adopted in practice\. In this work, we propose IntentionTest, which generates project\-specific tests given the description of validation intention\. The design is motivated by two insights: \(1\) rationale insight : the description of validation intention regarding scenario description and behavioral expectation, compared to coverage and focal code, carries more crucial information about what to test ; and \(2\) technical insight : practical test code exhibits high duplication, indicating that existing tests are highly reusable for how to test \. Therefore, IntentionTest adopts a retrieval\-and\-edit manner\. First, given a focal code and a description of validation intention consisting of a test objective with test precondition and expected results, IntentionTest retrieves a reusable test in the project as the test reference\. Then, IntentionTest edits the test reference with an LLM regarding the validation intention toward the target test\. To help the target test include a project\-specific test prefix and a relevant assertion, IntentionTest further explores the software project to identify crucial code facts \(i\.e\., relevant API/code to call and global variables to refer to in the test\) as important context for the test generation\. We extensively evaluate IntentionTest against four baselines \(TELPA, DA, ChatTester, and EvoSuite\) on 3,680 test cases from 12 open\-source projects\. Compared to state\-of\-the\-art baselines, with a given validation intention, IntentionTest can \(1\) generate tests far more semantically relevant to ground\-truth tests by \(i\) achieving common mutation scores 28\.1% to 37\.6% higher and \(ii\) achieving common coverage ratios 16\.9% to 23\.9% higher; and \(2\) achieve successful\-pass rates 23\.7% to 49\.0% higher\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->