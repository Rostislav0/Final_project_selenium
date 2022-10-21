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
