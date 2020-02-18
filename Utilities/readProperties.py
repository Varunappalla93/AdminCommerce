import configparser

config=configparser.RawConfigParser()

config.read("C:\\Users\\admin\\E-ComHybridFrm2020\\Configurations\\config.ini")

class readConfig:
    @staticmethod
    def getappurl():
        url=(config.get('common login info','url'))
        return url

    @staticmethod
    def getuserid():
        uid=(config.get('common login info','uid'))
        return uid

    @staticmethod
    def getuserpwd():
        pwd=(config.get('common login info','pwd'))
        return pwd

#print(readConfig.getappurl())
#print(readConfig.getuserid())
#print(readConfig.getuserpwd())