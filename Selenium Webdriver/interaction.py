from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

# Keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

#Searching through the XPATH
#article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

#OR

#searching in the "articlecount" ID and as the first ANCHORA TAG.
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#article_count.click()
#print(article_count.text)

#Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

#sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)