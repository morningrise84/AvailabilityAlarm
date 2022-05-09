# LOAD MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound
import time

# CHROME PREPARATION AND TARGET DEFINITION
PATH = r"""C:\Users\blablabla\chromedriver.exe""" # path to chromedriver in the local machine
s = Service(PATH)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.youknowwhatsiteiamtalkingabout.com/') # insert here the link to the buying options for the desired product
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="sp-cc-accept"]').click()

# SEARCH & NOTIFY OR RELOAD
while True:

    try:
        time.sleep(3)
        elem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Warehouse')
        if elem.is_displayed():
            playsound(r"""C:\Users\blablabla\alarm.wav""") # path to the alarm sound in the local machine
            print("FOUND!")
            break

    except NoSuchElementException:
        print("No luck")
        time.sleep(15)
        driver.execute_script("location.reload(true);")
        continue
