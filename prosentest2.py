from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

path='/Users/aysebetulaksakal/Desktop/chromedriver'
url='http://www.procenne.com/'
name='John'
surname='Doe'
email='jdoe@procenne.com'
product='Cryptaway'
inst='Procenne'
title='Senior QA Engineer'
phone='0090 212 6916363'
message='MERHABA TEST TAKIMI'

driver = webdriver.Chrome(path)
driver.get(url)
driver.maximize_window()


driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[2]/div[1]/a").click()

sleep(2)

driver.find_element(By.ID, "firstname").send_keys(name)

driver.find_element(By.ID, "lastname").send_keys(surname)

driver.find_element(By.ID, "email").send_keys(email)

Select(driver.find_element_by_id("konu")).select_by_value(product)

driver.find_element(By.ID, "company").send_keys(inst)

driver.find_element(By.ID, "title").send_keys(title)

driver.find_element(By.ID, "telephone").send_keys(phone)

driver.find_element(By.NAME, "message").send_keys(message)

driver.find_element(By.ID, "kvkk").click()

driver.find_element(By.ID, "campaing").click()

sleep(2)

driver.find_element(By.XPATH, '//*[@id="contact"]/div/div[2]/form/div/div[6]/button').click()

sleep(2)

print('Well done!')
driver.quit()