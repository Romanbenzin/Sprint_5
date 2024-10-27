from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import setup_registration
from locators import main_page_login_button, login_page_email_field, login_page_password_field, login_page_login_button, \
    main_page_make_burger_text, main_page_personal_account, register_page_login_button, forgot_page_login_button
from urls import main_page, register_page, forgot_pass_page


class TestAuthorization:

    def test_authorization_on_main_page(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        #Тест авторизации через кнопку "Войти в аккаунт" на главной
        driver.get(main_page)
        driver.find_element(By.XPATH, main_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page_make_burger_text)))

        assert driver.current_url == main_page

    def test_authorization_personal_account(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        #Авторизация через кнопку "Личный кабинет" на главной
        driver.get(main_page)
        driver.find_element(By.XPATH, main_page_personal_account).click()

        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page_make_burger_text)))
        assert driver.current_url == main_page

    def test_authorization_on_registration_page(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        #Авторизация через кнопку "Войти" на странице регистрации
        driver.get(register_page)
        driver.find_element(By.XPATH, register_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page_make_burger_text)))
        assert driver.current_url == main_page

    def test_authorization_on_forgot_password_page(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        #Авторизация через кнопку "Войти" на странице восстановления пароля
        driver.get(forgot_pass_page)
        driver.find_element(By.XPATH, forgot_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page_make_burger_text)))
        assert driver.current_url == main_page
