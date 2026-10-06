---
title: "CollisionRepair: First-Aid and Automated Patching for Storage Collision Vulnerabilities in Smart Contracts"
authors: "Yu Pan, Wanjing Han, Yue Duan, Mu Zhang"
date: "2025"
source: "USENIX Security"
tags: ["query:code-vuln", "query:code-analysis", "query:smart-contract"]
pdf: "https://www.usenix.org/system/files/usenixsecurity25-pan-yu.pdf"
---

[返回 CCF-A 文献库](https://wahaha0112.github.io/daily-paper-reader/ccf.html)

**来源**：USENIX Security · CCF-A · 2025（year 精度）

[出版社 / 官方论文页面](<https://www.usenix.org/conference/usenixsecurity25/presentation/pan-yu>)

> 本页依据公开书目与可用摘要整理，未读取或验证论文全文。CCF-A 标签标记来源，不代表单篇论文质量。

## Abstract

Storage collision vulnerabilities, a significant security risk in upgradeable smart contracts, often arise when a user\-facing proxy contract and a backend logic contract share storage space\. While static analysis techniques can detect such issues, they often over\-approximate program states, leading to false positives and requiring developers to manually verify each issue, giving attackers time to exploit any overlooked vulnerabilities\. To address this, we propose CollisionRepair, an automated patching technique for mitigating storage collision risks\. CollisionRepair monitors storage access sequences between proxy and logic contracts by defining an &quot;ownership&quot; property for storage locations\. It then replays historical transactions to recover existing storage ownership, ensuring the patched code aligns with the current state\. A gas impact\-aware differential analysis is applied to verify the patch, distinguishing genuine behavioral changes from variations caused by gas usage\. Our evaluation on 12,526 real\-world vulnerable upgradeable contracts shows that CollisionRepair effectively detects and mitigates storage collision attacks without interfering with normal contract operations\.

## 阅读状态

尚未调用模型生成解读；标题关键词匹配仅用于初筛。

<!-- ccf-user-notes -->