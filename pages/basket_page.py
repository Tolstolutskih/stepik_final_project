from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_basket_empty_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text == "Your basket is empty. Continue shopping", "No message for empty basket"



