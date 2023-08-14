from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import Locators
from .locators import MainPageLocators
from .locators import ProductPageLocators

import math


class PageObject(BasePage):
    def add_to_basket(self,timeout=5):
        bskt=self.browser.find_element(*Locators.BSKT)
        bskt.click()    

    def should_be_correct_price(self):
        product_price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE)
        product_price_value = product_price_page.text

        product_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_price_basket_value = product_price_basket.text[14:-12]  # Выбираю цену путем слайса строки

        assert product_price_value == product_price_basket_value, \
            f"Expeсted price: {product_price_value}. Actual price: {product_price_basket_value}."

        print("Correct price")

    def should_be_correct_name(self):
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE)
        product_name_value = product_name_page.text

        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET)
        product_name_basket_value = product_name_basket.text

        assert product_name_value == product_name_basket_value, \
            f"Expected name: {product_name_value}. Actual name: {product_name_basket_value}."

        print("Correct name")

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