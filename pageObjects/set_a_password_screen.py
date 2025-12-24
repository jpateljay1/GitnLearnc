from selenium.webdriver.common.by import By


class Set_a_password_page:
    # nLearn logo
    SP_nLearn_logo_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/img[1]")
    # Set a Password title
    SP_Set_a_password_title_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    # Please create a secure new password for a smoother learning journey. instruction text
    SP_instruction_text_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]")
    # new_password label text
    SP_new_password_label_text_xpath = (
        By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/label[1]")
    # new password textfield
    SP_new_password_textfield_xpath = (By.XPATH, "//input[@placeholder='Enter new password']")
    # eye button in new password text field
    SP_eye_button_in_new_password_textfield_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/img[1]")
    # verify new password label text
    SP_verify_new_password_label_text_xpath = (By.XPATH, "//label[contains(text(),'Verify New Password')]")
    # verify new password textfield
    SP_verify_new_password_textfield_xpath = (By.XPATH, "//input[@placeholder='Verify new password']")
    # eye button in verify new password text field
    SP_eye_button_in_verify_new_password_textfield_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/img[1]")

    # error text after enter password in new password textfield less than 6 character
    SP_error_text1_xpath = (By.XPATH, "//div[normalize-space()='Password should be minimum 6 characters']")

    # error text below verify new password textfield after entering password in new password text field
    SP_error_text2_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]")

    # update password button
    SP_update_pssword_btn_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[6]/button[1]/div[1]")
    

    def __init__(self, driver):
        self.driver = driver

    # nLearn logo is displayed
    def nLearn_logo_displayed(self):
        nLearn_logo = self.driver.find_element(*Set_a_password_page.SP_nLearn_logo_xpath)
        try:
            if nLearn_logo.is_displayed():
                print("nLearn logo is displayed")
                assert True
            else:
                print("nLearn logo is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Set a Password title is displayed
    def set_a_password_title_displayed(self):
        set_a_password_title = self.driver.find_element(*Set_a_password_page.SP_Set_a_password_title_xpath)
        expt_text = "Set a Password"
        try:
            if set_a_password_title.is_displayed():
                print("Set a Password title text is displayed")
                if expt_text.strip() == set_a_password_title.text:
                    print("Set a Password title text matched")
                else:
                    print("Set a Password title text not matched")
            else:
                print("Set a Password title text is not displayed")
                assert False
        except:
            print("test fail")

    # Please create a secure new password for a smoother learning journey. instruction text is displayed
    def instruction_text_displayed(self):
        instruction_text = self.driver.find_element(*Set_a_password_page.SP_instruction_text_xpath)
        expt_text = "Please create a secure new password for a smoother learning journey."
        try:
            if instruction_text.is_displayed():
                print("instruction text  is displayed")
                if expt_text.strip() == instruction_text.text:
                    print("instruction text  matched")
                else:
                    print("instruction text  not matched")
            else:
                print("instruction text is not displayed")
                assert False
        except:
            print("test fail")

    # new_password label text is displayed
    def new_password_label_text_displayed(self):
        new_password_label_text = self.driver.find_element(*Set_a_password_page.SP_new_password_label_text_xpath)
        expt_text = "New Password"
        try:
            if new_password_label_text.is_displayed():
                print("new_password label text  is displayed")
                if expt_text.strip() == new_password_label_text.text:
                    print("new_password label text  matched")
                else:
                    print("new_password label text  not matched")
            else:
                print("new_password label text is not displayed")
                assert False
        except:
            print("test fail")

    # new password textfield is displayed
    def new_password_textfield_displayed(self):
        new_password_textfield = self.driver.find_element(*Set_a_password_page.SP_new_password_textfield_xpath)
        try:
            if new_password_textfield.is_displayed():
                print("new password textfield is displayed")
                assert True
            else:
                print("new password textfield is not displayed")
                assert False
        except Exception as e:
            print(e)

    # enter text in new password textfield
    def enter_text_in_new_password_text_field(self, new_pwd: str):
        new_password_textfield = self.driver.find_element(*Set_a_password_page.SP_new_password_textfield_xpath)
        try:
            new_password_textfield.clear()
            new_password_textfield.send_keys(new_pwd)
            assert True
        except Exception as e:
            print(e)

    # eye button in new password textfield is displayed
    def eye_button_in_new_password_textfield_displayed(self):
        eye_button_in_new_password_textfield = self.driver.find_element(
            *Set_a_password_page.SP_eye_button_in_new_password_textfield_xpath)
        try:
            if eye_button_in_new_password_textfield.is_displayed():
                print("eye button in new password textfield is displayed")
                assert True
            else:
                print("eye button in new password textfield is not displayed")
                assert False
        except Exception as e:
            print(e)

    # verify new password label text is displayed
    def verify_new_password_label_text_displayed(self):
        verify_new_password_label_text = self.driver.find_element(
            *Set_a_password_page.SP_verify_new_password_label_text_xpath)
        expt_text = "Verify New Password"
        try:
            if verify_new_password_label_text.is_displayed():
                print("verify new password label text  is displayed")
                if expt_text.strip() == verify_new_password_label_text.text:
                    print("verify new password label text  matched")
                else:
                    print("verify new password label text  not matched")
            else:
                print("verify new password label text is not displayed")
                assert False
        except:
            print("test fail")

    # enter text in verify new password textfield
    def enter_text_in_verify_new_password_text_field(self, verify_new_pwd: str):
        verify_new_password_textfield = self.driver.find_element(
            *Set_a_password_page.SP_verify_new_password_textfield_xpath)
        try:
            verify_new_password_textfield.clear()
            verify_new_password_textfield.send_keys(verify_new_pwd)
            assert True
        except Exception as e:
            print(e)

    # eye button in new password textfield is displayed
    def eye_button_in_verify_new_password_textfield_displayed(self):
        eye_button_in_verify_new_password_textfield = self.driver.find_element(
            *Set_a_password_page.SP_eye_button_in_verify_new_password_textfield_xpath)
        try:
            if eye_button_in_verify_new_password_textfield.is_displayed():
                print("eye button in verify new password textfield is displayed")
                assert True
            else:
                print("eye button in verify new password textfield is not displayed")
                assert False
        except Exception as e:
            print(e)

    # error text after enter password in new password textfield less than 6 character
    def error_text1_displayed(self):
        error_text1 = self.driver.find_element(*Set_a_password_page.SP_error_text1_xpath)
        return error_text1.text

    # error text below verify new password textfield after entering password in new password text field "Confirm password and new password should be same"
    def error_text2_displayed(self):
        error_text2 = self.driver.find_element(*Set_a_password_page.SP_error_text2_xpath)
        return error_text2.text

    # update password button status
    def update_password_btn_displayed(self):
        update_password_btn = self.driver.find_element(*Set_a_password_page.SP_update_pssword_btn_xpath)
        try:
            if update_password_btn.is_displayed():
                print("update password  is displayed")
            else:
                print("update password is not displayed")
                assert False
        except Exception as e:
            print(e)

    # verify that after entering same password in new password and verify new password textfield, update password button enables
    def is_update_password_button_enabled(self):
        return self.driver.find_element(*Set_a_password_page.SP_update_pssword_btn_xpath).is_enabled()

    # click on update password button
    def update_password_button_click(self):
        update_password_btn = self.driver.find_element(*Set_a_password_page.SP_update_pssword_btn_xpath)
        update_password_btn.click()


