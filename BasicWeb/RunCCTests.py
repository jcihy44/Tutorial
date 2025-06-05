import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service


class RunCCTests():

    def test(self):
        service = Service(executable_path="C:\\Users\\jcihy\\PycharmProjects\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.target.com")
        time.sleep(5)

run_tests = RunCCTests()
run_tests.test()