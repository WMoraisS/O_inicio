# função clicar
# função expandir
from selenium import webdriver

dicio = {'btn-login' : '12345', 'rdBasico': '6789'}
print(dicio['btn-login'])



#driver = webdriver.Chrome(executable_path=)


def clicar(btn):
    driver.find_element_by_xpath(btn).click()

def expandir(lista):
    driver.find_element_by_xpath(lista).click()

