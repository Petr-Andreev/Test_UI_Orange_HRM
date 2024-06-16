from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USER_NAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    #Находим строчку с логином, нажимаем на неё и вставляет в нее логин
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD)).send_keys(login)

    # Находим строчку с паролем, нажимаем на неё и вставляет в нее пароль
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    # Находим кнопку подтверждения нажимаем на неё
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
