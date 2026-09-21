# Python 课程学习项目

这是我的 Python 课程学习仓库，用于保存课堂示例、课后练习和实验项目。
项目目前处于持续学习和补充阶段，代码以练习基础语法和编程思维为主。

## 项目内容

- `cource_source_code/`：课程章节示例代码和综合练习
  - `Chapter01/`：模块导入与基础项目
  - `Chapter02/`：代码格式、变量、数据类型和运算符
  - `Chapter03/`：条件语句、循环语句和跳转语句
  - `Chapter04/`：字符串及其常见操作
  - `Chapter05/`：列表、元组、集合、字典和综合应用
  - `Chapter06/`：函数、作用域和综合程序
  - `Chapter07/`：文件与目录操作
  - `Chapter08/`：类、对象、继承和多态
  - `Chapter09/`：异常处理和自定义异常
  - `Chapter10/`：Python 标准库、第三方库和综合案例
  - `Chapter11/`：小游戏项目
- `exercises/`：课后练习
- `lab/`：课程实验项目
  - `lab01/`：第一个实验
  - `lab02/`：第二个实验
- `license`：项目许可文件

## 环境要求

- Python `3.12` 或更高版本
- Windows、macOS 或 Linux
- 实验项目推荐使用 [uv](https://docs.astral.sh/uv/)

课程示例和练习目前主要使用 Python 内置功能，不需要额外安装第三方依赖。

## 快速开始

### 直接运行课程示例

在项目根目录执行：

```bash
python "cource_source_code/Chapter02/2-3变量和数据类型.py"
```

部分程序需要根据提示输入数据，例如计算器、登录检测和小游戏。

### 运行实验项目

进入对应实验目录后运行：

```bash
cd lab/lab01
uv run python src/main.py
```

运行第二个实验：

```bash
cd lab/lab02
uv run python src/main.py
```

如果不使用 `uv`，也可以直接运行：

```bash
python src/main.py
```

## 学习建议

1. 按 `Chapter01` 到 `Chapter11` 的顺序阅读和运行示例。
2. 先理解示例代码，再独立完成 `exercises/` 中的练习。
3. 修改输入、边界条件和输出格式，观察程序行为的变化。
4. 将多个基础知识点组合起来，逐步完善 `lab/` 中的实验项目。

## 当前状态

项目正在持续更新中。后续会继续补充课堂代码、实验报告、练习答案和项目说明。
