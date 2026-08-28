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

所有贡献都必须依据 [Developer Certificate of Origin](https://developercertificate.org/)（开发者原创证书，DCO）进行签署。通过签署，您证明该贡献由您本人撰写，或者您拥有在本项目的 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 许可证下提交它的权利。

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

您提交贡献即表示同意您的贡献依据 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 授权，与本项目采用相同的许可证。
