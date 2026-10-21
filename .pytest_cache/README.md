# Windows Calculator UI Automation

基于 **Python + Appium + NovaWindows** 的 Windows 桌面应用自动化测试项目。

## 🛠️ 技术栈
- 语言：Python 3.10+
- 自动化框架：Appium (NovaWindows Driver)
- 测试框架：Pytest
- 应用对象：Windows 系统自带计算器 (UWP 应用)

## 💡 项目背景与难点解决
1. **痛点**：原生 `pywinauto` 在操作 UWP 应用时，`UIA` 后端存在严重的性能问题，`click()` 会卡死，`win32` 后端又无法识别控件。
2. **技术选型**：经过调研，改用 Appium + NovaWindows 驱动，完美支持 UWP 应用的控件树。
3. **成果**：通过 `AccessibilityId` 精准定位元素，实现了自动化点击与断言，单次用例执行时间控制在 10 秒内。

## 🚀 如何运行
1. 启动 Appium 服务器：
   ```bash
   appium --use-plugins=inspector