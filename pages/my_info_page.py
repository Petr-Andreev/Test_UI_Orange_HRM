import time

import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



class MyInfoPage(BasePage):

    PAGE_URL = Links.MYINFO_PAGE

    FIRST_NAME_FIELD = ('xpath', "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ('xpath', "//input[@name='middleName']")
    LAST_NAME_FIELD = ('xpath', "//input[@name='lastName']")
    SAVE_BUTTON = ('xpath', "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")


    @allure.step("Смена имени в профиле")
    def change_name(self, new_name):
        with allure.step(f"Смена предыдущего имени на '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Смена фамилии в профиле")
    def change_middle_name(self, middle_name):
        with allure.step(f"Смена предыдущего имени на '{middle_name}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.BACKSPACE)
            middle_name_field.send_keys(middle_name)
            self.midname = middle_name

    @allure.step("Смена отчества в профиле")
    def change_last_name(self, last_name):
        with allure.step(f"Смена предыдущего имени на '{last_name}'"):
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
            last_name_field.send_keys(Keys.CONTROL + "A")
            last_name_field.send_keys(Keys.BACKSPACE)
            last_name_field.send_keys(last_name)
            self.lastname = last_name


    @allure.step("Нажатие кнопки Save")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Проверка, смены фио")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.MIDDLE_NAME_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))
        self.wait.until(EC.text_to_be_present_in_element_value(self.MIDDLE_NAME_FIELD, self.midname))
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, self.lastname))

