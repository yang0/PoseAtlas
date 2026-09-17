# Standard Pose Image / Contact Sheet Spec v2

## 单张标准 Pose

- 同一成年模特或同一套标准人体参考。
- 简单贴身、非抢眼、中性色服装；手脚和关节走势必须看清。
- 纯净灰/白背景，均匀光。
- Canonical 图优先全身；不裁脚、不裁手。
- 表情中性，发型简单，不用复杂道具。
- 图像只是 `poses.json` 的视觉实现，不是编号定义来源。

## 16 宫格图鉴

- 一页严格 16 个姿势，4×4。
- 页清单从 `data/pages.json` 读取；每页不跨类别。
- 每格必须先读取该 ID 在 `data/poses.json` 的 canonical `name_zh + summary + mechanics`。
- 每格底部只放 Pose ID，可加极短中文名但不建议。
- 同一页人物、服装、背景、镜头语言一致。
- 每个姿势需要有足够视觉差异，不能为了对齐版式牺牲身体力学。

## Naming

Canonical: `assets/pose-images/{ID}.webp`
Variant: `assets/variant-images/{ID}/{ID}-A.webp`
Sheet: `assets/contact-sheets/{CATEGORY}-{PAGE:02d}.webp`
