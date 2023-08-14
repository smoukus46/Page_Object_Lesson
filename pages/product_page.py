from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import Locators
from .locators import MainPageLocators


import math


class PageObject(BasePage):
    def add_to_basket(self,timeout=5):
        bskt=self.browser.find_element(*Locators.BSKT)
        bskt.click()    


    def compare(self):
        text1=self.browser.find_element(*Locators.TXT)
        text2=self.browser.find_element(*Locators.TXT2)
        assert text1.text == text2.text
   
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*Locators.SUC), \
       "Success message is presented, but should not be"
         
    def should_disappeared(self):
        assert self.is_disappeared(*Locators.SUC),\
        "Success message is not disappeared"
        
    def go_to_login(self):
        login=self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login.click()