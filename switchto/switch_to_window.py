from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window

        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # finding all window handles
        # for handle in handles:
        #     print("Handle: " + handle)

        # Switch to window and search course there will be 2 handles the parent and the second
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchBox = driver.find_element(By.XPATH, "//input[@id = 'search']")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        #swapping back to parent window
        driver.switch_to.window(parentHandle)
        element = driver.find_element(By.XPATH, "//input[@name = 'enter-name']")
        element.send_keys("Test")
        time.sleep(2)






ff = SwitchToWindow()
ff.test()