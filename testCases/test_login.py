import pytest
from selenium import webdriver
from Utilities.readProperties import readConfig
from pageObjects.loginpageObjects import Loginpage
from Utilities.CustomLogger import Loggen

class Test01_login:
    url = readConfig.getappurl()
    uid = readConfig.getuserid()
    pwd = readConfig.getuserpwd()
    logger=Loggen.loggen()

    @pytest.mark.sanity
    def test_launch(self,setup):
        self.logger.info('******TC001********')
        self.logger.info('*****Login Page********')
        self.driver = setup
        self.logger.info('******opening URL******')
        self.driver.get(self.url)
        acttitle=self.driver.title
        self.logger.info('****Title test passed')
        if acttitle=='Your store. Login':
            assert True
        else:
            self.logger.info('*****Title test failed*******')
            self.driver.save_screenshot("C:\\Users\\admin\\E-ComHybridFrm2020\\Screenshots\\"+"Loginpage.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp=Loginpage(self.driver)
        self.lp.setusername(self.uid)
        self.lp.setpassword(self.pwd)
        self.lp.login()
        acttitle1=self.driver.title
        if acttitle1=='Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\admin\\E-ComHybridFrm2020\\Screenshots\\" + "Home.png")
            assert False
        #self.lp.logout()
