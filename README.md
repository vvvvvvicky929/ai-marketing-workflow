# 《姚金刚提示词合集》

一个面向真实工作、学习、内容、营销和生活场景的中文 AI 提示词库。

本仓库从原始合集文档中拆分出 **100** 个独立提示词文件，并按场景重新分类。每个提示词保留可复制的正文，去除了原文中不适合放入开源仓库主体的教程推广、效果截图、视频附件说明和 HTML 样式残留。

## 仓库结构

```text
prompts/                # 按场景分类的提示词正文
references/             # 推荐资源、第三方内容和外部项目索引
templates/              # 新增提示词模板
maintenance/            # 维护、评审、发布检查清单
scripts/                # 目录生成和仓库质量检查脚本
CATALOG.md              # 全量提示词索引
CHANGELOG.md            # 更新记录
CONTRIBUTING.md         # 贡献和持续迭代规则
```

## 分类

| 分类 | 数量 | 说明 |
| --- | ---: | --- |
| AI方法 | 5 | 元提示词、反编译和提示词工程方法。 |
| AI工作 | 7 | 面向企业、销售、客服、PPT、网页等生产力场景。 |
| AI学习 | 10 | 学习方法、记忆术、习惯养成和学习助理。 |
| AI生活 | 2 | 健康、亲子歌曲等生活场景。 |
| AI教育 | 3 | 儿童教育和小游戏创作。 |
| AI内容 | 68 | 写作、标题、视频、图像和 PPT 创意。 |
| AI编程 | 1 | 架构设计和编程协作。 |
| AI营销 | 2 | GEO 内容生成、改写和营销增长。 |
| AI思考 | 2 | 记忆、标题和思维类灵感提示词。 |

完整目录见 [CATALOG.md](CATALOG.md)。

## 使用方式

1. 在 [CATALOG.md](CATALOG.md) 中按场景找到提示词。
2. 打开对应 Markdown 文件，复制 `Prompt` 区域。
3. 将 `{{变量}}`、`[占位符]` 或示例内容替换为你的真实任务信息。
4. 在目标模型中测试输出，并根据结果记录版本迭代。

## 提示词文件规范

每个提示词文件包含统一 frontmatter：

```yaml
title: 提示词标题
category: 一级分类
subcategory: 子类
source_section: 原合集章节号
author: 作者或来源
version: 提示词版本
created: 创建日期
status: active | draft | third-party-review
tags: 标签列表
```

正文只保留三部分：标题、简介、Prompt。需要展示案例、评测截图、教程链接或长说明时，优先放到 `references/` 或后续的案例目录，不和可复制提示词正文混在一起。

## 持续更新机制

- 新增提示词：复制 [prompt-file-template.md](templates/prompt-file-template.md)，放到对应分类目录。
- 更新提示词：优先在原文件内提升 `version`，并在 [CHANGELOG.md](CHANGELOG.md) 记录变更。
- 调整分类：同步更新 frontmatter 的 `category/subcategory/tags`，然后重新生成目录。
- 质量检查：运行 `python3 scripts/check_repo.py`。
- 重建目录：运行 `python3 scripts/generate_catalog.py`。
- 发布节奏：建议使用日期版本，如 `v2026.05.1`，每次发布前走 [release-checklist.md](maintenance/release-checklist.md)。

## 开源与来源策略

本仓库采用 **CC BY 4.0** 作为提示词内容许可；如果后续加入脚本或工具代码，可单独使用 MIT。明显第三方或转载内容不直接并入主提示词库，先放在 `references/` 或标记为 `third-party-review`，确认授权后再发布。
