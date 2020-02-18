#Page Object Class
from selenium import webdriver
#Locators
class Loginpage:
    userid='Email'
    passwordid="Password"
    loginbtnxpath="//input[@class='button-1 login-button']"
    logoutbtnxpath="//a[contains(text(),'Logout')]"

#Constructor
    def __init__(self,driver):
         self.driver=driver
#Actions
    def setusername(self,username):
        self.driver.find_element_by_id(self.userid).clear()
        self.driver.find_element_by_id(self.userid).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.passwordid).clear()
        self.driver.find_element_by_id(self.passwordid).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.loginbtnxpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logoutbtnxpath).click()