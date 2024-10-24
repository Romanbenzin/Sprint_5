import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration(random_email, random_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/p')))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    #Заполнение данных пользователя для регистрации
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys('test_name')
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[3]/div/div/input').send_keys(random_password)

    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/button').click()

    #Ждем прогрузку страницы после клика
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                      '//*[@id="root"]/div/main/div/div/p[2]/a')))
    #Авторизация после регистрации
    driver.find_element(By.XPATH,'/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_password)
    driver.find_element(By.XPATH,'/html/body/div/div/main/div/form/button').click()

    # Ждем прогрузку страницы после клика
    WebDriverWait(driver, 5).until(expected_conditions.
                                   element_to_be_clickable((By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button')))

    #Проверка, что после авторизации есть надпись: "Соберите бургер" и находимся главной странице
    make_a_burger = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/h1')
    assert make_a_burger.text == 'Соберите бургер'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_registration_using_incorrect_name(random_email, random_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/p')))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    #Заполнение данных пользователя для регистрации
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys('')
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(random_email)
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[3]/div/div/input').send_keys(random_password)

    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/button').click()

    #Проверка, что после нажатия на "Зарегистрироваться" никуда не перекинет, тк не указано "Имя"
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    driver.quit()

def test_registration_using_incorrect_email(random_email, random_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    WebDriverWait(driver, 3).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/p')))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    #Заполнение данных пользователя для регистрации
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys('test_name')
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys('mail.mail.mail')
    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/fieldset[3]/div/div/input').send_keys(random_password)

    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/button').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    driver.quit()

def test_registration_using_incorrect_password(random_email, random_password):
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
                        '/html/body/div/div/main/div/form/fieldset[3]/div/div/input').send_keys('four')

    driver.find_element(By.XPATH,
                        '/html/body/div/div/main/div/form/button').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(3) > div > p')))
    expected_message = driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(3) > div > p').text
    assert expected_message == "Некорректный пароль"

    driver.quit()