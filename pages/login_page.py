from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"{self.browser.current_url} does not contain login" 
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"login form not found" 

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), f"registration form not found"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REG_FORM)
        login.send_keys(email)

        ps = self.browser.find_element(*LoginPageLocators.REG_PASS_FORM)
        ps.send_keys(password)

        psc = self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM_FORM)
        psc.send_keys(password)

        rb = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        rb.click()

