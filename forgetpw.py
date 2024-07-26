import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("baniyajeshika@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Jess@977#")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Jess@977#")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)