from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Forgot_passwrd_page(BaseClass):
    # nLearn logo in forgot password page
    FP_nLearnlogo_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/img[1]")

    # back button in forgot password page
    FP_forgot_pwd_back_btn_xpath = (By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]")
    # No Worries! To reset your password, please enter your admission number. text
    FP_no_worries_text_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]")
    # Admission label text
    FP_admission_number_label_txt_xpath = (By.XPATH, "//input[@id='textInput']")
    # Admission number text field
    FP_admission_number_textfield_xpath = (By.XPATH, "//input[@id='textInput']")
    # submit button
    FP_submit_btn_xpath = (By.XPATH, "//span[.='Submit']")
    # error message below admission number textfield
    FP_error_text1_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]")

    def __init__(self, driver):
        self.driver = driver

    # nLearn logo in forgot password page is displayed
    def nLearn_logo(self):
        log = self.getLogger()
        nLearn_logo = self.driver.find_element(*Forgot_passwrd_page.FP_nLearnlogo_xpath)
        try:
            if nLearn_logo.is_displayed():
                print("nLearn logo in forgot password page is displayed")
                log.info("***nLearn logo in forgot password page is displayed****")
                assert True
            else:
                print("nLearn logo  in forgot password page is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the nLearn logo in forgot password page is displayed: {e}')

    # back button in forgot password page
    def back_button_displayed(self):
        log = self.getLogger()
        forgot_password_back_btn = self.driver.find_element(*Forgot_passwrd_page.FP_forgot_pwd_back_btn_xpath)
        try:
            if forgot_password_back_btn.is_displayed():
                print("back button in forgot password page is displayed")
                log.info("***back button in forgot password page is displayed***")
                assert True
            else:
                print("back button in forgot password page is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the back button in forgot password page is displayed: {e}')

    # click on back button in forgot password page
    def click_back_button(self):
        log = self.getLogger()
        forgot_password_back_btn = self.driver.find_element(*Forgot_passwrd_page.FP_forgot_pwd_back_btn_xpath)
        try:
            forgot_password_back_btn.click()
            log.info("****back button in forgot password page is clickable****")
        except Exception as e:
            log.error(f'Error while checking if the back button in forgot password page is clickable: {e}')

    # "No Worries! To reset your password, please enter your admission number." text is displayed.
    def no_worries_text_displayed(self):
        log = self.getLogger()
        no_worries_text = self.driver.find_element(*Forgot_passwrd_page.FP_no_worries_text_xpath)
        actual_text = no_worries_text.text
        expt_text = "No Worries! To reset your password, please enter your admission number."
        try:
            if no_worries_text.is_displayed():
                print("no worries label text is displayed" + actual_text)
                log.info(
                    "****No Worries! To reset your password, please enter your admission number text is displayed****")
                if expt_text.strip() == actual_text:
                    print("no worries text matched")
                    log.info(
                        "***No Worries! To reset your password, please enter your admission number text is matched***")
                else:
                    print("no worries text not matched")
            else:
                print("no worries text is not displayed")
                assert False
        except Exception as e:
            log.error(
                f'Error while checking if the No Worries! To reset your password, please enter your admission number text is displayed: {e}')

    # Admission number label text is displayed
    def admission_no_label_text_displayed(self):
        log = self.getLogger()
        admission_no_label_text = self.driver.find_element(*Forgot_passwrd_page.FP_admission_number_label_txt_xpath)
        actual_text = admission_no_label_text.text
        expt_text = "Admission Number"
        try:
            if admission_no_label_text.is_displayed():
                print("Admission Number label text is displayed" + actual_text)
                if expt_text.strip() == actual_text:
                    print("Admission Number text matched")
                    log.info("***Admission Number label text is displayed***")
                else:
                    print("Admission Number text not matched")
            else:
                print("Admission Number text is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Admission Number label text is displayed: {e}')

    # admission number textfield is displayed
    def admission_no_txtfield(self):
        log = self.getLogger()
        admission_number = self.driver.find_element(*Forgot_passwrd_page.FP_admission_number_textfield_xpath)
        try:
            if admission_number.is_displayed():
                print("admission number textfield is displayed")
                log.info("****Admission number textfield is displayed****")
                assert True
            else:
                print("admission number textfield is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Admission Number textfield is displayed: {e}')

    # enter text in admission number text field
    def enter_text_admission_number_textfield(self, admno: str):
        log = self.getLogger()
        admission_textfield = self.driver.find_element(*Forgot_passwrd_page.FP_admission_number_textfield_xpath)
        try:
            admission_textfield.clear()
            admission_textfield.send_keys(admno)
            log.info("****successfully entered admission number in admission number textfield****")
        except Exception as e:
            log.error(
                f'Error while checking if user is able to enter admission number in admission number textfield: {e}')

    def click_submit_btn(self):
        log = self.getLogger()
        submit_btn = self.driver.find_element(*Forgot_passwrd_page.FP_submit_btn_xpath)
        try:
            submit_btn.click()
            log.info("****Submit button is clickable after entering admission number****")
        except Exception as e:
            log.error(
                f'Error while checking if user is able to click on submit button after entering admission number: {e}')


    # submit button status
    def is_submit_button_enabled(self):
        submit_button = self.driver.find_element(*Forgot_passwrd_page.FP_submit_btn_xpath)
        return submit_button.is_enabled()

    # "This admission number doesn't exist" error text
    def error_message_text_display(self):
        error_text = self.driver.find_element(*Forgot_passwrd_page.FP_error_text1_xpath)
        return error_text.text
