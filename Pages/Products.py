from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Product:
    def __init__(self, driver):
        self.driver = driver
        self.filter = (By.CSS_SELECTOR, 'select[class="product_sort_container"]')
        self.onesie = (By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-onesie"]')
        self.bike_light = (By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-bike-light"]')


    def click_filter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.filter)
        )
        self.driver.find_element(*self.filter).click()

    def select_filter(self, filter_by):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.filter)
        )
        select = Select(self.driver.find_element(*self.filter))
        select.select_by_value(filter_by)

    def select_product_onesie(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie)
        )
        self.driver.find_element(*self.onesie).click()

    def select_product_bike_light(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bike_light)
        )
        self.driver.find_element(*self.bike_light).click()