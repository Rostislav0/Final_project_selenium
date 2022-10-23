from .locators import ProductPageLocators


class ProductPage():
    def __init__(self, browser, page):
        self.name_on_page = None
        self.price_on_page = None
        self.name_in_basket = None
        self.price_in_basket = None
        self.browser = browser
        self.page = page

    def add_to_basket_and_check_that_names_and_prices_equal(self):
        self.name_and_price_product_on_page()
        self.add_to_basket()
        self.name_and_price_product_in_basket()
        self.correct_name_and_price_on_page_and_basket()

    def name_and_price_product_on_page(self):
        self.name_on_page = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_PAGE).text
        self.price_on_page = float(self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_PAGE).text[1:])

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def name_and_price_product_in_basket(self):
        self.name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_BASKET).text
        self.price_in_basket = float(self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_BASKET).text[1:])

    def correct_name_and_price_on_page_and_basket(self):
        assert self.name_on_page == self.name_in_basket, 'Names on page and in basket are difference'
        assert self.price_on_page == self.price_in_basket, 'Price on page and in basket are difference'

    def should_not_be_success_message(self):
        assert self.page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.page.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappear, but should be"
