from Test.PageElement.swap_element import SwapElement

#SWAP页面元素操作层

class SwapPage:
    def __init__(self,driver):
        self.swap_page = SwapElement(driver)

    def click_tokenlist1(self):
        self.swap_page.find_click_tokenlist1().click()

    def click_tokenlist2(self):
        self.swap_page.find_click_tokenlist2().click()

    def tokenlist1_search(self,token1):
        self.swap_page.find_tokenlist_search1().send_keys(token1)

    def tokenlist2_search(self,token2):
        self.swap_page.find_tokenlist_search2().send_keys(token2)

    def click_USDT(self):
        self.swap_page.find_choose_USDT().click()

    def click_DODO(self):
        self.swap_page.find_choose_DODO().click()

    def input_USDT(self,amount1):
        self.swap_page.find_input_USDT().send_keys(amount1)

    def click_button(self):
        self.swap_page.find_swap_button().click()