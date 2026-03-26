# 杖剑传说任务迁移清单

## 第一期开工范围

已纳入最小启动骨架的能力：

- 启动游戏（含公告/点屏进游戏）
- 家园小推车（领取 + 升级）

对应落点：

- `interface.json`
- `assets/resource/pipeline/startup.json`
- `assets/resource/pipeline/daily.json`（仅 `DailyHandcart*` 链）
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

1. 将 `startUp.py` 的登录、回首页、公告关闭继续细化到 `startup.json`（如需单独通用弹窗链可再建 pipeline 文件）
2. 将 `daily.py` 的邮件领取、每日商店、每日签到等挂入 `daily.json` 新入口
3. 将 `baseUtils.py` 中无法直接用内建 Pipeline 表达的复杂逻辑迁入 `agent/`
