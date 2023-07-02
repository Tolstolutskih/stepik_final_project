from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REG_FORM = (By.CSS_SELECTOR, "#id_registration-email") 


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main >:nth-child(1)")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_BASKET_ALERT = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right ")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini >.btn-group > :nth-child(1)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
