from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Set the path to ChromeDriver executable
chrome_driver_path = "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"



# Create ChromeOptions object and set the executable path
chrome_options = Options()
# Add any additional options if needed

# Create a new instance of ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get("https://dashboard-dev.aylanetworks.com/#/devices")

# Wait for the "Yes" button to be clickable
yes_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes')]"))
)

# Click on the "Yes" button
yes_button.click()   
# Find the username and password input fields and fill them
username_field = driver.find_element(By.NAME, "email")  # Assuming the name attribute is "email"
username_field.send_keys("pokle+volt@aylanetworks.com")

password_field = driver.find_element(By.NAME, "password")  # Assuming the name attribute is "password"
password_field.send_keys("Volt@123")  # Replace "your_password" with the actual password


# Submit the form (assuming there's a submit button)
login_button = driver.find_element(By.CLASS_NAME, "log-in-button")  # Assuming the class name is "log-in-button"
login_button.click()
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(@ng-html-modal, 'views/search/index.html')]"))
)

WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "loader"))
)

# Click on the search button
search_button.click()

# Wait for the DSN input field to become visible
dsn_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='filters.byDevices.dsn']"))
)

# Wait for the user to enter the DSN
dsn = input("Please enter the DSN: ")

# Enter the DSN into the input field
dsn_input.send_keys(dsn)

# Wait for a brief period of time (6 seconds in this case)
time.sleep(6)

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='ng-binding' and contains(text(), 'SEARCH')]"))
)
search_button.click() 

time.sleep(3) 

# Re-locate the td_element after the DOM changes
td_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//td[@align='center']"))
)
td_element.click()


time.sleep(15) 
