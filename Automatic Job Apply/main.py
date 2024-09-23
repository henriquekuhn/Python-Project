from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
DIR = os.getcwd() + "/Automatic Job Apply"
os.chdir(DIR)

USER = os.getenv("email")
PSW = os.getenv("psw")

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3822890711&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

time.sleep(2)

login = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
login.click()

user = driver.find_element(By.ID, value="username")
user.send_keys(USER, Keys.ENTER)

time.sleep(2)

password = driver.find_element(By.ID, value="password")
password.send_keys(PSW, Keys.ENTER)
time.sleep(5)

save = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
save.click()
time.sleep(2)

#follow = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button/span')
#follow.click()

