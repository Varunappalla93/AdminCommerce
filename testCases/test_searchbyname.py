import time
import pytest
from pageObjects.loginpageObjects import Loginpage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCust
from Utilities.readProperties import readConfig
from Utilities.CustomLogger import Loggen

class Test_SearchCustomerByName_005:
    baseURL = readConfig.getappurl()
    username = readConfig.getuserid()
    password = readConfig.getuserpwd()
    logger = Loggen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCust(self.driver)
        searchcust.setFirstname("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchbyname("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
