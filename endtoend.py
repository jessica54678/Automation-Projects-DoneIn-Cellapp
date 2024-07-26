import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
lists = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
time.sleep(3)
for list in lists:
    name = list.find_element(By.XPATH, "div/h4/a").text
    if name == "Blackberry":
        list.find_element(By.XPATH, "div/button").click()
        time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "input[class*='filter-input']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Your order will be" in successText



