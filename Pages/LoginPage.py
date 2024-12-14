from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.BasePage import BasePage
import time

class LoginPage(BasePage):
    """
    find xpath locators from the web page/site
    """
    textbox_username_xpath = (By.XPATH,"//input[@id='email']")
    textbox_password_xpath = (By.XPATH, "//input[@id='pass']")
    button_signIn_xpath = (By.XPATH,"//button[@id='send2']")
    forgot_password_xpath = (By.XPATH,'//a[@class="action remind"]/span')
    createAccount_xpath = (By.XPATH,"//a[contains(@class,'action create primary')]/span")
    customer_login_my_account_xpath = (By.XPATH,"//h1[@class='page-title']/span")
    customer_login_txt_xpath = (By.XPATH, "//h1[@class='page-title']/span")

    def __init__(self, driver):
        super().__init__(driver)


    def loginToApp(self, username, password):
        BasePage.typeText_action(self, elementName=self.textbox_username_xpath, inputValue=username)
        BasePage.typeText_action(self, elementName=self.textbox_password_xpath, inputValue=password)
        BasePage.clickable_action(self, elementName=self.button_signIn_xpath)

    def clickForgotPassword(self):
        BasePage.clickable_action(self, elementName=self.forgot_password_xpath)

    def clickCreateAccount(self):
        BasePage.clickable_action(self, elementName=self.createAccount_xpath)

    def customerLoginTextDisplayed(self):
        BasePage.elementDisplayedStatus(self, elementName=self.customer_login_my_account_xpath)

    def get_page_title(self):
        """Get the current page title with a wait"""
        #return WebDriverWait(self.driver, 12,poll_frequency=0.5).until(ec.visibility_of_element_located(self.customer_login_txt_xpath)).text
        return BasePage.get_element_text(self,elementName=self.customer_login_txt_xpath)

    def my_account_text(self):
        return BasePage.get_element_text(self,elementName=self.customer_login_my_account_xpath)







