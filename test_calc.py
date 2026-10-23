import time

import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

from Pages.calculator_page import CalculatorPage

test_data = [("num1Button","plusButton","num1Button","2","1+1=2"),
             ("num2Button","plusButton","num3Button","5","2+3=5"),
             ("num9Button","minusButton","num4Button","5","9-4=5"),
             ("num5Button","multiplyButton","num2Button","10","5*2=10"),
             ]
@pytest.mark.parametrize("num1,operator,num2,expected_result,case_name",test_data)
def test_calculator_operations(num1,operator,num2,expected_result,case_name):
    print(f"\n开始执行用例:{case_name}")
    options = WindowsOptions()
    options.platform_name = "Windows"
    options.automation_name = "NovaWindows"
    options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
    time.sleep(3)
    try:
        calc_page = CalculatorPage(driver)
        calc_page.click_number(num1)
        calc_page.click_operator(operator)
        calc_page.click_number(num2)
        calc_page.click_equal()
        result = calc_page.get_result()
        assert expected_result in result, f"期望包含{expected_result},实际是{result}"
    finally:
        driver.quit()





