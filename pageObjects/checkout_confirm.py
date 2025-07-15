from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import BrowserUtils


class checkout_confirm(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.country_name = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkBox = (By.XPATH, "//div[@class= 'checkbox checkbox-primary']")
        self.Submit_button = (By.CSS_SELECTOR, "input[class*='btn-success']")
        self.alert_Message = (By.CLASS_NAME, "alert-success")

    def checkout(self, ):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery(self, countryName):
        self.driver.find_element(*self.country_name).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkBox).click()
        self.driver.find_element(*self.Submit_button).click()

    def confirm(self):
        successText = self.driver.find_element(*self.alert_Message).text
        assert "Success! Thank you!" in successText
