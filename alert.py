import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#name = "Jessica"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Jessica")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
time.sleep(5)
alertText = alert.text
print(alert.text)
#alert.accept()
alert.dismiss()
time.sleep(7)
