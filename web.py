from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
class info():
    def __init__(self):
        self.driver = webdriver.Chrome(options=option, service=ser)

    def get_info(self,query):
        self.query=query
        #bonus one
        self.driver.maximize_window()
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()

