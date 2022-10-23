from .locators import MainPageLocators, LoginPageLocators


class LoginPage():
    def __init__(self, browser):
        self.browser = browser
        self.current_url = self.browser.current_url

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.current_url, f'"login" is not in url({self.current_url})'

    def should_be_login_form(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), 'Form login not found'

    def should_be_register_form(self):
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM), 'Form register not found'

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)

        password_form1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM1)
        password_form1.send_keys(password)
        password_form2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM2)
        password_form2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_button.click()
