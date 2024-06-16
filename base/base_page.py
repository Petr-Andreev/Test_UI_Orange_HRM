from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    #Функция, которая будет открывать веб страницу
    def open(self):
        self.driver.get(self.PAGE_URL)

    # Функция, которая будет проверять, что веб страница действительно открылась
    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))
