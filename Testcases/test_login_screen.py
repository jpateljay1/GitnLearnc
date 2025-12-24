import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.login_screen import Login_page
from utilities.BaseClass import BaseClass


class Test_login_page(BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage-nlearn.nspira.in/")
        self.driver.maximize_window()
        print(self.driver.title)
        self.driver.implicitly_wait(8)

    def test_uielements(self):
        log = self.getLogger()
        ui_elements = Login_page(self.driver)
        ui_elements.narayana_logo()
        ui_elements.nLearn_logo()
        ui_elements.nLearn_kids_logo()
        ui_elements.welcome_to_narayana_text()
        ui_elements.labeltxtisdisplayed()
        ui_elements.admission_label_text_displayed()
        ui_elements.password_label_text_displayed()
        ui_elements.forgot_password_link_displayed()
        ui_elements.tnc_text_displayed()
        ui_elements.tnc_link_displayed()
        ui_elements.tnc_checkbox_displayed()
        ui_elements.Comprehensive_curriculum_for_all_students_text_displayed()

    def test_login(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield('TP2023045')
        Login.enter_text_password_textfield('test@123')
        Login.click_login_btn()
        actual_text = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Just For You!']").text
        if actual_text == "Just For You!":
            log.info("*****successfully login*****")
            assert True
        else:
            log.info("*****Login Fail*****")
            assert False

    # enter password in password textfield and click on login button and verify error message
    def test_login_with_blank_adm_txtfield(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_password_textfield("test@123")
        Login.click_login_btn()
        expt_error_message1 = "Please enter valid username"
        actual_error_message1 = Login.admno_error_text1()
        try:
            if expt_error_message1 == actual_error_message1:
                print("error message matched" + actual_error_message1)
                log.info("")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    #  login with  invalid admission number and valid password and verify error message
    def test_invalid_admno_valid_pwd(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield("abcdef123")
        Login.enter_text_password_textfield("test@123")
        Login.click_login_btn()
        expt_error_txt = "Admission number is not registered. Please contact your principal"
        actual_error_txt = Login.admno_error_text2()
        try:
            if expt_error_txt == actual_error_txt:
                print("error message matched" + actual_error_txt)
                log.info("****error message successfully and not able to login")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    # login with valid admission number and invalid password  and verify error message
    def test_valid_admno_invalid_pwd(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield("TP2023045")
        Login.enter_text_password_textfield("test@125533")
        Login.click_login_btn()
        expt_error_txt = "Incorrect Password!"
        actual_error_txt = Login.password_error_text2()
        try:
            if expt_error_txt == actual_error_txt:
                print("error message matched" + actual_error_txt)
                log.info("****error message successfully and not able to login")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    # login with invalid admission number and invalid password
    def test_invalid_admno_invalid_pwd(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield("abcd1234")
        Login.enter_text_password_textfield("test@125533")
        Login.click_login_btn()
        expt_error_txt = "Admission number is not registered. Please contact your principal"
        actual_error_txt = Login.admno_error_text2()
        try:
            if expt_error_txt == actual_error_txt:
                print("error message matched" + actual_error_txt)
                log.info("****error message successfully and not able to login")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    # login with invalid admission number and empty  password
    def test_valid_admno_empty_pwd(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield("TP2023045")
        Login.click_login_btn()
        expt_error_txt = "Please enter valid password"
        actual_error_txt = Login.password_error_text1()
        try:
            if expt_error_txt == actual_error_txt:
                print("error message matched" + actual_error_txt)
                log.info("****error message successfully and not able to login")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    # login with invalid admission number and invalid password
    #def test_empty_admno_empty_pwd(self):
    #Login = Login_page(self.driver)
    #Login.click_login_btn()
    #expt_error_txt1 = "Please enter valid username"
    #expt_error_txt2 = "Please enter valid password"
    #actual_error_txt1 = Login.admno_error_text1()
    #actual_error_txt2 = Login.password_error_text1()
    #self.assertEqual(actual_error_txt1, expt_error_txt1,
    #f"Expected error message '{expt_error_txt1}' but got '{actual_error_txt1}'")
    #self.assertEqual(actual_error_txt2, expt_error_txt2,
    #f"Expected error message '{expt_error_txt2}' but got '{actual_error_txt2}'")

    # Enter valid admission number and valid password but change in case sensitivity in admission number text field
    def test_wrong_admno_valid_pwd(self):
        log = self.getLogger()
        Login = Login_page(self.driver)
        Login.enter_text_admission_number_textfield("tp2023045")
        Login.enter_text_password_textfield("test@123")
        Login.click_login_btn()
        expt_error_txt = "Admission number is not registered. Please contact your principal"
        actual_error_txt = Login.admno_error_text2()
        try:
            if expt_error_txt == actual_error_txt:
                print("error message matched" + actual_error_txt)
                log.info("****error message successfully and not able to login")
            else:
                print("error message not matched")
        except:
            log.error("test failed")

    #def test_click_downloadnow_btn(self):
    #Login = Login_page(self.driver)
    #Login.click_download_now_button()
    #Login.scroll_to_available_section()
    #self.assertTrue(Login.is_available_section_displayed(),"Available on all platforms section is displayed")

    #def test_google_btn(self):
    #google_play_btn = Login_page(self.driver)
    #self.assertTrue(google_play_btn.google_play_displayed(), "Google play button not displayed")
    #google_play_btn.click_google_play()
    #self.assertEqual(self.driver.current_url,
    #'https://play.google.com/store/apps/details?id=com.narayanagroup.kids')

    def test_click_forgot_password_link(self):
        log = self.getLogger()
        forgot_password_link = Login_page(self.driver)
        try:
            forgot_password_link.click_forgot_password_link()
            self.assertEqual(self.driver.current_url,
                             'https://stage-nlearn.nspira.in/forgot-password')
            log.info("Forgot Password link is clickable")
        except:
            print("test failed")


if __name__ == '__main__':
    unittest.main()
