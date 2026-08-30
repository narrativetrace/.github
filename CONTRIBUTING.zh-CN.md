<!-- i18n: source=CONTRIBUTING.md lang=zh-CN -->

> 🌐 [English](CONTRIBUTING.md) · 简体中文 · [Español](CONTRIBUTING.es.md) · [Português](CONTRIBUTING.pt-BR.md) · [Français](CONTRIBUTING.fr.md)
>
> _本翻译仅为方便阅读而提供，英文版本为权威版本。_

# 为 NarrativeTrace 做贡献

感谢您对 NarrativeTrace 的关注。本文档适用于 [narrativetrace](https://github.com/narrativetrace) 组织下的每一个仓库。每个库的仓库都有自己的 `CONTRIBUTING.md`（或 `README.md`），其中包含该运行时的构建和测试说明。

## 我们接受的贡献

- **欢迎小型 Pull Request**——缺陷修复、文档修正、测试改进、小型且自包含的增强。
- **较大的改动：请先发起讨论。** 在投入大量精力之前，请在相关仓库中发起一个 GitHub Discussion（或 Issue），描述问题以及您建议的方案。这样可以避免在改动不符合项目方向时白费功夫。
- **设计层面的改动必须经过讨论。** 追踪格式、基线语义、脱敏行为以及注解模型是所有运行时（Java、.NET、TypeScript、Swift、Python）共享的契约。对它们的任何改动都必须先在讨论中达成一致，然后才能开始编写代码，因为这些改动需要在每个实现中保持一致地落地。

## 报告缺陷

请在相关仓库中提交 Issue，并提供：

- 库及其版本；
- 运行时/平台版本（JDK、.NET、Node、Swift、Python）；
- 最小化的复现步骤；
- 预期行为与实际行为的对比。

**安全问题不得作为公开 Issue 报告。** 请参阅 [SECURITY.md](SECURITY.zh-CN.md)。

## Developer Certificate of Origin

所有贡献都必须依据 [Developer Certificate of Origin](https://developercertificate.org/)（开发者原创证书，DCO）进行签署。通过签署，您证明该贡献由您本人撰写，或者您拥有依据下文“许可证”一节所述的入站许可提交它的权利。

请使用 `git commit -s` 为每次提交添加签署，该命令会追加一行类似如下的内容：

```
Signed-off-by: Your Name <your.email@example.com>
```

请使用您的真实姓名和一个可用的电子邮件地址。包含未签署提交的 Pull Request 无法被合并。

## 提交信息

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<optional scope>): <short summary>

<optional body explaining what and why>
```

常用类型：`feat`、`fix`、`docs`、`test`、`refactor`、`perf`、`build`、`ci`、`chore`。破坏性变更请在类型后加 `!` 标记（如 `feat!:`），并在正文中加以说明。

## 分支

从 `main` 创建分支，并使用以提交类型为前缀的简短、描述性的名称：

```
feat/value-references
fix/redaction-map-keys
docs/annotations-guide
```

## Pull Request

- 每个 PR 只专注于一项改动。
- 为行为改动添加测试；在相关之处更新文档。
- 在提交 PR 之前，确保构建和测试在本地通过（具体方法请参阅各仓库自己的贡献指南）。
- 在 PR 描述中引用相关的 Issue 或讨论。
- 请及时回应评审反馈；我们是一个小团队，评审可能需要一些时间。

## 许可证

NarrativeTrace 的许可分为三部分，每个仓库都会标明各制品属于哪一部分：

- **API 与输出格式**（`narrativetrace-api` 及其各平台等价物、格式规范、清晰度评分标准）是采用 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 的开放标准；
- **运行时**可免费使用（包括生产环境），源码可见，采用 [Business Source License 1.1](https://mariadb.com/bsl11/)；每个版本在发布四年后转为 Apache 2.0；
- **NarrativeTrace Pro** 为商业产品，不在这些仓库中开发。

**贡献的入站许可。** 提交贡献即表示您将该贡献依据 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 授权给 Empower Agile 以及本项目的所有接收者，无论它涉及项目的哪一部分。正是这一点使得对运行时的贡献今天可以在 Business Source License 下分发、在转换日期转为 Apache 2.0，并可纳入商业版本——同时您保留版权，以及 Apache 2.0 赋予您在别处使用自己作品的一切权利。对 API 与格式的贡献则是 Apache 2.0 进、Apache 2.0 出。

每次提交的 DCO 签署即是您对上述授权的证明；无需另行签署贡献者协议。对文档的贡献采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权。
