from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "//div[@class = 'collapse navbar-collapse']//a[@href = '/login']").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "login-password").send_keys("abc")
        driver.find_element(By.ID, "login").click()
        time.sleep(1)
        self.takeScreenshot(driver)
        # Mac
        # destinationFileName = "/Users/atomar/Desktop/test.png"
        # Windows
        # destinationFileName = "C:\\Users\\jcihy\\PycharmProjects\\Tutorial\\advanced\\test.png"

        # try:
        #     driver.save_screenshot(destinationFileName)
        #     print("Screenshot saved to directory --> :: " + destinationFileName)
        # except NotADirectoryError:
        #     print("Not a directory issue")

    def takeScreenshot(self, driver):
        fileName = str(round(time.time()*1000)) + ".png"
        screenshotDirectory = "C:\\Users\\jcihy\\PycharmProjects\\Tutorial\\advanced\\screenshots\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()