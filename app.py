from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get('https://www.google.com')
driver.find_element_by_name('q').send_keys('') #Pesquise algo aqui
driver.find_element_by_name('q').send_keys(Keys.RETURN)