from .locators import BasketPageLocators


class BasketPage():
    def __init__(self, browser, page):
        self.browser = browser
        self.page = page

    def is_basket_empty(self):
        self.basket_has_not_products()
        self.basket_has_text_about_it_empty()

    def basket_has_not_products(self):
        assert self.page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Basket has any product'

    def basket_has_text_about_it_empty(self):
        assert self.page.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            'Basket has not text about it empty'
