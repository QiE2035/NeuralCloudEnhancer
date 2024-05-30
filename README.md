<!-- **| [English](README_en.md) | 简体中文 |** -->

> # 已弃坑！暂不可用！！！

# NeuralCloudEnhancer

NCE(R)，云图进化，少女前线：云图计划的自动化脚本，基于 [ALAS](#关于-alas) 框架

## 关于名字的由来

> **TODO**

## 安装

### 获取源码

NCE(R) 还在开发中，暂时不提供自动安装包，需要以正常流程安装。

Clone 这个项目。

```bash
git clone https://github.com/QiE2035/NeuralCloudEnhancer
```

进入项目目录。

```bash
cd NeuralCloudEnhancer
```

<!--
使用 conda 新建 python 3.10.10 环境，假设新环境的名字叫 `src`。

> 注意：我们不维护更高或者更低版本的依赖，建议使用 3.10.10

```bash
conda create -n src python==3.10.10
```

激活刚刚创建的虚拟环境。

```bash
conda activate src
```
-->

安装 requirements.txt 中的依赖。

```bash
pip install -r requirements.txt
```

> **注意：依赖列表并未完善，后续可能会变更**

### 安装模拟器

<!-- 1. 下载 [ADB](https://developer.android.com/tools/releases/platform-tools) 并配置到环境变量中。 -->

在模拟器里安装游戏，而不是桌面端，建议使用最牛批的 MuMu 12，次选蓝叠模拟器。

> **为什么使用模拟器？** 如果你用桌面端来运行脚本的话，游戏窗口必须保持在前台，我猜你也不想运行脚本的时候不能动鼠标键盘像个傻宝一样坐在那吧，所以用模拟器。

<!-- 
> **模拟器的性能表现如何？** Lme 的 8700k+1080ti 使用 MuMu 12 模拟器画质设置非常高是有 40fps 的，如果你的配置稍微新一点的话，特效最高
> 60fps 不是问题。
-->

## 使用

启动 GUI 后端（默认开在 20305 端口）。

```bash
python gui.py
```

在浏览器访问 <http://127.0.0.1:20305>

在 `NCE设置` - `模拟器设置` - `模拟器Serial` 中按照帮助文本填写。

进入 `总览` 界面，点击 `启动` 按钮。（NCE(R) 将自动启动模拟器和游戏，如果它们没在运行的话，模拟器启动目前只支持 MuMu
系和夜神系模拟器）

保持脚本运行，NCE(R) 将在体力恢复的时候自动登录清体力。建议将 `NCE(R)设置` - `优化设置` - `当任务队列清空后`
设置为 `关闭游戏`
以节省资源。

## 开发

- 开发文档（目录在侧边栏）：[Alas wiki](https://github.com/LmeSzinc/AzurLaneAutoScript/wiki/1.-Start)
  ，但很多内容是新写的，建议阅读源码和历史提交。
- 欢迎提交 PR，挑选你感兴趣的部分进行开发即可。
- assets，参考 [开发文档 “添加一个 Button” 一节](https://github.com/LmeSzinc/AzurLaneAutoScript/wiki/4.1.-Detection-objects#%E6%B7%BB%E5%8A%A0%E4%B8%80%E4%B8%AA-button)。

<!--  **如何添加多语言/多服务器支持？** --> 

## 关于 ALAS

NCE(R) 源头上来说是基于碧蓝航线脚本 [AzurLaneAutoScript](https://github.com/LmeSzinc/AzurLaneAutoScript)
开发，但实际是基于 [StarRailCopilot 这个版本](https://githubfast.com/LmeSzinc/StarRailCopilot/tree/0e1b6578ebb1bfa599b4af618c812c45b548fb13)
魔改而来，主要是本人这学期有 Python 课，加上 ALAS 有更为优秀的调度器，所以本着就当练习的想法，在 [MAA](https://maa.plus/)
和 [ALAS](https://alas.azurlane.cloud/) 中选择了后者。
