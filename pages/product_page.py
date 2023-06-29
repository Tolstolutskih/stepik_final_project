from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        #self.solve_quiz_and_get_code()
        
    def should_be_product_in_basket_aslert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), "Alert that the product has been added to the basket not found"
    
    def should_be_product_in_basket(self):
        #link =  self.browser.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT).text  ,"Product does not match alert"
        
    def should_be_price_basket(self):
        
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET_ALERT), "Alert that the price to the basket not found"
        assert self.browser.find_element(*ProductPageLocators.PRICE_BASKET_ALERT).text in self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text  ,"Price does not match alert"
        
        

    
        