import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.Learn_Screen import Learn_page
from pageObjects.home_screen import home_page
from pageObjects.login_screen import Login_page
from utilities.BaseClass import BaseClass


class Test_learn_page(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/")
        self.driver.maximize_window()
        LS = Login_page(self.driver)
        LS.enter_text_admission_number_textfield('TP2023045')
        LS.enter_text_password_textfield('test@123')
        LS.click_login_btn()
        HS = home_page(self.driver)
        HS.click_Learn_left_nav_bar()

    def test_click_dropdown_btn_displayed(self):
        log = self.getLogger()
        LS = Learn_page(self.driver)
        LS.dropdown_btn_clicked()
        assert True
