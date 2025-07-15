from selenium.webdriver.common.by import By

from pageObjects.checkout_confirm import checkout_confirm
from utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shopCart = (By.XPATH, "//a[contains(@href, 'shop')]")
        self.productCards = (By.XPATH, "//div[@class= 'card h-100']")
        self.cart_checkout_button = (By.CSS_SELECTOR, "a[class*= 'btn-primary']")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shopCart).click()
        products = self.driver.find_elements(*self.productCards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def cart(self):
        self.driver.find_element(*self.cart_checkout_button).click()

        Checkout_Confirmation = checkout_confirm(self.driver)
        return Checkout_Confirmation
