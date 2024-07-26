import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
 #<a id="ui-id-4" class="ui-corner-all" tabindex="-1" xpath="1">India</a>

for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(5)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
