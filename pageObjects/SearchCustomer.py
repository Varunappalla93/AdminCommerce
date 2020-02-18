class SearchCust:
    srchemail="//input[@id='SearchEmail']"
    srchfirstname="//input[@id='SearchFirstName']"
    srchlastname="//input[@id='SearchLastName']"
    srchbutton="//button[@id='search-customers']"
    tablexpath="//table[@role='grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.srchemail).clear()
        self.driver.find_element_by_xpath(self.srchemail).send_keys(email)

    def setFirstname(self, fname):
        self.driver.find_element_by_xpath(self.srchfirstname).clear()
        self.driver.find_element_by_xpath(self.srchfirstname).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.srchlastname).clear()
        self.driver.find_element_by_xpath(self.srchlastname).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.srchbutton).click()

    def rowlen(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def collen(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.rowlen()+1):
            table = self.driver.find_element_by_xpath(self.tablexpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchbyname(self,name):
        flag=False
        for r in range(1,self.rowlen()+1):
            table=self.driver.find_element_by_xpath(self.tablexpath)
            Name=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag








