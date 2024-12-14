import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Configurations.TestData import TestData
from pathlib import Path
import pytest
import allure

@pytest.mark.usefixtures('setup_and_teardown')
class Test_Login():

    customer_login_txt_xpath = (By.XPATH, "//h1[@class='page-title']/span")

    @allure.title("TestCase#1 to check a URL is landing correct URL!")
    def test_loginPageTitle(self):
        lp = LoginPage(self.driver)
        pageTitle = lp.get_page_title()
        print("pageTtile=>\t", pageTitle)
        self.driver.save_screenshot("screenshot1.png")
        time.sleep(3)

        element = self.driver.find_element(*self.customer_login_txt_xpath)
        element.screenshot("element.png")
        assert "Customer Login" in pageTitle, "Not a valid Page"

    @allure.title("TestCase#2 to test successfull login for valid username and password!")
    def test_successfull_login(self):
        login_page = LoginPage(self.driver)
        login_page.loginToApp(TestData.USERNAME,TestData.PASSWORD)
        time.sleep(3)
        my_accountTxt = login_page.my_account_text()
        assert "My Account" in my_accountTxt, "not success the Login!"
        time.sleep(3)

    @allure.title("TestCase#3 to test successfull login for invalid username and password!")
    def test_with_invalid_username_negative_(self):
        login_page = LoginPage(self.driver)
        login_page.loginToApp("test@gmail.com", TestData.PASSWORD)
        time.sleep(3)
        #my_accountTxt = login_page.my_account_text()
        alert_message_xpath = "//div[@role='alert']//div[contains(@class, 'message-error')]//div"
        alert_element = self.driver.find_element(By.XPATH, alert_message_xpath)

        # Extract and print the text
        login_error_message = alert_element.text

        expected_error_message = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

        assert login_error_message in expected_error_message, "not success the Login!"
        time.sleep(3)





    