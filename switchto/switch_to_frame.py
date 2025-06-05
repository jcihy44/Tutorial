from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        # 3 ways to swap to different frame
        # Switch to frame using Id
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        driver.switch_to.frame(0)

        # Search course
        time.sleep(2)
        searchBox = driver.find_element(By.XPATH, "//input[@id = 'search']")
        searchBox.send_keys("python")
        time.sleep(2)
        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        searchBox2 = driver.find_element(By.XPATH, "//input[@id = 'name']")
        searchBox2.send_keys("python2")
        time.sleep(2)



ff = SwitchToFrame()
ff.test()
