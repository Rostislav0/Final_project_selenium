from .locators import LoginPageLocators


class LoginPage():
    def __init__(self, browser, url):
        self.browser = browser
        self.current_url = url

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.current_url, f'"login" is not in url({self.current_url})'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'Form login not found'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'Form register not found'
