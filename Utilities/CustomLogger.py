import logging

class Loggen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename='C:\\Users\\admin\\E-ComHybridFrm2020\\Logs\\automationlogs')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
