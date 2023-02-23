from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Info:
    def __init__(self, driver):
        self.driver = driver
        self.f_name = (By.CSS_SELECTOR, 'input[id="first-name"]')
        self.l_name = (By.CSS_SELECTOR, 'input[id="last-name"]')
        self.z_code = (By.CSS_SELECTOR, 'input[id="postal-code"]')
        self.continue_button = (By.CSS_SELECTOR, 'input[class="submit-button btn btn_primary cart_button btn_action"]')

    def first_name(self, first):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.f_name)
        )
        (self.driver.find_element(*self.f_name)).send_keys(first)

    def last_name(self, last):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.l_name)
        )
        self.driver.find_element(*self.l_name).send_keys(last)

    def zip_code(self, zip):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.z_code)
        )
        self.driver.find_element(*self.z_code).send_keys(zip)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        self.driver.find_element(*self.continue_button).click()