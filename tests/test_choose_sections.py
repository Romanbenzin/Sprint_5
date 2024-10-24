import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_selections(random_email, random_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/')
    #Соусы:
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span').click()
    expected_value_two = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]').get_attribute('class')
    assert expected_value_two == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    # Начинки:
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span').click()
    expected_value_three = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]').get_attribute('class')
    assert expected_value_three == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    #Булки:
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span').click()
    expected_value_one = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]').get_attribute('class')
    assert expected_value_one == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    driver.quit()