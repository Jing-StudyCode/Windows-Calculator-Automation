import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy


def test_calculator_addition():
    options = WindowsOptions()
    options.platform_name = "Windows"
    options.automation_name = "NovaWindows"
    options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    print("\n1 连接Appium服务器")
    driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
    time.sleep(3)
    try:
        print("2 开始点击 1+1=")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"num1Button").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"plusButton").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"num1Button").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"equalButton").click()
        time.sleep(1)
        print("3 开始断言结果")
        result_text = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"CalculatorResults").text
        print(f"屏幕上的结果是:{result_text}")
        assert "2" in result_text, f"计算错误，期望结果包含2，实际是{result_text}"
        print("测试通过！")
    finally:
        print("4 清理现场，关闭计算器")
        driver.quit()


