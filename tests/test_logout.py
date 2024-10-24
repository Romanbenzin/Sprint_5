from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_go_to_main_page_logo(random_email, random_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/p')))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    # Заполнение данных пользователя для регистрации
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys('test_name')
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[3]/div/div/input').send_keys(random_password)

    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/button').click()

    # Авторизация через кнопку "Войти в аккаунт" на главной
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        random_password)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/section[1]/h1')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > main > div > div > div > div > button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')))
    expected_field_mail = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input').get_attribute("value")

    assert expected_field_mail == random_email
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button').click()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    expected_result = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').text

    assert expected_result == 'Войти'

    driver.quit()