import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class Base():


    def __init__(self, driver):
        self.driver = driver


    """Method get current url, получение текущего url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        # print("Current url + get_urk")
        print(f"Current url {get_url}")


    """Method assert word, проверка авторизации по слову """
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверка по слову успешна")


    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        #self.driver.save_screenshot('C:\\Users\Серёга\\PycharmProjects\\main_project_s\\screen\\' + name_screenshot)
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")


    """Method assert url, проверка по url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good Value Url")


    """Method наведения на элемент"""
    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        # action.move_to_element(self.get_menu_gl().perform())
        ActionChains(self.driver).move_to_element(locator()).perform()

        print("Наводимся на элемент")


    """Method скролинг"""
    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
        print("Скроллинл страницы")


    """Method перемещиние ползунка"""
    def moving_the_slider(self, elem, x, y):
        action = ActionChains(self.driver)
        action.click_and_hold(elem).move_by_offset(x, y).release().perform()
        print("Передвигаем ползунок")


    """Method клик"""
    def click_element(self, locator):
        elem = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        print("Нажать на элемент")
        return elem.click()



    """Метод получения текста элемента"""
    def get_text(self, locator):
        elem = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return elem.text


    """Method ввода"""
    def input_value(self, locator, value):
        elem = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        elem.send_keys(value)
        print("Ввести значение")


    """Method получение элемента"""
    def get(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))


    """Method проверки цены"""
    def assert_price(self, locator, price):
        price_1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert (price_1.text.replace('₽', '').replace(' ', '')) == price
        print("Проверка цены успешна")


    """Method проверки по слову"""
    def assert_title(self, locator, title):
        title_1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert title_1.text == title
        print("Проверка по слову успешна")



