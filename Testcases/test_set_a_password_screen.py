import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.set_a_password_screen import Set_a_password_page
from utilities.BaseClass import BaseClass


class Test_set_a_password_page(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/forgot-password/TP2023045/90******60-primary/set")
        self.driver.maximize_window()

    def test_uielements(self):
        ui_elements = Set_a_password_page(self.driver)
        ui_elements.nLearn_logo_displayed()
        ui_elements.set_a_password_title_displayed()
        ui_elements.instruction_text_displayed()
        ui_elements.new_password_label_text_displayed()
        ui_elements.new_password_textfield_displayed()
        ui_elements.eye_button_in_new_password_textfield_displayed()
        ui_elements.verify_new_password_label_text_displayed()
        ui_elements.eye_button_in_verify_new_password_textfield_displayed()
        ui_elements.update_password_btn_displayed()

    def test_enter_pwd_in_new_password_textfield(self):
        log = self.getLogger()
        SP = Set_a_password_page(self.driver)
        SP.enter_text_in_new_password_text_field(new_pwd='test@123')

    # error text after enter password in new password textfield less than 6 character  "Password should be minimum 6 characters"
    def test_error_text_after_entering_pwd_less_than_6char(self):
        SP = Set_a_password_page(self.driver)
        SP.enter_text_in_new_password_text_field(new_pwd='test@')
        expt_error_txt = "Password should be minimum 6 characters"
        actual_error_txt = SP.error_text1_displayed()
        self.assertEqual(actual_error_txt, expt_error_txt,
                         f"Expected error message '{expt_error_txt}' but got '{actual_error_txt}'")

    # error text below verify new password textfield after entering password in new password text field "Confirm password and new password should be same"
    def test_error_test_after_entering_new_pwd_more_than_6char(self):
        SP = Set_a_password_page(self.driver)
        SP.enter_text_in_new_password_text_field(new_pwd='test@1')
        expt_error_txt = "Confirm password and new password should be same"
        actual_error_txt = SP.error_text2_displayed()
        self.assertEqual(actual_error_txt, expt_error_txt,
                         f"Expected error message '{expt_error_txt}' but got '{actual_error_txt}'")

    # enter password in verify new password text field
    def test_enter_pwd_in_verify_new_password_textfield(self):
        SP = Set_a_password_page(self.driver)
        SP.enter_text_in_verify_new_password_text_field(verify_new_pwd='test@123')

    # verify that after entering same password in new password and verify new password textfield, update password button enables
    def test_update_password_button_enabled(self):
        SP = Set_a_password_page(self.driver)
        new_pwd = SP.enter_text_in_new_password_text_field(new_pwd='test@123')
        verify_new_pwd = SP.enter_text_in_verify_new_password_text_field(verify_new_pwd='test@123')
        if new_pwd == verify_new_pwd:
            self.assertTrue(SP.is_update_password_button_enabled(),
                            "Update Password button should be enabled when passwords match.")
        else:
            print("Update Password button is disabled")

    # verify that after entering same password in new password and verify new password textfield,click on update password button
    def test_update_password_button_click(self):
        SP = Set_a_password_page(self.driver)
        new_pwd = SP.enter_text_in_new_password_text_field(new_pwd='test@123')
        verify_new_pwd = SP.enter_text_in_verify_new_password_text_field(verify_new_pwd='test@123')
        if new_pwd == verify_new_pwd:
            SP.update_password_button_click()
            print("password successfully changed")
        else:
            print("password not changed")


if __name__ == '__main__':
    unittest.main()
