# Rain Design Library · 免费网页素材资源索引

> **v2.0 · 2026-10-28** · 当前共 **48 个资源入口**，本次周更新增 **3 个**。这是 **网站索引 / 开发指引**，不是第三方源码或图片的打包下载。

## 三步开始（Mac + Codex）

1. 解压 `Rain-Design-Library-v2.zip`，双击 `Rain-Design-Library-v2/index.html` 打开离线目录。
2. 你可以按名称/用途搜索、按分类筛选，并勾选「只看不用付费」或「单文件 HTML 适用」。
3. 把此文件夹放入 Codex 工作区，或在现有项目的对话里给 Codex 其所在路径，告诉它先读 `AGENTS.md` 与 `resources.json`，再推荐免费组件。

## 常用一句话

> 请先阅读 Rain Design Library 的 `AGENTS.md` 与 `resources.json`，从官方免费或许可明确的项目中，推荐 3 个适用于我当前项目的网页组件/素材，分别说明安装方法、单 HTML / React 兼容性和授权条件。不要下载付费资源，不要重构我的页面。

## 内容文件

| 文件 | 用途 |
|---|---|
| `index.html` | 离线搜索 / 分类 / 免费级别 / 单 HTML 筛选，可点击官网或授权链接 |
| `resources.json` | Codex 可检索的结构化记录（当前 48 条） |
| `resources.csv` | Excel / Numbers 可编辑清单 |
| `AGENTS.md` | Codex 使用规则与许可防误用指南 |
| `LICENSE-GUIDE.md` | 免费等级、授权限制说明 |
| `PROMPTS.md` | 可复制的任务提示词 |
| `SCENARIOS.md` | GOSYNC、智库、汇报、单 HTML 的搭配推荐 |
| `ADD-RESOURCE.md` | 添加新网站的标准流程 |

### 免费等级（索引标签而非法务证明）

- A：可免费用于项目（MIT/CC0/ISC、官方免付费等，部分需保留版权许可、限制再分发）
- B：免费但需要公开署名 / 原作者标注
- C：免费额度、部分内容免费、或逐项核对许可后使用
- D：仅灵感/预览，不能直接提取付费源码

**授权不等于版权全部放弃。** 免费可商用并不等于可把素材重新分发、卖成组件库，也不等于可以绕过付费、复制网站整体品牌设计。请以实际组件/素材页面最新许可为准。

## 更新习惯

发现新素材网址，先记录官网和授权，再更新 `resources.json` 与 `resources.csv`，并重新将 JSON 内嵌至 `index.html`。为了离线可用，HTML 不依赖外部 API，不会实时抓取网站内容。

## 每周维护与发布

- 本地维护副本包含数据校验、同步脚本、候选列表和许可核查记录。
- 每周一北京时间 10:00 由当前聊天的定时任务搜索、核验和更新。
- 运行 `python3 update_library.py` 同步 CSV 与离线 HTML，运行 `python3 update_library.py --check` 检查一致性。
- 维护步骤见 [WEEKLY-UPDATE.md](WEEKLY-UPDATE.md)，变更见 [CHANGELOG.md](CHANGELOG.md)。
- 首次导入的 45 条记录沿用原有标注，并未在准备发布时逐项复核；新增记录必须有官方许可证据。
- 在线地址与发布状态见 `publish-config.json`。配置为空或 not_published 表示还未完成首次发布。
- 本地定时更新需要电脑开机、应用运行、网络和发布凭据可用；Pages 只托管最后成功发布的内容。
