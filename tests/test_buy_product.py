import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from selenium.webdriver.chrome.options import Options



#@pytest.mark.run(order=3)
@allure.description("Test Buy Product 1")
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_product_1()
    cp = Cart_page(driver)
    cp.product_confirmation()
    f = Finish_page(driver)
    f.finish()

    print("Finish Test 1")

    driver.quit()



#@pytest.mark.run(order=1)
@allure.description("Test Buy Product 2")
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_products_2()
    cp = Cart_page(driver)
    cp.product_confirmation_2()
    f = Finish_page(driver)
    f.finish()

    print("Finish Test 2")

    driver.quit()



#@pytest.mark.run(order=3)
@allure.description("Test sel")
def test_sel(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test sel")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.sel()

    print("Finish Test sel")

    driver.quit()


