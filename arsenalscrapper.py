from lib2to3.pgen2 import driver

from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True


# put your chromedrive path
PATH = "D:\chromedrvier\chromedriver.exe"  # you can change your chrome driver from here according to your directory
driver = webdriver.Chrome(PATH)
driver.get("https://www.arsenal.com/tickets")
time.sleep(5)

driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div/div[2]/div/button[2]").click()
teams = []
tick_exist = []  # bool array
no_element = 1

print("True means that seats are available for matches and false means not available")
while check_exists_by_xpath(
        f"/html/body/div[1]/div/main/div/div[1]/div/div/article[{no_element}]/div/div/div/div[1]/div[2]/a"):
    team_name = driver.find_element(by=By.XPATH,
                                    value=f"/html/body/div[1]/div/main/div/div[1]/div/div/article[{no_element}]/div/div/div/div[1]/div[2]/a").text
    teams.append(team_name)
    no_element += 1

for i in range(no_element):
    tick_exist.append(check_exists_by_xpath(
        f"/html/body/div[1]/div/main/div/div[1]/div/div/article[{i + 1}]/div/div/div/div[2]/div[2]/a"))

for i, t in enumerate(teams):
    print(f"{t}:{tick_exist[i]}")
