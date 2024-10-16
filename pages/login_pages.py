from base.base_class import Base
import allure
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://elmart-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_registration_button = "//a[@href='https://elmart-shop.ru/login']"
    email_login = "//input[@id='login-email']"
    password = "//input[@id='login-pass']"
    login_button = "//button[@class='le-button huge']"
    main_word = "//a[contains(text(), 'Личный кабинет')]"

    # Getters
    # Actions
    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_element(self.login_registration_button)
            self.input_value(self.email_login, "karpov.sti@bk.ru")
            self.input_value(self.password, "Test808")
            self.click_element(self.login_button)
            self.assert_title(self.main_word, "Личный кабинет")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
