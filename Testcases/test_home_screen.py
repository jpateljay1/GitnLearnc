import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.login_screen import Login_page
from pageObjects.home_screen import home_page
from utilities.BaseClass import BaseClass


class Test_Home_page(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/")
        self.driver.maximize_window()
        LS = Login_page(self.driver)
        LS.enter_text_admission_number_textfield('TP2023045')
        LS.enter_text_password_textfield('test@123')
        LS.click_login_btn()
        time.sleep(10)

    # login to nLearn and home page text verified
    def test_login_and_home_page_url(self):
        log = self.getLogger()
        HS = home_page(self.driver)
        expt_text = "Pick A Subject To Learn"
        actual_text = HS.pick_A_Subject_To_Learn_title()
        if expt_text == actual_text:
            print("user is on home page")
            assert True
        else:
            print("user is not on home page")
            assert False

    # ui elements on home page
    def test_ui_elements(self):
        ui_elements = home_page(self.driver)
        ui_elements.nLearn_logo_displayed()  # nLearn logo is displayed
        ui_elements.welcome_text_displayed()  # Welcome text is displayed or not
        ui_elements.dropdown_btn_displayed()  # dropdown button is displayed
        ui_elements.notification_btn_displayed()
        ui_elements.profile_icon_displayed()
        ui_elements.schedule_left_nav_btn_displayed()
        ui_elements.learn_Left_nav_btn_displayed()
        ui_elements.library_left_nav_btn_displayed()
        ui_elements.practice_left_nav_btn_displayed()
        ui_elements.assignments_left_nav_btn_displayed()
        ui_elements.HS_doubt_solving_left_nav_btn_displayed()
        ui_elements.tests_left_nav_btn_displayed()
        ui_elements.activities_left_nav_btn_displayed()
        ui_elements.term_exams_left_nav_btn_displayed()
        ui_elements.analytics_left_nav_btn_displayed()
        ui_elements.continue_from_where_you_left_text_displayed()
        ui_elements.learn_videos_nav_btn_displayed()

    # click on schedule left nav button
    def test_click_schedule_left_nav_btn(self):
        log = self.getLogger()
        HS = home_page(self.driver)
        HS.click_schedule_left_nav_bar()
        time.sleep(5)
        actual_text = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Schedule')]").text
        expt_text = "Schedule"
        if actual_text == expt_text:
            print("schedule left nav button is clickable ")
            log.info("***schedule nav btn is clickable***")
        else:
            print("schedule left nav button is not clickable ")
            log.info("***test fails***")

    # click on Learn left nav button
    def test_click_Learn_left_nav_btn(self):
        log = self.getLogger()
        HS = home_page(self.driver)
        HS.click_Learn_left_nav_bar()
        time.sleep(5)
        actual_text = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Topics']").text
        expt_text = "Topics"
        if actual_text == expt_text:
            print("Learn left nav button is clickable ")
            log.info("***Learn nav btn is clickable user navigate to learn page***")
        else:
            print("Learn left nav button is not clickable ")
            log.info("***test fails***")



    # After clicking on first carousel button first carrousel image is displayed
    def test_first_carousel_image_displayed(self):
        HS = home_page(self.driver)
        HS.first_cursl_pointer_btn_click()
        img = HS.first_cursl_img_displayed()
        self.assertTrue(img, "The carousel image is not displayed after clicking the button.")

    def test_second_carousel_image_displayed(self):
        HS = home_page(self.driver)
        HS.second_cursl_pointer_btn_click()
        img = HS.second_cursl_img_displayed()
        self.assertTrue(img, "The carousel image is not displayed after clicking the button.")

    def test_click_learn_videos_nav_btn(self):
        HS = home_page(self.driver)
        HS.click_learn_videos_nav_btn()

    def test_click_practice_nav_btn(self):
        HS = home_page(self.driver)
        HS.click_practice_nav_btn()

    def test_click_subject_card_1(self):
        log = self.getLogger()
        HS = home_page(self.driver)
        HS.click_subject_card_1()
        time.sleep(5)
        actual_text = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Topics')]").text
        if actual_text == "Topics":
            log.info("***subject card 1 is clickable and user navigate to learn module***")
            assert True
        else:
            log.info("***subject card 1 is clickable****")
            assert False


if __name__ == '__main__':
    unittest.main()
