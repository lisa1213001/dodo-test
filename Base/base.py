from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

"""
对selenium提供的API做了封装
find_element find elements
其他的方法之后补充
"""

# 元素定位的类型
LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
}


class Base:

    def find_element(locator, driver):
        # 返回单个元素
        # locator的格式 'xpath,//*[@id="kw"]'
     name = locator.split(',')[0]
     value = locator.split(',')[1]
     by = LOCATE_MODE[name]
     element = WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((by, value)))
     return element


    def find_all_elements(locator, driver):
        # 返回所有元素对象的列表name,value = locator
        name = locator.split(',')[0]
        value = locator.split(',')[1]
        by = LOCATE_MODE[name]
        elements = WebDriverWait(driver, 30, 1).until(EC.prensence_of_all_elements_located((by, value)))
        return elements

