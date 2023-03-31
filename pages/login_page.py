from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url
        assert "login" in current_link, f"expected login to be substring of '{current_link}'"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form link is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Register form link is not presented"
        assert True

    def register_new_user(self, email, password):
        link_email = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        link_email.send_keys(email)
        link_pass = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK)
        link_pass.send_keys(password)
        link_conf_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_LINK)
        link_conf_pass.send_keys(password)
        link_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_LINK)
        link_register.click()
