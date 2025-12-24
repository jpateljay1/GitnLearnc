from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Login_page(BaseClass):
    # narayan logo
    LS_narayana_logo_image_xpath = (By.XPATH, "(//img[@alt='naryana-logo'])[2]")
    # download mow button
    LS_download_now_btn_xpath = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]"
    # nlearn_logo
    LS_nLrean_logo_logo_xpath = (By.XPATH, "(//img[@alt='nlearn-b-logo'])[3]")
    # nLearn kids logo
    LS_nLearnkids_logo_xpath = (By.XPATH, "(//img[@alt='nlearn-b-logo'])[4]")
    # welcome to narayana text
    LS_welecome_text_xpath = (By.XPATH, "//h1[contains(text(),'Welcome to Narayana’s')]")
    # Use login details shared to your registered phone number
    LS_label_txt_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/h6[1]")
    # admission label text
    LS_AdmissionNumber_label_txt_xpath = (By.XPATH, "//h6[.='Admission Number']")
    # admission number textfield
    LS_AdmissionNumber_txt_field_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div["
                                                    "2]/div[1]/form[1]/input[1]")
    # password label text
    LS_Password_label_txt_xpath = (By.XPATH, "//h6[.='Password']")
    # password textfield
    LS_Password_txt_field_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div["
                                             "1]/form[1]/div[1]/input[1]")
    # login button
    LS_login_btn_xpath = (By.XPATH, "//button[normalize-space()='Login']")
    # forgot password link
    LS_forgot_pwd_link_xpath = (By.XPATH, "//h6[.='Forgot password?']")
    # term and condition text
    LS_TnC_txt_xpath = (By.XPATH, "//h2[@class='styles__TermsInfo-sc-1t7da4x-20 jdqTYO']")
    # term and condition link
    LS_TnC_link_xpath = (By.XPATH, "//body/div[@id='app']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form["
                                   "1]/label[1]/h2[1]/h4[1]/a[1]")
    # TnC checkbox
    LS_TnC_chkbox_xpth = (By.XPATH, "//input[@name='terms-check']")

    # error message below admission number textfield
    LS_admno_error_text1_xpath = (
        By.XPATH, "(//span[@class='input-error'])[1]")  # error msg1 "Please enter valid username"
    LS_admno_error_text2_xpath = (By.XPATH,
                                  "(//div[@class='input-error'])[1]")  # error msg2 "Admission number is not registered. Please contact your principal"
    # error message below password textfield
    LS_password_error_text1_xpath = (
        By.XPATH, "//span[@class='input-error']")  # error msg1 "Please enter valid password"
    LS_password_error_text2_xpath = (By.XPATH, "(//div[@class='input-error'])[1]")  # error msg2 "incorrect password"

    # Comprehensive curriculum for all  section
    LS_Comprehensive_curriculum_for_all_students_text_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/h1[1]")
    #  nLearn kids card in Comprehensive curriculum for all students section
    LS_google_play_btn_xpath = (By.XPATH, "//*[@id='app']/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div[1]/a")
    LS_app_store_btn_xpath = (By.XPATH, "//*[@id='app']/div/div[4]/div/div/div[2]/div[1]/div[2]/div/div[2]/a")

    # Available on all platforms section
    LS_Available_on_all_platforms_xpath = (By.XPATH, "//h2[normalize-space()='Available on all platforms']")

    def __init__(self, driver):
        self.driver = driver

    # narayana logo is displayed or not
    def narayana_logo(self):
        log = self.getLogger()
        narayana_logo = self.driver.find_element(*Login_page.LS_narayana_logo_image_xpath)
        try:
            if narayana_logo.is_displayed():
                print("narayana logo is displayed")
                log.info("*****narayana logo is displayed******")
                assert True
            else:
                log.info("narayana logo is not displayed")
                assert False
        except Exception as e:
            log.error(f'Test Fail, narayana logo is not displayed: {e}')

    # nLearn logo is displayed
    def nLearn_logo(self):
        log = self.getLogger()
        nLearn_logo = self.driver.find_element(*Login_page.LS_nLrean_logo_logo_xpath)
        try:
            if nLearn_logo.is_displayed():
                print("nLearn logo is displayed")
                log.info("*****nLearn logo is displayed******")
                assert True
            else:
                print("nLearn logo is not displayed")
                assert False
        except Exception as e:
            log.error(f'Test Fail, nLearn logo is not displayed: {e}')

    # nLearn Kids logo is displayed
    def nLearn_kids_logo(self):
        log = self.getLogger()
        nLearn_kids_logo = self.driver.find_element(*Login_page.LS_nLearnkids_logo_xpath)
        try:
            if nLearn_kids_logo.is_displayed():
                print("nLearn kids logo is displayed")
                log.info("*****nLearn Kids logo is displayed******")

                assert True
            else:
                print("nLearn kids logo is not displayed")
                assert False
        except Exception as e:
            log.error(f'Test Fail, nLearn Kids logo is not displayed: {e}')

    # welcome to narayana text is displayed
    def welcome_to_narayana_text(self):
        log = self.getLogger()
        welcome_to_narayana = self.driver.find_element(*Login_page.LS_welecome_text_xpath)
        actual_text = welcome_to_narayana.text
        expected_text = "Welcome to Narayana’s"
        try:
            if welcome_to_narayana.is_displayed():
                print("welcome message label text is displayed  " + actual_text)
                log.info("******welcome to narayana text displayed*******")
                if expected_text.strip() == actual_text:
                    print("welcome_to_narayana text matched")
                    log.info("******welcome to narayana text matched*******")
                else:
                    print("welcome_to_narayana text not matched")
            else:
                print(" welcome_to_narayana text is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the welcome to narayana text is not displayed: {e}')

    # Use login details shared to your registered phone number label text
    def labeltxtisdisplayed(self):
        log = self.getLogger()
        label_txt = self.driver.find_element(*Login_page.LS_label_txt_xpath)
        actual_text = label_txt.text
        expected_text = "Use login details shared to your registered phone number"
        try:
            if label_txt.is_displayed():
                print("Use login details shared to your registered phone number label text is displayed")
                log.info("******Use login details shared to your registered phone number text displayed*******")
                if expected_text.strip() == actual_text.stript():
                    print("Use login details shared to your registered phone number text matched")
                    log.info("******Use login details shared to your registered phone number text matched*******")
                else:
                    print("Use login details shared to your registered phone number text not matched")
            else:
                print(" Use login details shared to your registered phone number label text is not displayed")
                assert False
        except Exception as e:
            log.error(
                f'Error while checking if the Use login details shared to your registered phone number text is not displayed: {e}')

    # Admission label text is displayed
    def admission_label_text_displayed(self):
        log = self.getLogger()
        admission_label_txt = self.driver.find_element(*Login_page.LS_AdmissionNumber_label_txt_xpath)
        actual_text = admission_label_txt.text
        expected_text = "Admission Number"
        try:
            if admission_label_txt.is_displayed():
                print("Admission Number label text is displayed")
                log.info("******Admission Number label text displayed*******")
                if expected_text.strip() == actual_text:
                    print("Admission Number text matched")
                    log.info("******Admission Number label text matched*******")
                else:
                    print("Admission Number text not matched")
            else:
                print(" Admission Number label text is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Admission Number label text is not displayed: {e}')

    # password label text is displayed
    def password_label_text_displayed(self):
        log = self.getLogger()
        password_label_txt = self.driver.find_element(*Login_page.LS_Password_label_txt_xpath)
        actual_text = password_label_txt.text
        expected_text = "Password"
        try:
            if password_label_txt.is_displayed():
                print("Password label text is displayed")
                log.info("******Password label text displayed*******")
                if expected_text.strip() == actual_text:
                    print("Password text matched")
                    log.info("******Password label text matched*******")
                else:
                    print("Password text not matched")
                    assert False
            else:
                print(" Password label text is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Password label text is not displayed: {e}')

    # forgot password link is displayed.
    def forgot_password_link_displayed(self):
        log = self.getLogger()
        forgot_password_link = self.driver.find_element(*Login_page.LS_forgot_pwd_link_xpath)
        actual_text = forgot_password_link.text
        expected_text = "Forgot password?"
        try:
            if forgot_password_link.is_displayed():
                print("Forgot Password link is displayed")
                log.info("***** forgot password link is displayed******")
                if expected_text.strip() == forgot_password_link.text:
                    print("Forgot Password link matched")
                    log.info("*****Forgot Password link text matched")
                else:
                    print("Forgot Password link not  matched")
                    assert False
            else:
                print("Forgot  Password link is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Forgot Password link text is not displayed: {e}')

    # click on forgot password link
    def click_forgot_password_link(self):
        log = self.getLogger()
        forgot_password_link = self.driver.find_element(*Login_page.LS_forgot_pwd_link_xpath)
        try:
            forgot_password_link.click()
            log.info("Forgot Password link is clickable")
        except Exception as e:
            log.error(f'Error while checking if the Forgot Password link text is clickable  {e}')



    # term and condition text is displayed i.e. "By Proceeding you are automatically accepting to"
    def tnc_text_displayed(self):
        log = self.getLogger()
        tnc_label_txt = self.driver.find_element(*Login_page.LS_TnC_txt_xpath)
        actual_text = tnc_label_txt.text
        expected_text = "By Proceeding you are automatically accepting to T&C and Privacy Policy"
        try:
            if tnc_label_txt.is_displayed():
                print("TnC label text is displayed")
                log.info("****By Proceeding you are automatically accepting to T&C and Privacy Policy text displayed******")
                if expected_text.strip() == actual_text:
                    print("TnC text matched")
                    log.info("****By Proceeding you are automatically accepting to T&C and Privacy Policy text matched******")
                else:
                    print("TnC text not matched")
                    assert False
            else:
                print(" TnC label text is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the By Proceeding you are automatically accepting to T&C and Privacy Policy tex is displayed  {e}')

    # T&C and Privacy Policy link is displayed
    def tnc_link_displayed(self):
        log = self.getLogger()
        tnc_link = self.driver.find_element(*Login_page.LS_TnC_link_xpath)
        actual_text = tnc_link.text
        expected_text = "T&C and Privacy Policy"
        try:
            if tnc_link.is_displayed():
                print("TnC link  is displayed")
                log.info("****T&C and Privacy Policy link text is displayed*****")
                if expected_text.strip() == actual_text:
                    print("TnC link text matched")
                    log.info("*****T&C and Privacy Policy link text matched*****")
                else:
                    print("TnC link text not matched")
                    assert False
            else:
                print(" TnC link is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the T&C and Privacy Policy link text is displayed  {e}')

    # TnC checkbox is displayed
    def tnc_checkbox_displayed(self):
        log = self.getLogger()
        tnc_checkbox = self.driver.find_element(*Login_page.LS_TnC_chkbox_xpth)
        try:
            if tnc_checkbox.is_displayed():
                print("TnC checkbox  is displayed")
                log.info("****TnC checkbox is displayed*****")
            else:
                print(" TnC checkbox is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the T&C checkbox is displayed  {e}')

    # Comprehensive curriculum for all students text is displayed
    def Comprehensive_curriculum_for_all_students_text_displayed(self):
        log = self.getLogger()
        Comprehensive_curriculum_for_all_students_text = self.driver.find_element(
            *Login_page.LS_Comprehensive_curriculum_for_all_students_text_xpath)
        actual_text = Comprehensive_curriculum_for_all_students_text.text
        expected_text = "Comprehensive curriculum for all "
        try:
            if Comprehensive_curriculum_for_all_students_text.is_displayed():
                print("Comprehensive curriculum for all students is displayed")
                log.info("****Comprehensive curriculum for all students text is displayed****")
                if expected_text.strip() == actual_text:
                    print("Comprehensive curriculum for all students text matched")
                    log.info("****Comprehensive curriculum for all students text is matched****")
                else:
                    print("Comprehensive curriculum for all students text not matched")
                    assert False
            else:
                print("Comprehensive curriculum for all students is not displayed")
                assert False
        except Exception as e:
            log.error(f'Error while checking if the Comprehensive curriculum for all students text is displayed  {e}')

    def enter_text_admission_number_textfield(self, admno: str):
        log = self.getLogger()
        admission_textfield = self.driver.find_element(*Login_page.LS_AdmissionNumber_txt_field_xpath)
        try:
            admission_textfield.clear()
            admission_textfield.send_keys(admno)
            log.info("****Admission number successfully entered in admission Number Textfield****")
        except Exception as e:
            log.error(f'Error while checking if Admission Number is successfully entered in Admission Number textfield {e}')



    def enter_text_password_textfield(self, pwd: str):
        log = self.getLogger()
        password_textfield = self.driver.find_element(*Login_page.LS_Password_txt_field_xpath)
        try:
            password_textfield.clear()
            password_textfield.send_keys(pwd)
            log.info("****Password successfully entered in Password textfield*****")
        except Exception as e:
            log.error(f'Error while checking if Password is successfully entered in Password Textfield  {e}')

    def click_login_btn(self):
        log = self.getLogger()
        login_btn = self.driver.find_element(*Login_page.LS_login_btn_xpath)
        try:
            login_btn.click()
            log.info("*****Login button is clickable******")
        except Exception as e:
            log.error(f'Error while checking if Login Button is clickable {e}')



    # error msg1 "Please enter valid username"
    def admno_error_text1(self):
        error_txt1 = self.driver.find_element(*Login_page.LS_admno_error_text1_xpath)
        return error_txt1.text

    # error msg2 "Admission number is not registered. Please contact your principal"
    def admno_error_text2(self):
        error_text2 = self.driver.find_element(*Login_page.LS_admno_error_text2_xpath)
        return error_text2.text

    # error msg1 "Please enter valid password"
    def password_error_text1(self):
        error_text1 = self.driver.find_element(*Login_page.LS_password_error_text1_xpath)
        return error_text1.text

    # error msg2 "incorrect password"
    def password_error_text2(self):
        error_text2 = self.driver.find_element(*Login_page.LS_password_error_text2_xpath)
        return error_text2.text

    # click on download now but  user scroll down to Available on all platforms section
    def click_download_now_button(self):
        download_now_btn = self.driver.find_element(*Login_page.LS_download_now_btn_xpath)
        download_now_btn.click()
        available_section = self.driver.find_element(*Login_page.LS_Available_on_all_platforms_xpath)
        self.driver.execute_script("argument[0].scrollIntoView():", available_section)

    def scroll_to_available_section(self):
        available_section = self.driver.find_element(*Login_page.LS_Available_on_all_platforms_xpath)
        self.driver.execute_script("argument[0].scrollIntoView(true):", available_section)

    def is_available_section_displayed(self):
        return self.driver.find_element(*self.LS_Available_on_all_platforms_xpath)

    # Google play button in nLearn kids card in Comprehensive curriculum for all students section
    def google_play_displayed(self):
        google_play_btn = self.driver.find_element(*Login_page.LS_google_play_btn_xpath)
        return google_play_btn.is_displayed()

    # Click on Google play button in nLearn kids card in Comprehensive curriculum for all students section
    def click_google_play(self):
        click_google_play_btn = self.driver.find_element(*Login_page.LS_google_play_btn_xpath)
        click_google_play_btn.click()
