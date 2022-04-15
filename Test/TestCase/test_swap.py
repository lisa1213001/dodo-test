import os
from time import sleep
import pytest
import allure
from selenium import webdriver
from Common.wallet_operate import WalletOperate
from selenium.webdriver.chrome.options import Options
from Common.parse_yaml import parse_yaml
from Common.parse_csv import parse_csv
from Test.PageOperate.swap_page import SwapPage


abs_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file = 'extension_metamask.crx'
extension_path = os.path.join(abs_path, 'Config', file)

#这个路径写成这样是有原因的，因为是从主入口执行测试用例，所以采用的是主入口的相对路径
data = parse_csv('./Data/test_001_swap.csv')

@allure.feature("swap")
class TestSwap:
    def setup_class(self):
        #实例化一个启动参数对象
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--lang=zh-cn")
        chrome_options.add_argument('lang=zh_CN.UTF-8')

        #添加小狐狸插件
        chrome_options.add_extension(extension_path)
        #防止浏览器闪退
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        dodoex_url = parse_yaml('dodoex.yml','website')['url']
        self.driver.implicitly_wait(60)
        self.driver.get(dodoex_url)

        WalletOperate().connectWallet(self.driver)
        WalletOperate().changeMetamaskNetwork(self.driver)


    def teardown_class(self):
        sleep(3)
        #self.driver.quit()
        print("结束")
    @allure.story("输入不超过余额的代币数量")
    @pytest.mark.parametrize(("token1","amount1","token2"),data)
    def test_swap(self,token1,amount1,token2):
        sleep(5)
        SwapPage(self.driver).click_tokenlist1()
        SwapPage(self.driver).tokenlist1_search(token1)
        SwapPage(self.driver).click_USDT()
        
        SwapPage(self.driver).input_USDT(amount1)
        SwapPage(self.driver).click_tokenlist2()
        SwapPage(self.driver).tokenlist2_search(token2)
        SwapPage(self.driver).click_DODO()
        
        SwapPage(self.driver).click_button()
        WalletOperate().transactionFromMetamask(self.driver)


