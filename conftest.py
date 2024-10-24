import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import random_email
from helpers import random_password
from locators import main_page_personal_account, register_button_in_personal_account, \
    register_page_already_registered, register_page_register_button, register_page_fields
from urls import register_page, main_page

@pytest.fixture
def setup_registration():
    driver = webdriver.Chrome()
    driver.get(main_page)
    email = random_email()
    password = random_password()

    # Переход в личный кабинет и на страницу регистрации
    driver.find_element(By.XPATH, main_page_personal_account).click()
    driver.find_element(By.XPATH, register_button_in_personal_account).click()

    # Ожидание появления страницы регистрации
    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, register_page_already_registered)))

    # Проверка, что находимся на странице регистрации
    assert driver.current_url == register_page, "Открыта не страница регистрации"

    # Заполнение данных пользователя для регистрации
    driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('test_name')
    driver.find_elements(By.XPATH, register_page_fields)[1].send_keys(email)
    driver.find_elements(By.XPATH, register_page_fields)[2].send_keys(password)

    #Клик по кнопке регистрации
    driver.find_element(By.XPATH,register_page_register_button).click()
    yield {"driver": driver, "email": email, "password": password}

    driver.quit()

@pytest.fixture
def setup_auth_link():
    driver = webdriver.Chrome()
    driver.get(main_page)
    email = random_email()
    password = random_password()

    driver.find_element(By.XPATH, main_page_personal_account).click()
    driver.find_element(By.XPATH, register_button_in_personal_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, register_page_already_registered)))

    assert driver.current_url == register_page, "Открыта не страница регистрации"

    yield {"driver": driver, "email": email, "password": password}

    driver.quit()

@pytest.fixture()
def open_main_page():
    driver = webdriver.Chrome()
    driver.get(main_page)

    assert driver.current_url == main_page

    yield driver

    driver.quit()

@pytest.fixture()
def selected_this_one():
    return "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

@pytest.fixture()
def selected_value_not_this():
    return "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"
