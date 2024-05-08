from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

# Wait for the loader element to disappear
WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "loader")))

# Click on the search label to open the search modal
search_label = driver.find_element(By.XPATH, "//label[@data-modal-title='Search']")
search_label.click()

# Wait for the DSN input field to be visible
dsn_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='filters.byDevices.dsn']"))
)

# Wait for the user to enter the DSN
dsn = input("Please enter the DSN: ")

# Enter the DSN into the input field
dsn_input.send_keys(dsn)

# Find and click the search button
search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'SEARCH')]")
search_button.click()
