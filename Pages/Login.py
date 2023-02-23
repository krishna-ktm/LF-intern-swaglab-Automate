from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserLogin:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.CSS_SELECTOR, 'input[type="text"]')
        self.password = (By.CSS_SELECTOR, 'input[type="password"]')
        self.login_button = (By.CSS_SELECTOR, 'input[class="submit-button btn_action"]')

    def set_username(self, user):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username)
        )
        self.driver.find_element(*self.username).send_keys(user)

    def set_password(self, passw):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password)
        )
        self.driver.find_element(*self.password).send_keys(passw)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        self.driver.find_element(*self.login_button).click()