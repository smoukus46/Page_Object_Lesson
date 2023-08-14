from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name=registration_submit]")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class Locators():
    BSKT= (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket ")
    TXT=(By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    TXT2=(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in>.alertinner>strong")
    SUC= (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")
    CHECK_BSKT=(By.CSS_SELECTOR, ".btn-group>.btn.btn-default")
    TXT3=(By.CSS_SELECTOR, "#messages")
    BUY=(By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-block")

class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, " div > h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
  