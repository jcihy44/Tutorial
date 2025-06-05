from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (ensure you have the ChromeDriver executable in your path)
driver = webdriver.Chrome()

# Open the target page
driver.get("https://www.target.com/p/men-s-short-sleeve-crewneck-graphic-t-shirt-goodfellow-co/-/A-88464719?preselect=90833012#lnk=sametab")

# Locate the <a> elements within the region with the data-io-i attribute
a_elements = driver.find_elements(By.XPATH, "(//div[@role='region'])[1]//*[@data-io-i]")

# Extract and print the href or values from each <a> element
a_values = [element.get_attribute('href') for element in a_elements if element.get_attribute('href')]

# Print the list of <a> values (URLs)
print("List of <a> values (href):", a_values)

# Close the driver
driver.quit()