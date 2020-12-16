import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login():
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False



