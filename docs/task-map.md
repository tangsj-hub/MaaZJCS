# 杖剑传说任务迁移清单

## 第一期开工范围

已纳入最小启动骨架的能力：

- 启动游戏
- 识别登录页
- 识别首页
- 关闭常见弹窗
- 日常骨架入口

对应落点：

- `interface.json`
- `assets/resource/pipeline/common.json`
- `assets/resource/pipeline/startup.json`
- `assets/resource/pipeline/daily.json`
- `agent/main.py`

## 暂缓到后续阶段

以下能力不纳入第一期骨架实现：

- 邮件领取
- 每日商店
- 每日签到
- 主线探索
- 副本
- 公会
- 角色养成
- 多账号
- 战斗控制
- 世界聊天解析

## 参考来源

第一期拆分主要参考以下旧脚本：

- `reference/ASZJCS/startUp.py`
- `reference/ASZJCS/daily.py`
- `reference/ASZJCS/baseUtils.py`

## 后续迁移建议

优先级建议如下：

1. 将 `startUp.py` 的登录、回首页、公告关闭拆入 `startup.json` 和 `common.json`
2. 将 `daily.py` 的邮件领取、每日商店、每日签到逐步替换 `daily.json` 中的占位节点
3. 将 `baseUtils.py` 中无法直接用内建 Pipeline 表达的复杂逻辑迁入 `agent/`
