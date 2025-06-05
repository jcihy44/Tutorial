from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (ensure you have the ChromeDriver executable in your path)
driver = webdriver.Chrome()

# Open the target page
driver.get("https://www.target.com/p/men-s-short-sleeve-crewneck-graphic-t-shirt-goodfellow-co/-/A-88464719?preselect=90833012#lnk=sametab")

# Locate the first div with role="region" and get the elements with data-io-i
region_div = driver.find_elements(By.XPATH, "(//div[@role='region'])[1]//*[@data-io-i]")


# Print the number of elements
print(f"Number of elements with data-io-i: {len(region_div)}")

# Close the driver
driver.quit()