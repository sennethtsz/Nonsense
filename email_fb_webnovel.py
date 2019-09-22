import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.support.ui import Select
import re
import string
import sys


# options for headless chrome
chrome_options = Options()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
i = 0

while True:
    while True:
        # initiate temp mail and get email
        url = "https://temp-mail.org/en/option/change/"
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver.exe")
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'mail')))
        random_email = "".join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
        driver.find_element_by_xpath('//input[@name="mail"]').send_keys(random_email)
        select_domain = Select(driver.find_element_by_xpath('//*[@id="domain"]'))
        select_domain.select_by_value("@hubii-network.com")
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[@class='icon-control control-refresh']").click()
        time.sleep(1)
        ini = driver.find_element_by_xpath('//input[@id="mail"]')
        email = ini.get_attribute("value")

        # initiate facebook driver
        url1 = "https://www.facebook.com/r.php"
        driver1 = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver.exe")
        driver1.get(url1)

        # create facebook account
        d = str(random.randint(1, 28))
        m = str(random.randint(1, 12))
        y = str(random.randint(1980, 2000))
        g = str(random.randint(1, 2))
        WebDriverWait(driver1, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@name='firstname']")))
        driver1.find_element_by_xpath("//input[@name='firstname']").send_keys("sam")
        driver1.find_element_by_xpath("//input[@name='lastname']").send_keys("smith")
        driver1.find_element_by_xpath("//input[@name='reg_email__']").send_keys(email)
        WebDriverWait(driver1, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@name='reg_email_confirmation__']")))
        driver1.find_element_by_xpath("//input[@name='reg_email_confirmation__']").send_keys(email)
        driver1.find_element_by_xpath("//input[@name='reg_passwd__']").send_keys('1a2b3c4d5e')
        select_d = Select(driver1.find_element_by_id("day"))
        select_d.select_by_value(d)
        select_m = Select(driver1.find_element_by_id("month"))
        select_m.select_by_value(m)
        select_y = Select(driver1.find_element_by_id('year'))
        select_y.select_by_value(y)
        driver1.find_element_by_xpath("//input[@type='radio' and @value=" + g + "]").click()
        driver1.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        # error: email cannot be used, restart process
        if len(driver1.find_element_by_xpath("//div[@class='_58mo']").get_attribute("innerHTML")) > 37:
            driver.quit()
            driver1.quit()
            continue
        else:
            # otherwise continue
            break

    while True:
        try:
            # get email code
            driver.find_element_by_xpath("//span[@class='icon-control control-refresh']").click()
            first = driver.find_element_by_xpath("//table[@id='mails']")
            second = first.find_element_by_xpath("//a[@class='title-subject']")
            text = second.text
        except:
            continue
        else:
            # remove strings leaving integers
            text = re.sub('[a-zA-Z,.:;$#@!()/\" ]', '', text)
            break

    try:
        # insert email code into facebook verification
        WebDriverWait(driver1, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@id='code_in_cliff']")))
        driver1.find_element_by_xpath("//input[@id='code_in_cliff']").send_keys(text)
        driver1.find_element_by_xpath("//button[@name='confirm']").click()
    except:
        # phone verification required
        driver.quit()
        driver1.quit()
        sys.exit("Phone Verification Required")

    # webnovel site, login with facebook
    url2 = "http://wbnv.in/8ssgVG"
    driver2 = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver.exe")
    driver2.get(url2)
    driver2.find_element_by_id("link1").click()
    WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Sign in with Facebook']")))
    driver2.find_element_by_xpath("//a[@title='Sign in with Facebook']").click()
    tabs = driver2.window_handles

    # switch to Facebook new tab login page
    driver2.switch_to.window(tabs[1])
    WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    time.sleep(1)
    driver2.find_element_by_xpath("//input[@type='text']").send_keys(email)
    driver2.find_element_by_xpath("//input[@name='pass']").send_keys("1a2b3c4d5e")
    driver2.find_element_by_xpath("//button[@value='1']").click()
    try:
        WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='u_0_x']/div[2]/div[1]/div[1]/button")))
        driver2.find_element_by_xpath("//*[@id='u_0_x']/div[2]/div[1]/div[1]/button").click()
    except:
        driver.quit()
        driver1.quit()
        driver2.quit()
        sys.exit("Phone Verification Required")

    # switch back to webnovel
    driver2.switch_to.window(tabs[0])
    random_user = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
    WebDriverWait(driver2, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='j_name']")))
    driver2.find_element_by_xpath("//input[@class='j_name']").send_keys(random_user)
    driver2.find_element_by_xpath("//label[@tabindex='2']").click()

    time.sleep(2)
    driver.quit()
    driver1.quit()
    driver2.quit()
    i = i + 1
    print("Total account/s created: " + str(i) + " Username: " + str(email))
    with open("emails.txt", "a") as file:
        file.write(email + "\n")





