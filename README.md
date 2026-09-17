# Pose Atlas Skill v0.5.0

单人姿势导演 Skill，包含 480 个 Canonical Pose Family 与 1440 个 Variant，提供两个自动路由：

- **输入 Pose ID**：读取该 Canonical 或 Variant 的完整身体结构。
- **未输入 Pose ID**：根据主题、服装、场景、镜头、身材结构与活动能力，自由原创 6–8 个姿势。

主题原创推荐不会检索或引用姿势库，也不会输出图页、页码、图片路径或 `library_ref`。

## 最重要的规则

- `data/poses.json` 是 Canonical Pose ID 的唯一标准，仅在用户明确输入 ID 时读取。
- `data/variants.json` 仅用于 Variant ID 查询；Variant 只能覆盖 arm、hand、head、gaze。
- 原创 `NEW-*` 仅是当前推荐的临时编号，不能写入或冒充正式 Pose ID。
- 姿势描述以 Support、Legs、Weight、Pelvis、Torso、Shoulders、Arms/Hands、Head/Gaze、Shape 为核心。

## 核心文件

- `SKILL.md`：唯一 Skill 入口和路由规则。
- `data/poses.json`：Canonical Pose ID 的标准定义。
- `data/variants.json`：A/B/C Variant 覆盖定义。
- `data/arms.yaml`、`data/hands.yaml`、`data/heads.yaml`、`data/gaze.yaml`：ID 查询时的末端结构词典。
- `docs/ID_AND_VARIANT_RULES.md`、`docs/POSE_GRAMMAR.md`：库维护与身体语法说明。

## 保留的图库资产

项目仍保留图鉴页、目录数据、Viewer 与相关工具，供图库维护和人工浏览使用；它们不参与 Skill 的推荐或查询输出。

## v0.5.0 更新

- 合并原先的 Recommender 与 Pose Director 为根目录唯一入口。
- 主题推荐改为完全原创，不再使用 library / adapted / generated 三种推荐策略。
- 新增 ID 优先路由，支持 Canonical 与 Variant 的完整结构查询。
- 从 Skill 输出移除全部图页字段。
- 删除旧 director、主题预设和库内推荐实现。
