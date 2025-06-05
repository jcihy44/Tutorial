from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.open('https://www.letskodeit.com/practice', '_blank');")
        #swapping to new window for actions to happen
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(3)
        time.sleep(6)

        # element = driver.find_element(By.XPATH, "//input[@name = 'enter-name']")
        # element.click()
        element = driver.find_element(By.XPATH, "//input[@name = 'enter-name']")
        element.send_keys("Test")
        time.sleep(3)
ff = JavaScriptExecution()
ff.test()