import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import static_email, static_password
from helpers import random_email, random_password
from locators import main_page_personal_account, register_button_in_personal_account, \
    register_page_already_registered, register_page_register_button, register_page_fields
from urls import main_page

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

@pytest.fixture
def setup_register_new_account(driver):
    email = random_email()
    password = random_password()
    driver.get(main_page)

    # Переход в личный кабинет и на страницу регистрации
    driver.find_element(By.XPATH, main_page_personal_account).click()
    driver.find_element(By.XPATH, register_button_in_personal_account).click()

    # Ожидание появления страницы регистрации
    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, register_page_already_registered)))

    # Заполнение данных пользователя для регистрации
    driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('test_name')
    driver.find_elements(By.XPATH, register_page_fields)[1].send_keys(email)
    driver.find_elements(By.XPATH, register_page_fields)[2].send_keys(password)

    # Клик по кнопке регистрации
    driver.find_element(By.XPATH, register_page_register_button).click()
    yield {"driver": driver, "email": email, "password": password}

@pytest.fixture
def setup_registration(driver):
    email = static_email
    password = static_password
    driver.get(main_page)

    # Переход в личный кабинет и на страницу регистрации
    driver.find_element(By.XPATH, main_page_personal_account).click()
    driver.find_element(By.XPATH, register_button_in_personal_account).click()

    # Ожидание появления страницы регистрации
    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, register_page_already_registered)))

    # Заполнение данных пользователя для регистрации
    driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('test_name')
    driver.find_elements(By.XPATH, register_page_fields)[1].send_keys(email)
    driver.find_elements(By.XPATH, register_page_fields)[2].send_keys(password)

    #Клик по кнопке регистрации
    driver.find_element(By.XPATH,register_page_register_button).click()
    yield {"driver": driver, "email": email, "password": password}

@pytest.fixture
def setup_auth_link(driver):
    driver.get(main_page)
    email = static_email
    password = static_password

    driver.find_element(By.XPATH, main_page_personal_account).click()
    driver.find_element(By.XPATH, register_button_in_personal_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, register_page_already_registered)))

    yield {"driver": driver, "email": email, "password": password}
