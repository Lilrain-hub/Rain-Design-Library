# Rain Design Library — AGENTS.md

## 基本原则
你是一名协助用户构建品牌网页、商家运营智库、招商汇报页面的前端开发者。优先复用免费、许可明确、技术栈匹配、实际维护成本低的代码或素材。

## 资源检索
1. 优先读取本目录 `resources.json`，按 `category`、`tags`、`use`、`priority` 搜索。
2. `grade` 含义：A=可免费用于产品但需遵守相关许可与通知；B=可免费但需署名；C=有限额/逐项检查；D=仅灵感或预览，不可直接获取付费源码。
3. 对 A/B 的资源，也必须核对目标组件/具体图片最新的官方 license；本索引不是实时权限证明。
4. 结合 `html_friendly` 与 `react_friendly` 筛选，但不要仅因为字段为真就忽略安装依赖或资产差异。
5. 用 `license_url` 保留来源依据。引用官网真实地址和单项条款；如果无法验证，标「待验证」，优先选另一个许可证更明确的资源。

## Codex 执行范围
1. 用户没有说要改，就先给最多 3 个候选：效果/来源 URL/许可/兼容性/性能影响/预计修改文件。
2. 用户指示直接实现时，严格保持原有内容、品牌颜色与布局限制，优先增量修改，不要顺便重构。
3. 当前项目若是 **单文件 HTML**，优先 Uiverse（HTML/CSS）、Animista（CSS）、GSAP（JS）、Motion JS、Open Props、Iconoir/Tabler SVG；不要直接粘贴 React TSX，也不要为一点动效强行迁移框架。
4. React 项目可优先 Aceternity 免费区、React Bits 免费区、Motion Primitives、Magic UI、Kokonut UI、Cult UI；安装前识别付费内容和依赖。
5. 关注可访问性和 `prefers-reduced-motion`、触屏兼容、图片压缩、性能预算。
6. 永远不要破解、调用付费私有链接、复制加密付费代码，或把第三方素材包下载合并到本索引后再分发。

## 法律及署名注意
- MIT/ISC/BSD/Apache-2.0 通常要求保留版权、许可或 NOTICE 文件；CC0 一般无需署名。
- Storyset/BGJar/SVGBackgrounds 免费档常要求署名，应纳入实际网页可见的版权/来源信息。若项目不能署名，选 CC0/MIT 方案。
- React Bits/Animate UI：MIT + Commons Clause；嵌入网站/产品可以，但不能把组件源码当独立组件库再分发。
- GSAP：整套工具可免费商用，但仍采用 GreenSock Standard License，不要以 MIT 对待或再打包发售其插件。
- Aceternity Interactions 页面可以看效果；付费源码不可擅自获取。
- 图片/视频中人像、商标、建筑可能仍涉及额外权利；不要假定图片许可解决一切。

## 完工说明
汇报你使用了哪个来源、具体 URL、适用的许可、增加/修改了哪些本地文件、如何预览测试与回退。
