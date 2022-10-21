from .locators import MainPageLocators


class ProductPage():
    def __init__(self, browser, page):
        self.name_on_page = None
        self.price_on_page = None
        self.name_in_basket = None
        self.price_in_basket = None
        self.browser = browser
        self.page = page

    def all(self):
        self.name_and_price_product_on_page()
        self.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.name_and_price_product_in_basket()
        self.correct_name_and_price_on_page_and_basket()

    def name_and_price_product_on_page(self):
        self.name_on_page = self.browser.find_element(*MainPageLocators.NAME_OF_PRODUCT_PAGE).text
        self.price_on_page = float(self.browser.find_element(*MainPageLocators.PRICE_OF_PRODUCT_PAGE).text[1:])

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def name_and_price_product_in_basket(self):
        self.name_in_basket = self.browser.find_element(*MainPageLocators.NAME_OF_PRODUCT_BASKET).text
        self.price_in_basket = float(self.browser.find_element(*MainPageLocators.PRICE_OF_PRODUCT_BASKET).text[1:])

    def correct_name_and_price_on_page_and_basket(self):
        assert self.name_on_page == self.name_in_basket, 'Names on page and in basket are difference'
        assert self.price_on_page == self.price_in_basket, 'Price on page and in basket are difference'
