from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

# Set the correct path to ChromeDriver executable
chrome_driver_path = "c:\\Users\\Admin\\Desktop\\chromedriver-win64\\chromedriver.exe"

# Create ChromeOptions object and set the executable path
chrome_options = Options()
# Add any additional options if needed

# Create a new instance of ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the webpage
    driver.get("https://dashboard-dev.aylanetworks.com/#/devices")

    # Wait for the "Yes" button to be clickable
    yes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes')]"))
    )
    yes_button.click()

    # Find the username and password input fields and fill them
    username_field = driver.find_element(By.NAME, "email")
    username_field.send_keys("pokle+volt@aylanetworks.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Volt@123")  # Replace "" with the actual password

    # Submit the form
    login_button = driver.find_element(By.CLASS_NAME, "log-in-button")
    login_button.click()

    # Wait for the page to load and the search button to be clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@data-modal-title='Search']"))
    )
    
    # Ensure any overlays are gone
    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located((By.CLASS_NAME, "loader"))
    )

    # Use JavaScript to click the search button
    driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
    driver.execute_script("arguments[0].click();", search_button)

    # Wait for the DSN input field to become visible
    dsn_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='filters.byDevices.dsn']"))
    )
    
    # Prompt for user input for the DSN
    dsn = input("Please enter the DSN: ")
    dsn_input.send_keys(dsn)

    # Wait for a brief period of time
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

    time.sleep(5)

    # Click on the "Properties" link
    try:
        properties_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@ng-click, \"showDetail('properties')\")]"))
        )
        properties_link.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].scrollIntoView(true);", properties_link)
        driver.execute_script("arguments[0].click();", properties_link)

    # Click on the center of the "Properties"
    properties_center = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[contains(text(), 'fix_001_conf')]"))
    )
    properties_center.click()

    # Function to create and update data point
    def create_and_update_datapoint(json_data):
        try:
            # Click on the "Datapoints" link using JavaScript
            datapoints_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@rel='list-datapoints']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", datapoints_link)
            driver.execute_script("arguments[0].click();", datapoints_link)

            # Click the button to create a new datapoint using JavaScript
            create_datapoint_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@ng-html-modal, 'views/devices/createDatapoint.html')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", create_datapoint_button)
            driver.execute_script("arguments[0].click();", create_datapoint_button)

            # Fill in the JSON data in the datapoint value field
            datapoint_value_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@ng-model='datapoint.value']"))
            )
            datapoint_value_field.send_keys(json_data)

            # Click the button to create the datapoint using JavaScript
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @ng-click='createDatapoint()']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            driver.execute_script("arguments[0].click();", submit_button)
        except TimeoutException as e:
            print(f"An error occurred: {e}")

    # JSON data to update
    json_data_list = [
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Relax","WW":0,"C":16711680},"M":"show","CB":7,"WW":255,"CW":0,"Show":{"S3":{"C":14352128,"WW":0,"CW":0},"CB":100,"S1":{"C":16711680,"WW":0,"CW":0},"name":"Halloween","S":10,"S2":{"C":16756736,"WW":0,"CW":0}},"P":0,"C":65535}',
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Relax","WW":0,"C":16711680},"M":"show","CB":0,"WW":255,"CW":0,"Show":{"S3":{"C":14352128,"WW":0,"CW":0},"CB":100,"S1":{"C":16711680,"WW":0,"CW":0},"name":"Halloween","S":10,"S2":{"C":16756736,"WW":0,"CW":0}},"P":1,"C":0}',
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Relax","WW":0,"C":16711680},"M":"preset","CB":0,"WW":255,"CW":0,"Show":{"S3":{"C":2675525,"WW":0,"CW":0},"CB":100,"S1":{"C":65535,"WW":0,"CW":0},"name":"Christmas","S":10,"S2":{"C":1761961,"WW":0,"CW":0}},"P":1,"C":0}',
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Summer","WW":0,"C":65535},"M":"preset","CB":0,"WW":255,"CW":0,"Show":{"S3":{"C":2675525,"WW":0,"CW":0},"CB":100,"S1":{"C":65535,"WW":0,"CW":0},"name":"Christmas","S":10,"S2":{"C":1761961,"WW":0,"CW":0}},"P":1,"C":0}',
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Relax","WW":0,"C":16711680},"M":"show","CB":0,"WW":255,"CW":0,"Show":{"S3":{"C":2675525,"WW":0,"CW":0},"CB":100,"S1":{"C":65535,"WW":0,"CW":0},"name":"Christmas","S":10,"S2":{"C":1761961,"WW":0,"CW":0}},"P":1,"C":0}',
        '{"P":1,"WW":98,"C":65535,"CW":27,"Preset":{"name":"Relax","CB":100,"C":16711680,"B":100,"CW":0,"WW":0},"Show":{"name":"Halloween","CB":100,"S":10},"M":"color","CB":100}',
        '{"P":1,"WW":98,"C":65535,"CW":27,"Preset":{"name":"Relax","CB":100,"C":16711680,"B":100,"CW":0,"WW":0},"Show":{"name":"Halloween","CB":100,"S":10},"M":"color","CB":100}',
        '{"Preset":{"CB":100,"CW":0,"B":255,"name":"Relax","WW":0,"C":16711680},"M":"show","CB":7,"WW":255,"CW":0,"Show":{"S3":{"C":14352128,"WW":0,"CW":0},"CB":100,"S1":{"C":16711680,"WW":0,"CW":0},"name":"Halloween","S":10,"S2":{"C":16756736,"WW":0,"CW":0}},"P":0,"C":65535}'
    ]

    # Update each JSON data
    for json_data in json_data_list:
        create_and_update_datapoint(json_data)

finally:
    # Close the driver after completion
    driver.quit()
