from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "http://www.goibibo.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)
partialText = "Del"
textToSelect = "Delhi, India"
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class = 'sc-12foipm-22 kGtxGm']").click()
textElement = driver.find_element(By.XPATH, "//input[@type = 'text']")
textElement.send_keys(partialText)
time.sleep(1)
ulElement = driver.find_element(By.ID, "autoSuggest-list")
inner_html = ulElement.get_attribute('innerHTML')
# print(inner_html)

liElements = ulElement.find_elements(By.TAG_NAME, "li")
time.sleep(2)

for element in liElements:
    # print(element.text)
    if textToSelect in element.text:
        element.click()
        break

time.sleep(4)

driver.quit()