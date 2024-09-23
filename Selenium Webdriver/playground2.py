from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/path/to/your/new/user-profile")
chrome_options.add_argument("--profile-directory=Profile 1")  # Change Profile 1 to the desired profile name

driver = webdriver.Chrome(service=Service("path/to/chromedriver"), options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(f'The price is: {price_dollar.text}.{price_cents.text}')

driver.quit()
