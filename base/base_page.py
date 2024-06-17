from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    #Функция, которая будет открывать веб страницу
    def open(self):
        with allure.step(f'Открытие {self.PAGE_URL} страницы'):
            self.driver.get(self.PAGE_URL)

    # Функция, которая будет проверять, что веб страница действительно открылась
    def is_opened(self):
        with allure.step(f'Страница {self.PAGE_URL} открылась'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    # Создание скриншота
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
