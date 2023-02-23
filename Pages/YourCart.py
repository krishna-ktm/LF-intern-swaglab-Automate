from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
        self.remove = (By.CSS_SELECTOR, 'button[id="remove-sauce-labs-bike-light"]')
        self.checkout = (By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium checkout_button"]')

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        self.driver.find_element(*self.cart_icon).click()

    def remove_item_bike_light(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove)
        )
        self.driver.find_element(*self.remove).click()

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout)
        )
        self.driver.find_element(*self.checkout).click()