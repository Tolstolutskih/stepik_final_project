from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_product_in_basket_aslert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), "Alert that the product has been added to the basket not found"
    
    def should_be_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT).text  ,"Product does not match alert"
        
    def should_be_price_basket(self):
        
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET_ALERT), "Alert that the price to the basket not found"
        assert self.browser.find_element(*ProductPageLocators.PRICE_BASKET_ALERT).text in self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text  ,"Price does not match alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
            "Success message has not disappeared "

        