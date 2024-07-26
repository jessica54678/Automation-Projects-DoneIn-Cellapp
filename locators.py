import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("JESSICA")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("hello123")
driver.find_element(By.ID, "exampleCheck1").click()

#static dropdown just like male,female in which you dont need to search
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
driver.find_element(By.ID, "inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
time.sleep(5)