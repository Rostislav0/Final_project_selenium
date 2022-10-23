from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

    NAME_OF_PRODUCT_PAGE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] > h1")
    PRICE_OF_PRODUCT_PAGE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] > p[class='price_color']")

    NAME_OF_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRICE_OF_PRODUCT_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators():
    EMAIL_FORM = (By.CSS_SELECTOR, "form[id='register_form'] input[type='email']")
    PASSWORD_FORM1 = (By.CSS_SELECTOR, "form[id='register_form']  input[name='registration-password1']")
    PASSWORD_FORM2 = (By.CSS_SELECTOR, "form[id='register_form']  input[name='registration-password2']")

    REGISTER_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")
