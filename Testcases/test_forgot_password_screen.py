import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.forgot_password_screen import Forgot_passwrd_page
from utilities.BaseClass import BaseClass


class Test_forgot_password_page(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/forgot-password")
        self.driver.maximize_window()

    def test_uielements_forgotpassword_page(self):
        ui_element = Forgot_passwrd_page(self.driver)
        ui_element.nLearn_logo()
        ui_element.back_button_displayed()
        ui_element.no_worries_text_displayed()
        ui_element.admission_no_txtfield()

    def test_click_back_btn_forgot_password_page(self):
        log = self.getLogger()
        back_btn = Forgot_passwrd_page(self.driver)
        back_btn.click_back_button()
        self.assertEqual(self.driver.current_url,
                         'data:,')
        log.info("***after clicking on back button in Forgot Password Page, user navigate to login page****")

    # entering admission number in admission number textfield
    def test_enter_text_admission_number_textfield(self):
        log = self.getLogger()
        admission_number = Forgot_passwrd_page(self.driver)
        try:
            admission_number.enter_text_admission_number_textfield(admno='chandan')
            log.info("***admission number successfully entered in admission number textfield****")
        except Exception as e:
            log.error(
                f'Error while checking if user is able to enter admission number in admission number textfield: {e}')

    # testing submit button status before and after entering admission number
    def test_submit_button_status_before_entering_number(self):
        log = self.getLogger()
        submit_btn = Forgot_passwrd_page(self.driver)
        try:
            is_enabled_before = submit_btn.is_submit_button_enabled()
            # Check if the submit button is initially enabled or disabled
            self.assertTrue(is_enabled_before, "Submit button should be disabled before entering admission number.")
            log.info("***submit button is disable before entering admission number***")
            # enter admission number
            submit_btn.enter_text_admission_number_textfield(admno='chandan')
            log.info("***admission number entered in admission number text field***")
            # Check if the submit button status has changed after entering the admission number
            is_enabled_after = submit_btn.is_submit_button_enabled()
            self.assertFalse(is_enabled_after, "Submit button should be enabled after entering admission number.")
            log.info("***submit button is enabled after entering admission number***")
        except Exception as e:
            log.error(
                f'Error while checking submit button status before and after entering admission number : {e}')


    # verify error text after entering invalid admission number and clicking on submit button
    def test_error_text_display(self):
        log = self.getLogger()
        error_text = Forgot_passwrd_page(self.driver)
        error_text.enter_text_admission_number_textfield(admno="chandan")
        error_text.click_submit_btn()
        actual_error_text = error_text.error_message_text_display()
        expt_error_txt = "This admission number doesn't exist"
        try:
            if expt_error_txt == actual_error_text:
                print("error text displayed and matched after entering invalid admission number")
                log.info("***error text displayed and matched after entering invalid admission number***")
        except Exception as e:
            log.error(
                f'Error while checking after entering invalid admission number, verifying error text : {e}')


    # enter admission number and click on submit button
    def test_valid_admno_click_submit_btn(self):
        log = self.getLogger()
        FP = Forgot_passwrd_page(self.driver)
        FP.enter_text_admission_number_textfield(admno='TP2023045')
        FP.click_submit_btn()
        expt_url = "https://stage-nlearn.nspira.in/forgot-password/TP2023045"
        actual_url = self.driver.current_url
        try:
            assert actual_url == expt_url, f"Expected url: {expt_url}, but got {actual_url}"
            log.info("***after entering valid admission number and clicking on submit button, user navigate to mobile verification page***")
        except Exception as e:
            log.error(
                f'Error while checking after entering valid admission number and clicking on submit button, user navigate to mobile verification page : {e}')




if __name__ == '__main__':
    unittest.main()
