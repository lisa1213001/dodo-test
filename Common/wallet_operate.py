import os
from time import sleep
from selenium import webdriver
from Common.parse_yaml import parse_yaml
from Base.base import Base
from selenium.webdriver.chrome.options import Options

extention_id = 'nkbihfbeogaeaoehlefnkodbefgpgknn'



"""
因为我这里已经把驱动地址写到path里了，webdriver.Chrome()就不用传参数了
因为谷歌插件用selenium打开是不会每次保存的，所以每次打开都要重新加载小狐狸插件
整体流程：
填写助记词导入钱包→DODO连接钱包→切换网络（如果不切换默认为主网）/添加再切换网络→ 授权/取消授权→同意交易/取消交易 or 签名
"""


# 按地址读取助记词
def getSeedPhrase(filename,address):
    input_address = address
    mnemonic_list = []
    wallet_address = parse_yaml(filename, 'metamask')['address']
    if wallet_address == address:
        mnemonic_list = parse_yaml(filename, 'metamask')['mnemonic'].split()
        return mnemonic_list

class WalletOperate:



   # 导入助记词完成导入钱包
    def metamaskSetup(self,driver):
       filename = 'wallet.yml'
       address = '0x25729CFE1e39619aca364C236Df6Df04eaa5769F'
       password = parse_yaml(filename, 'metamask')['password']

       # 切换到metamask窗口
       driver.switch_to.window(driver.window_handles[0])
       Base.find_element('xpath,//*[@id="app-content"]/div/div[2]/div/div/div/button',driver).click()
       Base.find_element('xpath,//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button',driver).click()
       Base.find_element('xpath,//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]',driver).click()
       mnemonic_list = getSeedPhrase(filename,address)

       for i in range(12):
           element = Base.find_element('id,import-srp__srp-word-'+str(i),driver)
           element.send_keys(mnemonic_list[i])
       Base.find_element('id,password',driver).send_keys(password)
       Base.find_element('id,confirm-password',driver).send_keys(password)
       Base.find_element('id,create-new-vault__terms-checkbox',driver).click()
       Base.find_element('xpath,//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button',driver).click()
       Base.find_element('xpath,//*[@id="app-content"]/div/div[2]/div/div/button',driver).click()

    # DODO连接钱包
    def connectWallet(self,driver):
        self.metamaskSetup(driver)
        Base.find_element('xpath,//button[text()="下一步"]',driver).click()
        Base.find_element('xpath,//button[text()="连接"]',driver).click()
        Base.find_element('xpath,//*[@id="popover-content"]/div/div/section/header/div/button',driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # 切换网络
    def changeMetamaskNetwork(self,driver,network="Rinkeby 测试网络"):
        """打开一个无标题新窗口，这时候新窗口的句柄下标为1，切换到新窗口
        打开metamask页面，然后就可以进行元素定位切换网路
        以太坊 Ethereum 主网络
        Ropsten 测试网络
        Kovan 测试网络
        Rinkeby 测试网络
        Goerli 测试网络
        """

        #self.connectWallet(driver) 需要先连接钱包
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f'chrome-extension://{extention_id}/home.html')

        Base.find_element('xpath,//span[text()="以太坊 Ethereum 主网络"]',driver).click()
        Base.find_element('xpath,//a[text()="显示/隐藏"]',driver).click()
        Base.find_element('xpath,//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/div/div[1]/div[2]/div',driver).click()
        Base.find_element('xpath,//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/div/div[1]/div[2]/div',driver).click()
        Base.find_element('xpath,//span[text()="以太坊 Ethereum 主网络"]',driver).click()
        Base.find_element(f'xpath,//span[text()="{network}"]',driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        sleep(2)

    # 通过Chainlist切换指定网络
    # add_network 要添加的网络名称 要写全称比如Polygon Mainnet
    def changeNetworkByChainList(self,driver,add_network):
        #self.connectWallet(driver) 需要先连接钱包
        driver.execute_script('window.open();')
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https:///chainlist.org')
        Base.find_element('xpath,//h5[text()="Connect Wallet"]',driver).click()
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(f'chrome-extension://{extention_id}/popup.html')
        Base.find_element('xpath,//button[text()="下一步"]', driver).click()
        Base.find_element('xpath,//button[text()="连接"]', driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        Base.find_element('xpath,//span[text()="Testnets"]', driver).click()
        Base.find_element('xpath,//*[@id="__next"]/div[1]/main/div/div[2]/div[1]/div[1]/div/div/div/input', driver).send_keys(add_network)
        sleep(3)
        Base.find_element('xpath,//span[text()="Add to Metamask"]', driver).click()
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(f'chrome-extension://{extention_id}/popup.html')
        Base.find_element('xpath,//button[text()="批准"]', driver).click()
        Base.find_element('xpath,//button[text()="切换网络"]', driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])




    # 确认/取消授权、交易
    def transactionFromMetamask(self,driver,comfirm="True"):
        sleep(3)
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f'chrome-extension://{extention_id}/popup.html')
        if comfirm == "True":
            Base.find_element('xpath,//button[text()="确认"]', driver).click()
        if comfirm == "False":
            Base.find_element('xpath,//button[text()="拒绝"]', driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # 确认/取消签名
    def confirmSign(self,driver,comfirm="True"):
        sleep(3)
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f'chrome-extension://{extention_id}/popup.html')
        if comfirm == "True":
            Base.find_element('xpath,//button[text()="签名"]', driver).click()
        if comfirm == "False":
            Base.find_element('xpath,//button[text()="取消"]', driver).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

