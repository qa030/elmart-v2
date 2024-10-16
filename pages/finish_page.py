import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout = "//a[@class='le-button big']"

    # Getters

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    # Actions
    # Methods

    def finish(self):
        with allure.step("Finish"):
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/cart')
            self.move_to_element(self.get_checkout)
            self.get_screenshot()
