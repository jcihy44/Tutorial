from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
class TargetApparelPage:

    #def __int__(self,driver):
 #       self.driver = driver

    #SELECT_COLOR = (By.XPATH, "(//div[@role='region'])[1]")

    def select_color(self):
        service = Service(executable_path="C:\\Users\\jcihy\\PycharmProjects\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.target.com/p/men-s-short-sleeve-crewneck-graphic-t-shirt-goodfellow-co/-/A-88464719?preselect=90832987#lnk=sametab")
        color_list = driver.find_element(By.XPATH, "(//div[@role='region'])[1]")
        data_io_elements = color_list.find_elements(By.XPATH, ".//*[@data-io-i]")
        print(f"Number of elements with data-io-i: {len(data_io_elements)}")
        #size = len(colorList)
        #print("size of the list: "+ str(size))
cc = TargetApparelPage()
cc.select_color()
#    def select_size_group(self):


#    def select_size(self):


#    def select_qty(self):