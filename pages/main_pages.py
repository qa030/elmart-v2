import allure
from selenium.webdriver import Keys
from base.base_class import Base
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger



class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    menu_gl = "(//a[@class='dropdown-toggle'])[7]"
    coffee_makers = "//a[@href='/catalog/category/kofevarki']"
    price = "(//div[@class='slider-handle'])[1]"
    price_max = "//input[@name='price-max']"
    apply_filters_button = "//button[@class='btn btn-primary btn-block']"
    delonghi = "//img[@alt='Delonghi ECAM350.55.B']"
    select_cart_product_1 = "//a[@data-id='21421']"
    close_button = "(//button[contains(text(),'Закрыть')])[2]"

    menu_gl_2 = "(//a[@class='dropdown-toggle'])[16]"
    thermos = "//a[@href='/catalog/category/termosy']"
    manufacturer = "/html/body/div[1]/section/div/div/div[2]/div/div[2]/div/div/form/div[1]/ul/li[7]"
    sentore = "(//div[@class='product-item'])[2]"
    select_cart_product_2 = "//a[@data-id='38500']"

    appliances = "//a[@data-id='1']"
    robot_vacuum_cleaners = "//a[@data-id='435']"
    price_lef = "(//div[@class='slider-handle'])[2]"
    xiaomi_s10 = "//img[@alt='XIAOMI Mi Robot Vacuum S10+']"
    select_cart_product_3 = "//a[@data-id='48633']"

    discounts = "//a[@href='/catalog/discounts']"
    word_discount = "//h1[@class='section-title']"


    # Getters

    def get_menu_gl(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_gl)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_delonghi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delonghi)))



    def get_menu_gl_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_gl_2)))

    def get_sentore(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sentore)))

    def get_price_lef(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_lef)))

    def get_xiaomi_s10(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi_s10)))


    # Actions

    def clear_price_max(self, price_max):
        self.get_price_max().send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        print("Очистить поле максимального значения")


    # Methods

    def select_product_1(self):
        with allure.step("Select Product"):
            Logger.add_start_step(method="select_product_1")
            self.get_current_url()
            self.move_to_element(self.get_menu_gl)
            self.get(self.coffee_makers)
            self.click_element(self.coffee_makers)
            self.scroll_page(0, 1500)
            self.moving_the_slider(self.get_price(), 50, 0)
            self.clear_price_max(self.get_price_max)
            self.input_value(self.price_max, "105000")
            self.click_element(self.apply_filters_button)
            self.scroll_page(0, 700)
            self.move_to_element(self.get_delonghi)
            self.click_element(self.select_cart_product_1)
            Logger.add_end_step(url=self.driver.current_url, method="select_product_1")

    def select_products_2(self):
        with allure.step("Select Product 2"):
            Logger.add_start_step(method="select_product_2")
            self.get_current_url()
            self.move_to_element(self.get_menu_gl_2)
            self.click_element(self.thermos)
            self.scroll_page(0, 1100)
            self.click_element(self.manufacturer)
            self.move_to_element(self.get_sentore)
            self.click_element(self.select_cart_product_2)
            self.click_element(self.close_button)
            self.click_element(self.appliances)
            self.click_element(self.robot_vacuum_cleaners)
            self.scroll_page(0, 1500)
            self.moving_the_slider(self.get_price(), 60, 0)
            self.moving_the_slider(self.get_price_lef(), -60, 0)
            self.click_element(self.apply_filters_button)
            self.move_to_element(self.get_xiaomi_s10)
            self.click_element(self.select_cart_product_3)
            Logger.add_end_step(url=self.driver.current_url, method="select_product_2")

    def sel(self):
        with allure.step("Select sel"):
            Logger.add_start_step(method="sel")
            self.get(self.discounts)
            self.click_element(self.discounts)
            self.assert_title(self.word_discount, "Товары со скидкой")
            Logger.add_end_step(url=self.driver.current_url, method="sel")


