import csv
import datetime
from datetime import date, time
import random
import time

# Selenium imports
import requests
import wget as wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from PIL import Image

query = "fish"

driver = webdriver.Chrome()
driver.get('https://images.google.com/')

def randomDate():
    return date(2020, random.randrange(1, 12), random.randrange(1, 28))


def randomTime():
    return time(random.randrange(1, 24), random.randrange(0, 59), random.randrange(0, 59))


def randomInteractions():
    return random.randrange(0, 1000000)

searchBar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[title='Search']")))
searchBar.send_keys(query)
searchBar.send_keys(Keys.RETURN)

with open('C:/Users/raybo/OneDrive/Documents/School/Comp 363/images/fish.csv', mode='w') as fish:
    fish_writer = csv.writer(fish, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fish_writer.writerow(["Row", "Fish image URL", "Date posted", "Time posted", "Interactions"])

    rowsToWrite = []
    row_counter = 1
    for i in range(1, 101):
        if i % 25 == 0:
            continue

        try:
            element = driver.find_element(By.XPATH, """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img""" % i)
            driver.execute_script("arguments[0].click();", element)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            imgelement = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
            imgURL = imgelement.get_attribute('src')
            post_date = date(2020, random.randrange(1, 12), random.randrange(1, 28))
            post_time = datetime.time(random.randrange(1, 24), random.randrange(0, 59), random.randrange(0, 59))
            interactions = random.randrange(0, 1000000)
            fish_writer.writerow([row_counter, imgURL, post_date, post_time, interactions])
            row_counter += 1
        except:
            pass

    fish.close()
