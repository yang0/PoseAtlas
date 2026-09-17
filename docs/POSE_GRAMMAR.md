# Pose Grammar v2

## Canonical body hierarchy

每个 Pose Family 用以下顺序描述：

1. **Support**：身体与地面/家具/墙面的支撑点。
2. **Legs**：腿部拓扑：站、屈、伸、交叉、前后/左右错位。
3. **Weight**：主要重心和转移方向。
4. **Pelvis**：侧移、倾斜、旋转；决定下段曲线。
5. **Torso**：纵向延展、侧弯、前倾、后伸、扭转。
6. **Shoulders**：肩线与骨盆的互补关系。
7. **Arm / Hand**：大结构和末端动作；默认可做 Variant 覆盖。
8. **Head / Gaze**：默认可覆盖。
9. **Shape**：从画面上最先读到的几何轮廓。
10. **Intensity 1–5**：造型幅度，而不是“好不好看”。

## Family boundary

以下任一项发生显著变化，通常应新建 Family：Support、腿部拓扑、主重心、骨盆/胸腔主关系、主要 Shape。

以下变化通常只做 Variant：手臂、手、头部、视线、轻微脚尖方向、轻微表情。

## Intensity

- 1：几乎自然站/坐，普通客人最容易复现。
- 2：轻微重心与肩胯设计。
- 3：明显造型，有清晰线条但仍适合大多数客人。
- 4：强时装造型，大侧弯/扭转/低位/平衡要求。
- 5：高动态、高柔韧或明显运动瞬间。

## Shape is visual, not emotional

S_CURVE 等 Shape 只描述人体几何，不绑定性感、可爱、高级等情绪。
