from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time

dicion = {
    'mais':'/html/body/div[1]/div/div[2]/div[2]/header/div/div[2]/div[1]/nav/ul/li[12]/div[1]'
}

class action:
    def __init__(self):
        self.web = webdriver.Chrome(executable_path=r'C:\\Users\\wilh2\\AppData\\Local\\SeleniumBasic\\chromedriver.exe')
        self.mMove = action_chains.ActionChains(self.web)
    
    def click(self, path):
        self.web.find_element_by_xpath(path).click()

    def expandir(self, path):
        element = self.web.find_element_by_xpath(path)
        self.mMove.move_to_element(element).perform()

url = 'https://chromedriver.chromium.org/capabilities'

xAuto = action()
xAuto.web.get(url)

xAuto.expandir(dicion['mais'])
time.sleep(2)
