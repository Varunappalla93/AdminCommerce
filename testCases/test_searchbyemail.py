import time
import pytest
from pageObjects.loginpageObjects import Loginpage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCust
from Utilities.readProperties import readConfig
from Utilities.CustomLogger import Loggen

class Test_SearchCustomerByEmail_004:
    baseURL = readConfig.getappurl()
    username = readConfig.getuserid()
    password = readConfig.getuserpwd()
    logger = Loggen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        self.searchcust = SearchCust(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status=self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")