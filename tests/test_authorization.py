from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_authorization_on_main_page(random_email, random_password):
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

    #Тест авторизации через кнопку "Войти в аккаунт" на главной
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_password)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/section[1]/h1')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_authorization_personal_account(random_email, random_password):
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

    #Авторизация через кнопку "Личный кабинет" на главной
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_password)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/section[1]/h1')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_authorization_on_registration_page(random_email, random_password):
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

    #Авторизация через кнопку "Войти" на странице регистрации
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p/a').click()

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_password)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/section[1]/h1')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_authorization_on_forgot_password_page(random_email, random_password):
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

    #Авторизация через кнопку "Войти" на странице восстановления пароля
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p/a').click()

    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_password)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/section[1]/h1')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
