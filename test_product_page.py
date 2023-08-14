from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import math
import pytest
import time
from selenium.common.exceptions import TimeoutException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"    
link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(2)
    page.compare()

@pytest.mark.need_review  
def test_guest_can_add_product_to_basket(browser):    
    page=PageObject(browser, link1,timeout=5)
    page.open()
    page.add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code() 
      
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page=PageObject(browser, link,timeout=5)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    page=PageObject(browser, link,timeout=5)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page=PageObject(browser, link,timeout=5)
    page.open()
    page.add_to_basket()
    page.should_disappeared()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page=PageObject(browser, link,timeout=5)
    page.open()
    page.check_basket()
    page.should_be_empty_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page=PageObject(browser, link,timeout=5)
    page.open()
    page.go_to_login()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@supermail.ru"
        password = '123456789Nn'
        loginPage = LoginPage(browser, link,timeout=5)
        loginPage.open()
        loginPage.register_new_user()
        time.sleep(5)
        loginPage.should_be_authorized_user()
        
    def test_user_guest_can_add_product_to_basket(self,browser):
       link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       page=PageObject(browser, link,timeout=5)
       page.open()
       time.sleep(3)
       page.add_to_basket()
       time.sleep(2)
       page.compare()

    def test_user_guest_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page=PageObject(browser, link,timeout=5)
        page.open()
        page.should_not_be_success_message()