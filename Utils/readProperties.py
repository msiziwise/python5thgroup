import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Configuration.ini")


class ReadConfig():

    @staticmethod
    def getUrl():
        return config.get('URLS', 'saurceDemoURL')

    @staticmethod
    def getUserName():
        return config.get('Login Details', 'username')

    @staticmethod
    def getPassword():
        return config.get('Login Details', 'password')
