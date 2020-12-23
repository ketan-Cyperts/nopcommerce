import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
import logging
# logging.basicConfig(filename="./Logs.log", format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
#
# logging.info("Ketan")

class Test_001_Login:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("*********Test_001_Login*********")
        self.logger.info("*********test_homePageTitle Started*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("*********test_homePageTitle Test is Passed*********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*********test_homePageTitle Test is Failed*********")
            assert False

    def test_login(self, setup):
        self.logger.info("*********test_login Started*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*********test_login Test is Passed*********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("*********test_login Test is Failed*********")
            assert False



