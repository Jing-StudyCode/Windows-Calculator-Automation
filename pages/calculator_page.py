import time

from appium.webdriver.common.appiumby import AppiumBy


class CalculatorPage:
    def __init__(self,driver):
        self.driver = driver
    def click_number(self,number_id):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,number_id).click()
    def click_operator(self,operator_id):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,operator_id).click()
    def click_equal(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"equalButton").click()
    def get_result(self):
        time.sleep(1)
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"CalculatorResults").text


