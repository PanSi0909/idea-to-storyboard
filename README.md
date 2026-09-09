# idea-to-storyboard｜一键式短片分镜

把一句短片想法，经苏格拉底追问、8句话故事、故事设计卡、逻辑核查、150秒七拍和一致性设计，整理成可执行的文字分镜表。

> 核心观念：短片不是压缩长片，而是放大一次选择。

## 适合谁

- 第一次写2—3分钟短片，不熟悉剧本或分镜术语的人。
- 已有一句想法、零散片段、故事卡、剧本或旧分镜，希望继续完善的人。
- 希望保留自己故事核心，只让AI协助提问、整理和检查的人。

你不需要先学会“反向选择”“英雄镜头”或“景别”。只要说出一个想法，Skill 会在必要时询问1—3个关键问题。

## 它会交付什么

- 核心表达、8句话故事和故事设计卡
- 逻辑核查与不可改动核心
- 150秒七拍结构
- 角色与场景一致性卡
- 10秒英雄镜头
- 150秒八列分镜表
- 信息密度、阻碍升级、时长与一致性验收

它生成的是**故事设计和文字分镜**，不会自动拍摄、剪辑或生成最终视频。

## 30秒安装：推荐方式

你需要 Codex 桌面版、Codex CLI 或 Codex IDE 扩展，并能够访问 GitHub。不需要安装 GitHub CLI、Python 或视频剪辑软件。

第一步，在 Codex 中输入：

```text
$skill-installer
```

第二步，发送下面这段话：

```text
请安装这个 GitHub Skill：
https://github.com/PanSi0909/idea-to-storyboard/tree/main/skill/idea-to-storyboard
```

安装器提示完成后，新开一个对话。如果没有看到 Skill，请重启 Codex。

![使用 Skill Installer 安装](docs/images/00-install.svg)

## 确认安装成功

1. 在 Codex 中输入 `/skills`，或在输入框中键入 `$`。
2. 查找 `idea-to-storyboard` 或“一键式短片分镜”。
3. 能够选中 `$idea-to-storyboard`，即表示安装成功。

![检查并调用 Skill](docs/images/00-verify.svg)

Codex 支持显式调用和自动匹配两种方式。第一次使用时建议显式输入 `$idea-to-storyboard`。详见 [OpenAI Skills 官方文档](https://developers.openai.com/codex/skills)。

## 第一次使用

最简单的输入只有一句：

```text
$idea-to-storyboard 把这个想法做成150秒短片分镜：20年后，人类把情感关系交给AI代理。
```

如果想提供得更完整，可以复制下面的模板：

```text
$idea-to-storyboard

我想做一个约150秒的短片。
主题或作业要求：
我的初步想法：
我最不希望被改变的内容：
已有材料：没有／故事片段／故事卡／剧本／文档链接
```

![从一句想法开始](docs/images/01-start.svg)

## 接下来会发生什么

1. Codex 判断你的素材已经完成到哪一步。
2. 信息不足时，Skill 只追问会改变故事方向的1—3个问题。
3. Skill 整理8句话故事和故事设计卡，并锁定内在问题、错误办法、关键选择、英雄镜头和结尾余味。
4. 你确认后，它继续生成150秒结构、角色场景卡和完整分镜。

![六步创作流程](docs/images/02-workflow.svg)

继续拆分镜头前，Skill 会明确锁定五项故事核心。发现冲突时先指出问题；未经确认，不擅自改变。

![锁定核心五项](docs/images/03-core-lock.svg)

最终分镜会逐镜列出时间、场景、单一情绪任务、画面动作、景别机位运镜、声音台词和功能标记。

![检查分镜并按授权同步](docs/images/04-output.svg)

想快速了解一次完整对话，请看 [小白案例导读](docs/BEGINNER-GUIDE.md)；完整成品见原创示例案例 [《那只歪船》](examples/the-crooked-boat.md)。

## 外部文档兼容性

作者本人使用飞书，因此部分开发过程和示例最初在飞书中完成。但本 Skill 的创作流程不依赖飞书，也不限定文档平台。

用户可以提供在线文档链接、Word、Markdown、PDF 或其他可读取的内容。默认结果直接在对话中输出；只有用户明确要求，且当前环境具备对应平台的连接能力时，才会写回外部文档。无法直接写入时，Skill 会输出可复制或导入的 Markdown。

## 手动安装：备用方式

如果当前 Codex 中没有 `$skill-installer`：

1. 在 GitHub 点击 `Code` → `Download ZIP`，然后解压。
2. 找到解压目录中的 `skill/idea-to-storyboard` 文件夹。
3. 把该文件夹复制到个人 Skills 目录：
   - macOS／Linux：`$HOME/.agents/skills/idea-to-storyboard`
   - Windows：`%USERPROFILE%\.agents\skills\idea-to-storyboard`
4. 确认最终路径下直接存在 `SKILL.md`，不要多套一层同名文件夹。
5. 重启 Codex，再用 `/skills` 检查。

`dist/idea-to-storyboard.skill` 是校验过的分发压缩包，不是所有客户端都支持双击安装；小白优先使用 `$skill-installer`。

## 常见问题

**输入 `$idea-to-storyboard` 没有出现 Skill？** 先用 `/skills` 检查；若刚完成安装，重启 Codex。

**安装器提示目标已经存在？** 不要直接删除原文件。先备份已有版本，再更新或重新安装。

**只提供一句想法可以吗？** 可以。Skill 会补问真正影响故事方向的内容。

**它会直接修改我的在线文档吗？** 不会。只有你明确授权具体文档，且当前环境支持写入时才会修改。

**它能直接生成视频吗？** 不能。当前交付是故事卡、结构和文字分镜。

## 仓库结构

```text
idea-to-storyboard/
├── skill/idea-to-storyboard/   # 可安装的 Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── docs/                       # 小白指南和教程图片
├── examples/                   # 原创完整案例
├── dist/                       # .skill 包和校验和
├── SECURITY.md
└── ACKNOWLEDGEMENTS.md
```

## 致谢

感谢 **抖音AI夜校**、**WaytoAGI**、**周鹏@鲤鱼与鱼ai** 对AI创作学习与方法分享的启发。
