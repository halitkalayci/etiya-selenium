
from argparse import Action
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get("https://www.kodlama.io/")
driver.maximize_window()
WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div[1]/footer/div/div/div[2]/ul/li[1]/a')))
termsAndConditions = driver.find_element(By.XPATH,'/html/body/div[1]/footer/div/div/div[2]/ul/li[1]/a')
sleep(1)
actions = ActionChains(driver)
actions.move_to_element(termsAndConditions)
actions.click(termsAndConditions)
actions.perform()
sleep(20)
# searchBox = driver.find_element(By.NAME,"q")
# searchBox.send_keys("kodlamaio")
# sleep(1)
# searchBox.send_keys(Keys.ENTER)
# sleep(5)
# firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
# print(firstResult.get_attribute("href") == "https://www.kodlama.io/")
# sleep(25)


# selenium kullanılacak
# seçtiğiniz bir website olacak
# 1 test case belirle
# bu test case'i koda dök
# süre yarın ders saatine kadar