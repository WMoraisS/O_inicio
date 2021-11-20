from selenium import webdriver
from selenium.webdriver.common import action_chains
import time

nav = webdriver.Chrome('D:\GitHub\O_inicio\Cursos\Python\Cisco Academy\packages/chromedriver.exe')
site = nav.get('https://www.netacad.com/pt-br')
nav.maximize_window()
entrar = nav.find_element_by_xpath('/html/body/header/div/div[5]/nav/div[1]/section/ul/li/a')
login = nav.find_element_by_xpath('/html/body/header/div/div[5]/nav/div[1]/section/ul/li/ul/li[1]/a')
move = action_chains.ActionChains(nav)
move.move_to_element(entrar).perform()
move.move_to_element(login).click().perform()
time.sleep(2)
nav.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/span/input').send_keys('wil.h2or@hotmail.com')
x = nav.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div[2]/input')
x.click()
time.sleep(2)
nav.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div[2]/div[2]/span/input').send_keys('2Wsxdvfr')
nav.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div[2]/input').click()
time.sleep(10)
