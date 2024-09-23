from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

# Keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Rosbiff")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("el Hombre")

first_name = driver.find_element(By.NAME, value="email")
first_name.send_keys("Rosbiff@email.com", Keys.ENTER)

# OR

#submit = driver.find_element(By.CSS_SELECTOR, value="form_button")
#submit.click()