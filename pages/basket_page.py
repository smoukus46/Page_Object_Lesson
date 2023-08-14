from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import Locators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
       assert self.is_not_element_present(*Locators.BUY)
       assert self.browser.find_element(*Locators.TXT3).text in "Your basket is empty."