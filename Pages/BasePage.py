from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def typeText_action(self,elementName, inputValue):
        WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).send_keys(inputValue)

    def clickable_action(self,elementName):
        WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).click()

    def get_elementText(self,elementName):
        return WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).text

    def elementEnabledStatus(self,elementName):
        return WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).is_enabled()

    def elementDisplayedStatus(self,elementName):
        return WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).is_displayed()

    def get_element_text(self,elementName):
        """Get the current page title with a wait"""
        return WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(elementName)).text


