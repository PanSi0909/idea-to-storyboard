# idea-to-storyboard｜一键式短片分镜

把一句短片想法，经苏格拉底追问、8句话故事、故事设计卡、逻辑核查、150秒七拍和一致性设计，整理成可执行的文字分镜表。

> 核心观念：短片不是压缩长片，而是放大一次选择。

## 一分钟开始

本 Skill 已在 Codex 桌面版、Codex CLI 和 Codex IDE 扩展的 Skills 工作流中验证。

在 Codex 中输入：

```text
$skill-installer
```

然后发送：

```text
请安装这个 GitHub Skill：
https://github.com/PanSi0909/idea-to-storyboard/tree/main/skills/idea-to-storyboard
```

安装完成后新开一个对话，直接输入：

```text
$idea-to-storyboard 把这个想法做成150秒短片分镜：20年后，人类把情感关系交给AI代理。
```

![使用 Skill Installer 安装](docs/images/00-install.svg)

## 它怎样工作

```mermaid
flowchart LR
    A[一句想法或已有材料] --> B[苏格拉底追问]
    B --> C[8句话故事与故事卡]
    C --> D[逻辑核查并锁定核心]
    D --> E[150秒七拍]
    E --> F[角色与场景一致性]
    F --> G[八列文字分镜与验收]
```

| 阶段 | 主要结果 |
|---|---|
| 发现故事 | 已知事实、关键缺口、1—3个关键追问 |
| 搭建故事 | 核心表达、8句话故事、故事设计卡 |
| 锁定核心 | 逻辑核查、不可擅改的五项核心 |
| 组织节奏 | 约150秒七拍，每20—30秒一次新信息 |
| 固定一致性 | 角色锚点、场景锚点、视觉方向 |
| 生成分镜 | 八列文字分镜、时长和升级验收 |

它生成的是故事设计和文字分镜，不会自动拍摄、剪辑或生成最终视频。

## 你可以从任何阶段开始

| 你现在有什么 | 可以这样说 | Skill 从哪里接手 |
|---|---|---|
| 只有一句想法 | “把这个想法做成150秒短片分镜……” | 从关键追问开始 |
| 已有8句话或故事卡 | “核查逻辑，不要改变我的核心选择” | 从逻辑核查开始 |
| 已有剧本 | “整理成150秒七拍和分镜” | 提取并确认核心后拆分 |
| 已有分镜 | “只检查时长、阻碍升级和一致性” | 从验收开始 |
| 在线文档或文件 | “读取这份内容，先给修改建议” | 先读取；经授权后才写回 |

不知道“反向选择”“英雄镜头”或“景别”也没关系。信息不足时，Skill 只追问真正会改变故事方向的1—3个问题。

## 不会被擅自改动的内容

进入分镜前，Skill 会明确锁定以下五项：

1. 主角的内在问题
2. 主角先采用的错误办法
3. 最后的关键选择
4. 英雄镜头
5. 结尾余味

发现冲突时会先指出问题；未经确认，不会为了增强戏剧性而擅自加入反派、死亡、阴谋或新的世界制度。

![锁定核心五项](docs/images/03-core-lock.svg)

## 完整安装与验证

### 推荐安装

你需要能够访问 GitHub 的 Codex 桌面版、Codex CLI 或 Codex IDE 扩展。不需要额外安装 GitHub CLI、Python 或视频剪辑软件。

1. 输入 `$skill-installer`。
2. 提供上方 GitHub 子目录地址。
3. 安装完成后新开对话；若仍未出现，重启 Codex。
4. 输入 `/skills` 或在输入框中键入 `$`，查找 `idea-to-storyboard`。

![检查并调用 Skill](docs/images/00-verify.svg)

Codex 支持显式调用和自动匹配。第一次使用建议显式输入 `$idea-to-storyboard`。详见 [OpenAI Skills 官方文档](https://developers.openai.com/codex/skills)。

### 更新

再次让 Codex 安装同一个 GitHub 地址即可发起更新。如果安装器提示目标已经存在，请让 Codex 先备份旧目录，再重新安装；验证新版本正常后，再决定是否删除备份。

可以直接说：

```text
请更新 idea-to-storyboard。更新前保留旧版本备份，安装并验证成功后告诉我差异，不要直接删除备份。
```

### 手动安装

如果当前环境没有 `$skill-installer`：

1. 在 GitHub 点击 `Code` → `Download ZIP` 并解压。
2. 找到 `skills/idea-to-storyboard` 文件夹。
3. 将该文件夹复制到个人 Skills 目录：
   - macOS／Linux：`$HOME/.agents/skills/idea-to-storyboard`
   - Windows：`%USERPROFILE%\.agents\skills\idea-to-storyboard`
4. 确认目标目录下直接存在 `SKILL.md`，不要多套一层同名文件夹。
5. 重启 Codex，并用 `/skills` 检查。

`dist/idea-to-storyboard.skill` 是经过校验的分发压缩包，不是所有客户端都支持双击安装；初次使用优先选择 `$skill-installer`。

## 第一次使用模板

```text
$idea-to-storyboard

我想做一个约150秒的短片。
主题或作业要求：
我的初步想法：
我最不希望被改变的内容：
已有材料：没有／故事片段／故事卡／剧本／文档链接
```

![从一句想法开始](docs/images/01-start.svg)

Skill 会判断素材已经完成到哪一步，确认故事核心后，再继续生成150秒结构、角色场景卡和完整分镜。

![六步创作流程](docs/images/02-workflow.svg)

最终分镜逐镜列出时间、场景、单一情绪任务、画面动作、景别／机位／运镜、声音／台词和功能标记。

![检查分镜并按授权同步](docs/images/04-output.svg)

## 原创示例案例

[《那只歪船》](examples/the-crooked-boat.md)展示了从核心表达、8句话故事、故事设计卡到150秒七拍和21个镜头的完整结果。

> 一个习惯让AI替自己处理生活与社交的人，必须决定是否亲自完成一次可能尴尬、失败的告别。

第一次阅读建议依次检查：决定性选择是否清楚、阻碍是否升级、英雄镜头是否与旧办法相反，以及结尾是否用无台词动作留下余味。

更细的操作说明见[小白使用指南](docs/BEGINNER-GUIDE.md)。

## 外部文档与平台兼容性

作者本人使用飞书，因此部分开发过程最初在飞书中完成；本 Skill 不依赖飞书，也不限定文档平台。

用户可以提供在线文档链接、Word、Markdown、PDF 或其他当前环境能够读取的内容。默认结果直接在对话中输出；只有用户明确授权，且当前环境具备对应平台连接能力时，才会写回外部文档。

| 环境 | 当前状态 |
|---|---|
| Codex 桌面版／CLI／IDE 扩展 | 已验证 Skills 安装与调用路径 |
| 其他支持 Agent Skills 的工具 | 可读取 `skills/idea-to-storyboard/SKILL.md`；具体安装方式取决于平台 |
| 飞书、Word、Markdown、PDF | 作为输入或同步目标，不是运行依赖 |

未验证的平台不会在文档中标记为“完整支持”。

## 常见问题

**输入 `$idea-to-storyboard` 后没有出现 Skill？** 先用 `/skills` 检查；若刚安装或更新，重启 Codex。

**只有一句想法可以吗？** 可以。Skill 会补问真正影响故事方向的内容。

**会直接修改我的在线文档吗？** 不会。只有你明确授权具体文档，且当前环境支持写入时才会修改。

**能直接生成视频吗？** 不能。当前交付是故事卡、结构和文字分镜。

**可以只检查已有内容吗？** 可以。说明你只需要逻辑、节奏或一致性检查，并列出不能改动的内容。

## 仓库结构

```text
idea-to-storyboard/
├── skills/idea-to-storyboard/  # 可安装的 Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── docs/                        # 小白指南和教程图片
├── examples/                    # 原创示例案例
├── scripts/                     # 仓库自动校验
├── dist/                        # .skill 包和 SHA-256 校验和
├── .github/                     # Issues 模板和持续集成
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

## 贡献与反馈

- Bug 或安装问题：提交 Bug report，并写明 Codex 版本、系统和复现步骤。
- 输出质量问题：提供输入、实际输出、期望结果，以及哪些核心内容不能改变。
- 功能建议：说明使用场景，不必预先设计实现方式。

提交修改前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。版本变化记录在 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

- `skills/`、`docs/`、`scripts/` 及仓库维护文件采用 [MIT License](LICENSE)。
- 原创案例 [《那只歪船》](examples/the-crooked-boat.md)采用 [CC BY-NC 4.0](examples/LICENSE.md)：允许署名分享和改编，但不得用于商业目的。

## 致谢

感谢[抖音AI夜校][school]、[WaytoAGI][waytoagi]和[周鹏@鲤鱼与鱼ai][zhoupeng]对AI创作学习与方法分享的启发。

完整说明见 [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)。

[school]: https://bytedance.larkoffice.com/wiki/YOE3wLBAHiW74PkXRTpcKJlznQf
[waytoagi]: https://waytoagi.feishu.cn/wiki/QPe5w5g7UisbEkkow8XcDmOpn8e
[zhoupeng]: https://www.douyin.com/user/MS4wLjABAAAAZ5yA9sauF9ETKPvy1mdv4GgSN1ECOzdZeH2i8hKgVyk?from_tab_name=main
