# Windows Calculator UI Automation

基于 **Python + Appium + Pytest** 的 Windows 桌面应用自动化测试项目。

## 🛠️ 技术栈
- **语言**：Python 3.10+
- **自动化框架**：Appium (NovaWindows Driver)
- **测试框架**：Pytest
- **设计模式**：POM (Page Object Model)
- **测试报告**：pytest-html
- **应用对象**：Windows 系统自带计算器 (UWP 应用)

## 💡 项目背景与难点解决
1. **痛点**：原生 `pywinauto` 在操作 UWP 应用时，`UIA` 后端存在严重的性能问题，`click()` 会卡死，`win32` 后端又无法识别控件。
2. **技术选型**：经过调研，改用 Appium + NovaWindows 驱动，完美支持 UWP 应用的控件树。
3. **成果**：通过 `AccessibilityId` 精准定位元素，实现了自动化点击与断言，并利用 `try...finally` 保证测试环境清理。

## 🚀 框架亮点 (进阶升级)
- **POM 设计模式**：将页面元素定位与测试逻辑分离，代码结构清晰，维护成本极低。
- **数据驱动测试**：利用 `@pytest.mark.parametrize` 实现数据驱动，一份代码即可覆盖加、减、乘等多种测试场景。
- **可视化报告**：集成 `pytest-html`，每次运行自动生成直观的 HTML 测试报告。

## 📂 项目结构
```text
Calc01/
 ├── pages/                  # POM 页面对象层（封装元素定位和操作）
 │   └── calculator_page.py
 ├── report/                 # 测试报告及截图存放目录
 │   └── test_report.png
 ├── test_calc.py            # 测试用例层（数据驱动与断言）
 ├── .gitignore              # Git 忽略规则
 └── README.md               # 项目说明文档