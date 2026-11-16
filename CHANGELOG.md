# 更新记录

## 2026-11-16 · 每周资源维护

收录 6 个资源，目录从 51 条增至 57 条。R52–R54 为上周待入库项目，本次重新核对官方许可。

- 新增 R52 [Reka UI](https://www.reka-ui.com/docs/overview/introduction)。无样式菜单、弹窗和表单控件，提供键盘操作和焦点管理。
- 新增 R53 [Floating UI](https://floating-ui.com/docs/getting-started)。让提示框和菜单贴合触发元素并避开视口边缘。React 包另提供交互 Hooks。
- 新增 R54 [React Aria Components](https://react-aria.adobe.com/getting-started)。提供带键盘操作的日期选择器、组合框和表格，可用 CSS 或 Tailwind 定制。
- 新增 R55 [Web Awesome · Core](https://webawesome.com/docs/)。Shoelace 的后续项目，免费 Core 提供按钮、选择框和浮层。Pro 的日期选择器、图表和 Figma 套件另行授权。
- 新增 R56 [Anime.js](https://animejs.com/documentation/getting-started/installation)。支持属性补间和时间线，可给现有网页加标题、按钮和 SVG 动效。
- 新增 R57 [PhotoSwipe](https://photoswipe.com/getting-started/)。从缩略图打开全屏灯箱，支持大图缩放和手势。接入时保留原图链接，并使用有授权的图片。
- 复核 R39 LottieFiles，修正免费动画及其衍生版本的许可保留和分发条件。
- 复核 R41 GSAP，补充标准许可的商用范围、竞争性无代码动画工具限制和声明要求。
- 11 月 2 日版本于 11 月 9 日上线，线上网页及 JSON 已核验。

## 2026-11-02 · 每周资源维护

- 新增 R49 [Bulma](https://bulma.io/)：免费 MIT CSS 框架，记录无必需 JavaScript、交互自备及全局样式影响。
- 新增 R50 [Splide · Free Core](https://splidejs.com/)：MIT 轮播核心，记录 JS / CSS 初始化及框架集成；赞助专享 Premium Shader Carousel 不纳入免费范围。
- 新增 R51 [Swiper · Free Core](https://swiperjs.com/)：MIT 触屏轮播核心，记录模块和样式依赖；Studio 服务、UI Initiative Premium 模板与效果另行授权。
- 目录从 48 条增至 51 条；读取三项官方许可及免费范围页面，证据写入 reviews.json。按项目身份去重，不将框架适配包单独计数。
- 复核 R28 Phosphor Icons、R37 Open Props，均保持 MIT；更新 Phosphor 许可链接至本轮实际读取的 core LICENSE。
- Pico CSS 许可明确但官方已停止维护，暂存候选；CSS Loaders 仍待许可核验。候选总计 2 项。
- 远端起点为 5a6ef82b562f367830186801d677f1745607cc27，本轮开始时无其他新增提交。原有记录与 legacy_ids 保留。
- 修正页面运行时覆盖“本次新增”数量的旧逻辑：本周应显示 +3，而非历史累计差值 +36。数量由 catalog-meta.json 生成。
- 同步数据、README、CSV、HTML 与更新日期；在线发布仅在实际网页和 JSON 核验后记录到 publish-config.json。
- 本轮本地校验通过，预览已确认轮播搜索与 HTML 筛选。浏览器标签页接口超时，原生上传页持续无法读取正文，未上传或提交；本地待发布 51 条，远端最后确认仍为 48 条。待发布清单与原因已写入 publish-config.json，不覆盖上次成功发布信息。

## 2026-10-28 · 首次执行每周维护

- 新增 R46 [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)：代码 MIT，文档 CC BY 3.0；记录全局样式和可选 JS / Popper 依赖。
- 新增 R47 [Headless UI](https://headlessui.com/)：MIT，无样式 React / Vue 交互组件；记录框架与样式需求。
- 新增 R48 [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)：MIT，React 无样式交互基础；记录可访问性和安装边界。
- 逐项读取官方许可证，为新增资源保存核验日期、使用条件与来源。目录从 45 条增至 48 条。
- 复核 R07 shadcn/ui（MIT）、R08 Lucide（ISC，部分 Feather 衍生图标另有 MIT）；补充 Lucide 的混合许可说明。
- CSS Loaders 暂留 candidates.json：本轮未找到明确可验证的官方许可，不纳入已确认免费目录。
- 数据、CSV 与网页已同步；在线发布结果以实际 GitHub / Pages 核验及 publish-config.json 为准。

## 2026-10-26

- 从本地 v2.0 导入 45 条原有资源索引，保留现有分类与使用规范。
- 新增数据同步与校验脚本；JSON 为内容来源，CSV 与离线网页由脚本同步。
- 为后续每周收集增加授权核查记录和待审核候选清单。
- 原有 45 条记录未在本次准备发布时逐项重新核验，不代表本周核验通过。
- GitHub 仓库创建及 Pages 发布状态以 publish-config.json 和实际线上验证为准。
