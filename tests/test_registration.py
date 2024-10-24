from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (login_page_recover_password_button, main_page_make_burger_text, \
                      register_page_register_button, register_page_error, register_page_fields, \
                      login_page_login_button, login_page_email_field, login_page_password_field)
from urls import register_page, main_page

class TestRegistration:

    def test_registration(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        #Ждем прогрузку страницы после клика
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, login_page_recover_password_button)))
        #Авторизация после регистрации
        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        # Ждем прогрузку страницы после клика
        WebDriverWait(driver, 5).until(expected_conditions.
                                       element_to_be_clickable((By.XPATH, main_page_make_burger_text)))

        #Проверка, что после авторизации есть надпись: "Соберите бургер" и находимся главной странице
        make_a_burger = driver.find_element(By.XPATH, main_page_make_burger_text)
        assert make_a_burger.text == 'Соберите бургер'
        assert driver.current_url == main_page,  "Открыта не главная страница"

    def test_registration_using_incorrect_name(self, setup_auth_link):
        driver = setup_auth_link["driver"]
        email = setup_auth_link["email"]
        password = setup_auth_link["password"]

        #Заполнение данных пользователя для регистрации
        driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('')
        driver.find_elements(By.XPATH, register_page_fields)[1].send_keys(email)
        driver.find_elements(By.XPATH, register_page_fields)[2].send_keys(password)

        driver.find_element(By.XPATH, register_page_register_button).click()

        #Проверка, что после нажатия на "Зарегистрироваться" никуда не перекинет, тк не указано "Имя"
        assert driver.current_url == register_page, "Открыта не страница регистрации"

    def test_registration_using_incorrect_email(self, setup_auth_link):
        driver = setup_auth_link["driver"]
        password = setup_auth_link["password"]

        #Заполнение данных пользователя для регистрации
        driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('test_name')
        driver.find_elements(By.XPATH, register_page_fields)[1].send_keys('mail.mail.mail')
        driver.find_elements(By.XPATH, register_page_fields)[2].send_keys(password)

        driver.find_element(By.XPATH, register_page_register_button).click()

        assert driver.current_url == register_page, "Открыта не страница регистрации"

    def test_registration_using_incorrect_password(self, setup_auth_link):
        driver = setup_auth_link["driver"]
        email = setup_auth_link["email"]

        # Заполнение данных пользователя для регистрации
        driver.find_elements(By.XPATH, register_page_fields)[0].send_keys('test_name')
        driver.find_elements(By.XPATH, register_page_fields)[1].send_keys(email)
        driver.find_elements(By.XPATH, register_page_fields)[2].send_keys('four')

        driver.find_element(By.XPATH, register_page_register_button).click()

        assert driver.current_url == register_page, "Открыта не страница регистрации"

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, register_page_error)))
        expected_message = driver.find_element(By.XPATH, register_page_error).text
        assert expected_message == "Некорректный пароль", f"Текст ошибки: {expected_message}"
