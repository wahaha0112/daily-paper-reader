---
title: "Generating Project-Specific Test Cases with Requirement Validation Intention"
authors: "Binhang Qi, Yun Lin, Xinyi Weng, Yuhuan Huang, Chenyan Liu, Hailong Sun, Zhi Jin, Jin Song Dong"
date: "2026-10-01"
source: "ISSTA"
tags: ["query:code-analysis"]
title_zh: "生成具有需求验证意图的项目特定测试用例"
score: 8
tldr: "该论文提出 IntentionTest，用于根据验证意图描述生成项目特定的测试用例。作者指出，现有自动化测试生成技术多聚焦于最大化分支覆盖率或将焦点方法翻译为测试代码，而实际测试往往源于开发者验证某需求是否被满足的意图，即测试场景是什么、该场景下的预期行为是什么。IntentionTest 基于两点洞察：验证意图描述比覆盖率和焦点代码包含更关键的“测什么”信息；实际测试代码高度重复，说明已有测试在“怎么测”上高度可复用。因此方法采用检索加编辑的方式：先根据焦点代码和验证意图检索项目中可复用的测试作为参考，再用大语言模型按验证意图编辑该参考测试，并探索项目以识别关键代码事实作为上下文。论文在 12 个开源项目的 3680 个测试用例上与四个基线比较。"
evidence: "该论文属于程序分析与软件测试方向，研究自动化测试生成、测试用例复用与检索、基于大语言模型的测试编辑，并强调需求验证意图与断言生成，与 code-analysis 标签中“测试生成、静态动态分析、代码复用识别”的研究范围高度契合。其检索复用已有测试的思路也与代码克隆和复用识别相关。论文未涉及漏洞检测、供应链、恶意软件、智能合约或 AI Agent 安全，因此不归入其他标签。"
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：ISSTA · CCF-A · 2026-10-01（day 精度）

[出版社 / 官方论文页面](<https://doi.org/10.1145/3832181>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Test cases are valuable assets for maintaining software quality\. State\-of\-the\-art automated test generation techniques typically focus on maximizing program branch coverage or translating focal methods into test code\. However, in contrast to branch coverage or code\-to\-test translation, practical tests are written out of the need to validate whether a requirement has been fulfilled\. Specifically, a test usually reflects a developer’s validation intention for a particular scenario of a program function, regarding \(1\) what is the test scenario of a program function? and \(2\) what is the expected behavior under such a scenario? Without taking such intention into account, generated tests are less likely to be adopted in practice\. In this work, we propose IntentionTest, which generates project\-specific tests given the description of validation intention\. The design is motivated by two insights: \(1\) rationale insight : the description of validation intention regarding scenario description and behavioral expectation, compared to coverage and focal code, carries more crucial information about what to test ; and \(2\) technical insight : practical test code exhibits high duplication, indicating that existing tests are highly reusable for how to test \. Therefore, IntentionTest adopts a retrieval\-and\-edit manner\. First, given a focal code and a description of validation intention consisting of a test objective with test precondition and expected results, IntentionTest retrieves a reusable test in the project as the test reference\. Then, IntentionTest edits the test reference with an LLM regarding the validation intention toward the target test\. To help the target test include a project\-specific test prefix and a relevant assertion, IntentionTest further explores the software project to identify crucial code facts \(i\.e\., relevant API/code to call and global variables to refer to in the test\) as important context for the test generation\. We extensively evaluate IntentionTest against four baselines \(TELPA, DA, ChatTester, and EvoSuite\) on 3,680 test cases from 12 open\-source projects\. Compared to state\-of\-the\-art baselines, with a given validation intention, IntentionTest can \(1\) generate tests far more semantically relevant to ground\-truth tests by \(i\) achieving common mutation scores 28\.1% to 37\.6% higher and \(ii\) achieving common coverage ratios 16\.9% to 23\.9% higher; and \(2\) achieve successful\-pass rates 23\.7% to 49\.0% higher\.

## AI 摘要解读

该论文提出 IntentionTest，用于根据验证意图描述生成项目特定的测试用例。作者指出，现有自动化测试生成技术多聚焦于最大化分支覆盖率或将焦点方法翻译为测试代码，而实际测试往往源于开发者验证某需求是否被满足的意图，即测试场景是什么、该场景下的预期行为是什么。IntentionTest 基于两点洞察：验证意图描述比覆盖率和焦点代码包含更关键的“测什么”信息；实际测试代码高度重复，说明已有测试在“怎么测”上高度可复用。因此方法采用检索加编辑的方式：先根据焦点代码和验证意图检索项目中可复用的测试作为参考，再用大语言模型按验证意图编辑该参考测试，并探索项目以识别关键代码事实作为上下文。论文在 12 个开源项目的 3680 个测试用例上与四个基线比较。

**方向相关性**：该论文属于程序分析与软件测试方向，研究自动化测试生成、测试用例复用与检索、基于大语言模型的测试编辑，并强调需求验证意图与断言生成，与 code\-analysis 标签中“测试生成、静态动态分析、代码复用识别”的研究范围高度契合。其检索复用已有测试的思路也与代码克隆和复用识别相关。论文未涉及漏洞检测、供应链、恶意软件、智能合约或 AI Agent 安全，因此不归入其他标签。

**证据限制**：仅凭摘要无法核验：IntentionTest 的具体检索与编辑算法细节、关键代码事实的识别方式、提示词设计；实验所用 12 个开源项目的名称与选取标准；3680 个测试用例的构造与标注方式；四个基线（TELPA、DA、ChatTester、EvoSuite）的配置与公平性；变异分数、覆盖率、通过率提升数字的统计显著性与可复现性；验证意图描述的来源与质量；方法对非 Java 或其他语言项目的泛化能力。摘要中给出的提升幅度未在全文层面核实。

<!-- ccf-user-notes -->