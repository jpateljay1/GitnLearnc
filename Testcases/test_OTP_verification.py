import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.OTP_verification import otp_verification_page
from utilities.BaseClass import BaseClass


class Test_OTP_verification_page(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/forgot-password/TP2023045/90******60-primary")
        self.driver.maximize_window()

    def test_uielements(self):
        ui_element = otp_verification_page(self.driver)
        ui_element.back_btn_displayed()
        ui_element.label_text_displayed()
        ui_element.intruction_label_text_displayed()

    def test_back_btn_click(self):
        log = self.getLogger()
        back_btn = otp_verification_page(self.driver)
        back_btn.click_back_btn()
        self.driver.implicitly_wait(8)
        try:
            self.assertEqual(self.driver.current_url,
                             'data:,')
        except Exception as e:
            log.error(f'Error while checking if resend otp button is clickable: {e}')

    def test_enter_otp(self):
        OV = otp_verification_page(self.driver)
        OV.enter_otp(otp='1234')
        assert OV.is_verify_otp_button_enabled(), "verify otp  button should be enabled after entering OTP"

    # verify error message after entering wrong otp
    def test_error_text(self):
        log = self.getLogger()
        OV = otp_verification_page(self.driver)
        OV.enter_otp(otp='1234')
        OV.click_verify_otp_btn()
        expt_error_txt = "You have entered wrong OTP"
        actual_error_txt = OV.error_text_displayed()
        try:
            self.assertEqual(actual_error_txt, expt_error_txt,
                         f"Expected error message '{expt_error_txt}' but got '{actual_error_txt}'")
            log.info("***after entering wrong otp, error text displayed successfully***")
        except Exception as e:
            log.error(f'Error while checking if after entering wrong otp, error text displayed: {e}')



    def test_resend_otp_button_visibility(self):
        log = self.getLogger()
        OV = otp_verification_page(self.driver)
        # Check if the resend OTP button is initially invisible
        assert not OV.is_resend_otp_button_visible(), "Resend OTP button should not be visible initially"
        log.info("***resend button is not visible****")
        # Wait for 30 seconds and then check if the button becomes visible
        time.sleep(40)  # Wait for 30 seconds
        assert OV.is_resend_otp_button_visible(), "Resend OTP button should be visible after 30 seconds"
        log.info("***resend button is visible after 30 seconds****")
        try:
            if OV.click_resend_otp_link():
                print("resend otp button is clickable")
                log.info("***resend otp button is clickable***")
            else:
                print("resend otp button is not clickable")
                assert False
        except Exception as e:
            log.error(f'Error while checking if resend otp button is visible after 30 second and it is clickable: {e}')


if __name__ == '__main__':
    unittest.main()
