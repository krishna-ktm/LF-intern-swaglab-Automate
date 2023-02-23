from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OView:
    def __init__(self, driver):
        self.driver = driver
        self.finish = (By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium cart_button"]')

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish)
        )
        self.driver.find_element(*self.finish).click()