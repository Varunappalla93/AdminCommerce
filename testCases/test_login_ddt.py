import pytest
import time
from selenium import webdriver
from Utilities.readProperties import readConfig
from pageObjects.loginpageObjects import Loginpage
from Utilities.CustomLogger import Loggen
from Utilities import ExcelUtils

class Test_login_DDT:
    url = readConfig.getappurl()
    #No need as it is cmg frm excel
    #uid = readConfig.getuserid()
    #pwd = readConfig.getuserpwd()
    logger=Loggen.loggen()
    path="C:\\Users\\admin\\E-ComHybridFrm2020\\TestData\\LoginData.xlsx"

    @pytest.mark.regression
    def test_login_DDT(self,setup):
        self.driver = setup
        self.logger.info('******Test case Data Driven********')
        self.logger.info('*****Login Page DDT********')
        self.driver.get(self.url)
        self.lp=Loginpage(self.driver)
        self.rows=ExcelUtils.getrowcount(self.path,'Sheet1')
        lststatus=[]

        for r in range(2,self.rows+1):
            self.uid=ExcelUtils.readData(self.path,'Sheet1',r,1) #username
            self.pwd=ExcelUtils.readData(self.path,'Sheet1',r,2) #password
            self.exp=ExcelUtils.readData(self.path,'Sheet1',r,3) #exp

            self.logger.info('****Entering username and password')
            self.lp.setusername(self.uid)
            self.lp.setpassword(self.pwd)
            self.lp.login()
            time.sleep(5)
            acttitle1=self.driver.title
            exptitle='Dashboard / nopCommerce administration'
            if acttitle1==exptitle:
                if self.exp=='Pass':
                    self.logger.info('**passed***')
                    lststatus.append("Pass")
                    self.lp.logout()

                elif self.exp=='Fail':
                    self.logger.info("**failed***")
                    lststatus.append("Fail")
                    self.lp.logout()

            elif acttitle1!=exptitle:
                if self.exp=='Pass':
                    self.logger.info('***failed****')
                    lststatus.append("Fail")

                elif self.exp=='Fail':
                    self.logger.info('**passed***')
                    lststatus.append("Pass")

        print(lststatus)
        if "Fail" not in lststatus:
            self.logger.info("PASSED")
            self.driver.close()
            assert True
        else:
            self.logger.error("FAILED")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")



