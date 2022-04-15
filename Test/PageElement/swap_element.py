from Base.base import Base

# SWAP页面元素对象层




class SwapElement:
    def __init__(self,driver):
        self.driver = driver
    #点击tokenlist
    def find_click_tokenlist1(self):
        ele = Base.find_element('xpath,//*[@id="root"]/div[1]/div/main/div/div[2]/div[4]/div/div[1]/div/button/span',self.driver)
        return ele

    def find_tokenlist_search1(self):
        ele = Base.find_element('xpath,//input[@placeholder="输入代币简写或合约地址"]',self.driver)
        return ele
    def find_choose_USDT(self):
        ele = Base.find_element('xpath,//span[@title="USDT Token"]',self.driver)
        return ele

    def find_input_USDT(self):
        ele =Base.find_element('xpath,//*[@id="root"]/div[1]/div/main/div/div[2]/div[4]/div/form/div/input',self.driver)
        return ele

    def find_click_tokenlist2(self):
        ele = Base.find_element('xpath,//*[@id="root"]/div[1]/div/main/div/div[2]/div[5]/div/div/div',self.driver)
        return ele

    def find_tokenlist_search2(self):
        ele = Base.find_element('xpath,//input[@placeholder="输入代币简写或合约地址"]',self.driver)
        return ele

    def find_choose_DODO(self):
        ele = Base.find_element('xpath,/html/body/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/span',self.driver)
        return ele
    def find_swap_button(self):
        ele = Base.find_element('xpath,//*[@id="root"]/div[1]/div/main/div/div[2]/div[6]/button[2]',self.driver)
        return ele

