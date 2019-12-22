from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("--mute-audio")

url = "https://dragonbound.net/"
driver = webdriver.Chrome(options=chrome_options, executable_path="./chromedriver.exe")
driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'LoginUsername')))

driver.find_element_by_id('LoginUsername').send_keys('')
driver.find_element_by_id('LoginPass').send_keys('')
driver.find_element_by_id('LoginSubmit').click()

time.sleep(2)

driver.find_element_by_id('BrokerChannel2').click()

time.sleep(2)

try:
    driver.find_element_by_id('event_button').click()
except:
    pass

driver.quit()


'''
scheduler = BlockingScheduler()
scheduler.add_job(db, 'interval', hours=4)
scheduler.start()
'''
