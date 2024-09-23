from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

# Keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument(r"--user-data-dir=C:/Users/adm_cafrunikuhn/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r'--profile-directory=Default') 

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_times = [event.get_attribute('datetime').split("T")[0] for event in event_times]
#datetime_attribute = event_times.get_attribute('datetime').split("T")[0]
print(event_times)
#for time in event_times:
#    datetime_attribute = time.get_attribute('datetime').split("T")[0]
#    print(datetime_attribute)

event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
#for event in event_names:
#    eventname_attribute = event.text
#    print(eventname_attribute)

event_dict = {}
for n in range(len(event_names)):
     event_dict[n] = {
         "time": event_times[n],
         "name": event_names[n].text
     }

print(event_dict)
driver.close()