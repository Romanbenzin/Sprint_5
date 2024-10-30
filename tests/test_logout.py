from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import login_page_email_field, login_page_password_field, login_page_login_button, main_page_login_button, \
    main_page_make_burger_text, main_page_personal_account, personal_account_save_button,  personal_account_email_field, \
    personal_account_exit_button
from urls import main_page, authorization_page, profile_page

class TestLogout:

    def test_go_to_main_page_logo(self, setup_register_new_account):
        driver = setup_register_new_account["driver"]
        email = setup_register_new_account["email"]
        password = setup_register_new_account["password"]

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
        expected_field_mail = (driver.
                               find_element(By.XPATH, personal_account_email_field).get_attribute("value"))

        assert expected_field_mail == "test_name"
        assert driver.current_url == profile_page

        driver.find_element(By.XPATH, personal_account_exit_button).click()
        driver.get(authorization_page)
        expected_result = driver.find_element(By.XPATH, login_page_login_button).text

        assert expected_result == 'Войти'
