from .base_page import BasePage
import time
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .product_page import PageObject

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "url isn't correct"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form input is not presented"
        assert True


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form input is not presented"
        assert True

    def  register_new_user(self,email = str(time.time()) + "@supermail.ru", password = 'kek1337'):
        email = str(time.time()) + "@supermail.ru"
        password = '123456789Nn'
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_REGISTER).click()