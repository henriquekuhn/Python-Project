from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument(r"--user-data-dir=C:/Users/adm_cafrunikuhn/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r'--profile-directory=Default') 

driver = webdriver.Chrome(options=chrome_options)

#driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

#print(f'The price is: {price_dollar.text}.{price_cents.text}')

driver.get("https://www.python.org/")
#documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


#drive.close()
driver.quit()