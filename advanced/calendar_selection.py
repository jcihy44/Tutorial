from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        # driver.find_element_by_id("tab-flight-tab").click()
        driver.find_element(By.XPATH, "//button[@data-testid = ('uitk-date-selector-input1-default')]").click()
        # Find departing field
        departingfield = driver.find_element(By.ID, "flight-departing")
        # Click departing field
        departingfield.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        datetoselect = driver.find_element(By.XPATH,
                                           "(//div[@class='datepicker-cal-month'])[1]//button[text()='30']")
        # Click the date
        datetoselect.click()

        time.sleep(3)
        driver.quit()

ff = CalendarSelection()
ff.test1()