from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import login_page_email_field, login_page_password_field, login_page_login_button, main_page_login_button, \
    main_page_make_burger_text, main_page_personal_account, personal_account_email_field, personal_account_save_button
from urls import main_page

class TestPersonalAccount:

    def test_go_to_personal_account(self, setup_registration):
        driver = setup_registration["driver"]
        email = setup_registration["email"]
        password = setup_registration["password"]

        # Авторизация через кнопку "Войти в аккаунт" на главной
        driver.get(main_page)
        driver.find_element(By.XPATH, main_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_field).send_keys(email)
        driver.find_element(By.XPATH, login_page_password_field).send_keys(password)
        driver.find_element(By.XPATH, login_page_login_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_page_make_burger_text)))
        assert driver.current_url == main_page

        driver.find_element(By.XPATH, main_page_personal_account).click()

        WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, personal_account_save_button)))
        expected_field_mail = driver.find_elements(By.XPATH, personal_account_email_field)[1].get_attribute("value")

        assert expected_field_mail == email
