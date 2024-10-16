# import pytest
#
#
# @pytest.fixture()
# def set_up():
#     print("Start test")
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#     url = 'https://www.saucedemo.com/'
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#
#     yield
#
#     driver.quit()
#     print("Finish test")

# или

# import pytest
#
#
# @pytest.fixture()
# def set_up() -> Generator[WebDriver, None, None]:
#     print("\nStart test\n")
#     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#     #url = 'https://www.saucedemo.com/'
#     #self.driver.get(self.url)
#     self.driver.maximize_window()
#     yield driver
#     print("\nFinish test\n")
#



# """"variant 2"""""
#
# import pytest
#
#
# @pytest.fixture()
# def set_up():
#     print("Start test")
#     yield
#     print("Finish test")



""" Запуск теста с параметром scope"""

import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")