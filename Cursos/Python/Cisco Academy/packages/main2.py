#from sys import path, path_importer_cache

# path.append('..\\packages')

# import extra.ugly.omega

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp

# print(extra.ugly.omega.FunO())
# print(sig.FunS())
# print(alp.FunA())

# from sys import path

# path.append('..\\packages\\extrapack.zip')

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp
# from extra.iota import FunI
# from extra.good.beta import FunB

# print(sig.FunS())
# print(alp.FunA())
# print(FunI())
# print(FunB())

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='D:\GitHub\O_inicio\Cursos\Python\Cisco Academy\packages/chromedriver.exe')
driver.get('http://allselenium.info/category/python-selenium/')
achains = ActionChains(driver)
# MOUSO HOVER
#lings = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/div/div[2]/div/ul/li[2]/div')
#ko = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/div/div[2]/div/ul/li[2]/div/ul/li[1]')
#achains.move_to_element(lings).perform()
#achains.move_to_element(ko).perform()
#################################################################################################################
# CLICK IN EACH ITEM
tabela = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]')

i = 0
for i in range(5):
    li = driver.find_elements_by_tag_name('li')#(i)
    li.click()
    i += 1

time.sleep(10)
