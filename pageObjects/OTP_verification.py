import time
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class otp_verification_page(BaseClass):
    # back button
    OV_back_btn_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]")
    # OTP Verification label text
    OV_OTP_Verification_labbel_text_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[1]/text()")

    # OTP send to label text "OTP sent to"
    OV_label_text_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/h4[1]/div[1]")
    # "Please Enter 4 Digit OTP" label txt
    OV_intruction_label_text_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/h2[1]")

    # OTP BOX
    OV_otp_box_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div[1]/div/input")
    OV_first_OTP_box_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div[1]/div[1]/input")
    OV_second_OTP_box_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div[1]/div[2]/input")
    OV_third_OTP_box_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div[1]/div[3]/input")
    OV_fourth_OTP_box_xpath = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div[1]/div[4]/input")

    # submit button
    OV_verify_otp_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[4]/button[1]")

    # verify error message after entering wrong otp
    OV_error_text_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]")

    # resend OTP button
    OV_resend_OTP_link_xpath = (By.XPATH, "//h4[contains(text(),'Resend OTP')]")

    def __init__(self, driver):
        self.driver = driver

    # back button is displayed
    def back_btn_displayed(self):
        log = self.getLogger()
        bact_btn = self.driver.find_element(*otp_verification_page.OV_back_btn_xpath)
        try:
            if bact_btn.is_displayed():
                print("back button  is displayed")
                log.info("***Back button is displayed***")
            else:
                print("back button is not displayed")
                log.info("***Back Button is not displayed***")
        except Exception as e:
            log.error(f'Error while checking if Back button is displayed: {e}')

    # click on back button
    def click_back_btn(self):
        log = self.getLogger()
        otp_back_btn = self.driver.find_element(*otp_verification_page.OV_back_btn_xpath)
        try:
            otp_back_btn.click()
            log.info("***back button is clickable***")
        except Exception as e:
            log.error(f'Error while checking if Back button is clickable: {e}')

    # OTP send to label text "OTP sent to"
    def label_text_displayed(self):
        label_text = self.driver.find_element(*otp_verification_page.OV_label_text_xpath)
        try:
            if label_text.is_displayed():
                print("OTP sent to text is displayed")
            else:
                print("OTP sent to text is not displayed")
                assert False
        except Exception as e:
            print(e)

    # "Please Enter 4 Digit OTP" label txt is displayed
    def intruction_label_text_displayed(self):
        log = self.getLogger()
        instruction_label_text = self.driver.find_element(*otp_verification_page.OV_intruction_label_text_xpath)
        actual_text = instruction_label_text.text
        expt_text = "Please Enter 4 Digit OTP "
        try:
            if instruction_label_text.is_displayed():
                print("Please Enter 4 Digit OTP label txt is displayed")
                log.info("***Please Enter 4 Digit OTP label txt is displayed***")
                if expt_text.strip() == actual_text:
                    print("Please Enter 4 Digit OTP label txt is matched")
                    log.info("***Please Enter 4 Digit OTP label txt is matched***")
                else:
                    print("Please Enter 4 Digit OTP label txt is not matched")
            else:
                print("Please Enter 4 Digit OTP label txt is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if Please Enter 4 Digit OTP label txt is displayed: {e}')

    # enter otp in otp box
    def enter_otp(self, otp):
        otp_box = [
            self.driver.find_element(*otp_verification_page.OV_first_OTP_box_xpath),
            self.driver.find_element(*otp_verification_page.OV_second_OTP_box_xpath),
            self.driver.find_element(*otp_verification_page.OV_third_OTP_box_xpath),
            self.driver.find_element(*otp_verification_page.OV_fourth_OTP_box_xpath)
        ]
        for i, digit in enumerate(otp):
            if i < len(otp_box):  # Check if the index is within bounds
                otp_box[i].clear()  # Clear any existing text (optional)
                otp_box[i].send_keys(digit)

    # verify otp button status
    def is_verify_otp_button_enabled(self):
        verify_otp_button = self.driver.find_element(*otp_verification_page.OV_verify_otp_btn_xpath)
        return verify_otp_button.is_enabled()

    # click on verify otp button
    def click_verify_otp_btn(self):
        log = self.getLogger()
        click_verify_otp = self.driver.find_element(*otp_verification_page.OV_verify_otp_btn_xpath)
        try:
            click_verify_otp.click()
            log.info("*** verify otp button is clickable***")
        except Exception as e:
            log.error(f'Error while checking if verify otp button is clickable: {e}')



    # verify error message after entering wrong otp
    def error_text_displayed(self):
        error_text = self.driver.find_element(*otp_verification_page.OV_error_text_xpath)
        return error_text.text

    def is_resend_otp_button_visible(self):
        try:
            # Wait for the button to be visible and return True if it is
            return self.driver.find_element(*otp_verification_page.OV_resend_OTP_link_xpath) is not None
        except:
            # If there's an exception (e.g., timeout), return False
            return False

    def click_resend_otp_link(self):
        log = self.getLogger()
        click_resend_otp = self.driver.find_element(*otp_verification_page.OV_resend_OTP_link_xpath)
        try:
            click_resend_otp.click()
        except Exception as e:
            log.error(f'Error while checking if resend otp button is clickable: {e}')



