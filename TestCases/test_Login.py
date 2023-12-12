import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Pages import loginPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Utils.readProperties import ReadConfig


class Test_001_LoginTests:
    url = ReadConfig().getUrl()
    username = ReadConfig().getUserName()
    password = ReadConfig().getPassword()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validlogin(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.hp=HomePage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        product_label = self.driver.find_element(By.XPATH,self.hp.label_product_xpath).text

        if product_label=='Products':
            allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Error", attachment_type=AttachmentType.PNG)
            assert False
        self.driver.quit()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Invalidlogin(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username + "Nkosi")
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        loginerror = self.driver.find_element(By.XPATH,self.lp.label_loginError_xpath).text

        if loginerror=='Epic sadface: Username and password do not match any user in this service':
            allure.attach(self.driver.get_screenshot_as_png(),name="Login Error",attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)

            assert False

        self.driver.quit()
