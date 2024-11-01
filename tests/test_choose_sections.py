from selenium.webdriver.common.by import By
from locators import main_page_select_sauce, main_page_select_filling, main_page_select_sauce_up, \
    main_page_select_bun_up, main_page_select_filling_up, selected_value_not_this, selected_this_one
from urls import main_page


class TestSelections:

    def test_selections_sauce(self, driver):
        driver.get(main_page)
        driver.find_element(By.XPATH, main_page_select_sauce).click()

        expected_value_first_field = driver.find_element(By.XPATH, main_page_select_bun_up).get_attribute('class')
        expected_value_second_field = driver.find_element(By.XPATH, main_page_select_sauce_up).get_attribute('class')
        expected_value_third_field = driver.find_element(By.XPATH, main_page_select_filling_up).get_attribute('class')

        assert expected_value_first_field == selected_value_not_this
        assert expected_value_second_field == selected_this_one
        assert expected_value_third_field == selected_value_not_this

    def test_selections_filling(self, driver):
        driver.get(main_page)
        driver.find_element(By.XPATH, main_page_select_filling).click()

        expected_value_first_field = driver.find_element(By.XPATH, main_page_select_bun_up).get_attribute('class')
        expected_value_second_field = driver.find_element(By.XPATH, main_page_select_sauce_up).get_attribute('class')
        expected_value_third_field = driver.find_element(By.XPATH, main_page_select_filling_up).get_attribute('class')

        assert expected_value_first_field == selected_value_not_this
        assert expected_value_second_field == selected_value_not_this
        assert expected_value_third_field == selected_this_one

    def test_selections_bun(self, driver):
        driver.get(main_page)
        expected_value_first_field = driver.find_element(By.XPATH, main_page_select_bun_up).get_attribute('class')
        expected_value_second_field = driver.find_element(By.XPATH, main_page_select_sauce_up).get_attribute('class')
        expected_value_third_field = driver.find_element(By.XPATH, main_page_select_filling_up).get_attribute('class')

        assert expected_value_first_field == selected_this_one
        assert expected_value_second_field == selected_value_not_this
        assert expected_value_third_field == selected_value_not_this
