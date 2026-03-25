# 杖剑传说小助手

基于 `MaaFramework` 的《杖剑传说》自动化项目，当前以 `MXU` 作为通用图形界面进行联调与运行。

## 项目简介

`杖剑传说小助手` 面向《杖剑传说》游戏场景，目标是沉淀一套可维护、可扩展、可视化调试的自动化工程。

当前仓库已经完成了项目基础骨架，包括：

- `interface.json` 与多语言描述
- `assets/resource` 资源目录与 Pipeline 目录
- `maafw` 运行库目录
- `reference/MXU` 调试用 GUI
- 最小可用的“启动游戏”任务链

后续会继续围绕《杖剑传说》的启动、登录、通用弹窗处理和日常任务进行迭代。

## 技术方案

本项目的核心组成如下：

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)：自动化黑盒测试框架，负责图像识别、任务调度、控制器接入与资源加载。
- [MXU](https://github.com/MistEO/MXU)：基于 Tauri + React + TypeScript 的通用 GUI，用于加载 `interface.json`、管理任务、连接设备和查看日志。
- `Project Interface v2`：通过 `interface.json` 声明控制器、资源、任务与多语言信息，使项目可以被 MXU 直接识别和运行。

这意味着《杖剑传说小助手》本身主要聚焦于：

- 游戏资源组织
- Pipeline 编排
- 识别与动作逻辑
- 项目级运行配置

而底层能力与通用界面分别由 MaaFramework 与 MXU 提供。

## 当前目录

```text
MaaZJCS/
├─ interface.json
├─ interface_zh.json
├─ maafw/
├─ assets/
│  └─ resource/
│     ├─ image/
│     ├─ model/
│     └─ pipeline/
├─ agent/
├─ config/
├─ debug/
└─ reference/
   └─ MXU/
```

## 快速开始

### 1. 准备运行环境

- 准备 `maafw` 运行库
- 准备安卓设备或模拟器，并确保 `ADB` 可用
- 准备《杖剑传说》安装包，并确认包名正确

### 2. 启动 MXU

开发调试阶段，可在 `reference/MXU` 下运行：

```powershell
pnpm tauri dev
```

如果是本项目联调环境，需确保 `MXU_PROJECT_ROOT` 指向当前项目根目录。

### 3. 在 MXU 中加载项目

MXU 启动后，应能识别当前项目的：

- 控制器：`安卓端`
- 资源：`官服`
- 任务：`启动游戏`

当前最小链路已支持直接启动《杖剑传说》客户端，用于验证工程接入、资源加载、设备连接与任务投递是否正常。

## 已接入组件说明

### MaaFramework

[MaaFramework](https://github.com/MaaXYZ/MaaFramework) 是本项目的自动化核心引擎，提供：

- 控制器能力，如 `Adb`、`Win32`、`PlayCover`、`Gamepad`
- 资源加载与任务执行
- Pipeline 低代码协议
- 自定义识别与自定义动作扩展能力

本项目并不重新发明底层自动化框架，而是在 MaaFramework 之上实现《杖剑传说》专属逻辑。更多说明可参考其官方仓库：[MaaFramework](https://github.com/MaaXYZ/MaaFramework)。

### MXU

[MXU](https://github.com/MistEO/MXU) 是本项目当前采用的通用 GUI，负责：

- 解析 `interface.json`
- 连接设备并管理实例
- 选择资源和任务
- 展示日志与截图
- 作为联调阶段的主要桌面入口

本仓库中保留了 `reference/MXU` 作为调试和适配参考。更多说明可参考其官方仓库：[MXU](https://github.com/MistEO/MXU)。

## 开源许可

本仓库当前附带的根级 `LICENSE.md` 为 `LGPL-3.0`。

同时，本项目在开发与运行过程中引入或参考了以下开源组件，其许可证需分别遵守：

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)：`LGPL-3.0`
- [MXU](https://github.com/MistEO/MXU)：`AGPL-3.0`

如果你分发了包含修改版 `MXU` 的完整桌面程序，或基于其代码继续发布衍生版本，需要额外留意 `AGPL-3.0` 的源码公开义务与分发要求。

## 免责声明

本项目仅用于合法合规的自动化测试、项目研究与工程实践。

使用者应自行确认其使用方式符合相关法律法规、平台规则与目标软件服务条款，并自行承担由此带来的风险与责任。

## 鸣谢

感谢以下开源项目为本项目提供基础能力或工程参考：

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)
- [MXU](https://github.com/MistEO/MXU)
- [MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)
