# 每周更新流程

计划频率：每周一 10:00，Asia/Shanghai。由当前聊天的定时任务执行。

1. 先读取 AGENTS.md、ADD-RESOURCE.md、resources.json、reviews.json 和本文件。
2. 搜索官方组件网站、官方 GitHub 仓库及其更新日志，关注免费 HTML/CSS 组件、React/Vue 组件、动画工具、SVG 图标、插画、背景及字体。目标每次找到 3–8 个值得收录的新入口，允许没有合格新增，不为数量凑条目。
3. 对照现有名称、URL、重定向与同一项目的镜像去重；不把同一库的每个组件都当作独立资源重复加入。
4. 必须打开官方许可证和免费/付费范围页面。确认商业嵌入条件、署名、保留许可要求、源码再分发限制和技术依赖。只有能够提供证据的 A/B 资源直接入库；试用、部分免费但边界不明或条款无法读取的资源记入 candidates.json，并写明阻塞原因。
5. 为新资源分配不重复的 R 编号。在 reviews.json 按编号记录 verified_at（YYYY-MM-DD）、free_scope、license_summary、official_sources（实际读取的官方 URL 数组）。该文件用于记录人工/代理查证的证据；脚本仅检查完整性，不能代替授权判断。
6. 更新 resources.json、catalog-meta.json 的 updated_at / new_count，并追加 CHANGELOG.md。legacy_ids 仅代表 2026-10-26 的历史导入记录，不得将新资源加入以绕过核验。
7. 运行 `python3 update_library.py`，然后 `python3 update_library.py --check`。预览页面，验证新增条目可被搜索、筛选，官网与许可链接正确。遇到失败应修复后再发布。
8. 发布前读取 publish-config.json，确认仓库及 Pages 已创建。同步远端后仅提交本次资源更新，保留他人的修改；不要强制推送。可以使用已授权的 Git 凭据或浏览器上传。没有可用发布凭据时保留本地更新并明确报告，不能宣称线上更新成功。
9. 发布后等待 Pages 完成，读取实际网页及 resources.json，确认新增记录在线可见。只在新增/条款变化/发布完成/失败或需要用户操作时通知；没有可操作变化时保持安静。

## 运行条件

本地定时任务需要电脑开机、应用运行，并能访问网络及本文件夹。GitHub Pages 负责托管，不会自行搜索新资源。电脑离线时在线目录仍展示最后成功发布的版本。

## 首次发布

在 Lilrain-hub 账号下创建公开仓库 Rain-Design-Library，上传本文件夹内容，在 Settings → Pages 选择 Deploy from a branch / main / root。成功后将实际仓库 URL、Pages URL 及状态写入 publish-config.json，再验证线上内容。预期地址不能作为已经发布的证据。
