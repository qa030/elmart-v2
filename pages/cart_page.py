import allure
from base.base_class import Base



class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    cart_button = "//a[@class='btn btn-primary']"
    test_word_1 = "//a[@href='/catalog/product/delonghi-ecam350.55.b']"
    price_product_1 = "(//div[@class='price'])[2]"
    test_word_2 = "//a[@href='/catalog/product/sentore-hc-450-grey']"
    price_product_2 = "(//div[@class='price'])[3]"
    test_word_3 = "//a[@href='/catalog/product/xiaomi-mi-robot-vacuum-s10']"
    price_product_3 = "(//div[@class='price'])[4]"


    # Getters
    # Actions
    # Methods

    def product_confirmation(self):
        with allure.step("Product Confirmation"):
            self.get_current_url()
            self.click_element(self.cart_button)
            self.assert_title(self.test_word_1, "Delonghi ECAM350.55.B")
            self.assert_price(self.price_product_1, "80254")



    def product_confirmation_2(self):
        with allure.step("Product Confirmation 2"):
            self.click_element(self.cart_button)
            self.assert_title(self.test_word_2, "SENTORE HC-450 Grey")
            self.assert_price(self.price_product_2, "668")
            self.assert_title(self.test_word_3, "XIAOMI Mi Robot Vacuum S10+")
            self.assert_price(self.price_product_3, "35688")



