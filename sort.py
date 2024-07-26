import time
from selenium import webdriver
from selenium.webdriver.common.by import By
list = []
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
time.sleep(3)
elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in elements:
    list.append(element.text)
oldlist = list.copy()
list.sort()
assert oldlist == list