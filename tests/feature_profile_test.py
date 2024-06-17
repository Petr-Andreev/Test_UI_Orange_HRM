from faker import Faker
import allure
import pytest

from base.base_test import BaseTest

fake = Faker()
name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()

@allure.feature('Profile Functionality')
class TestProfileFeature(BaseTest):

    @allure.title("Смена ФИО провиля")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_fio(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.my_info_page.is_opened()
        self.my_info_page.change_name(name)
        self.my_info_page.change_middle_name(middle_name)
        self.my_info_page.change_last_name(last_name)
        self.my_info_page.save_changes()
        self.my_info_page.is_changes_saved()
        self.my_info_page.make_screenshot("Success")
