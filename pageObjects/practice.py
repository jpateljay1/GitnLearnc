import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome driver service selenium
driver = webdriver.Chrome()
driver.get("https://stage-nlearn.nspira.in/")
driver.maximize_window()
print(driver.title)


def test_admission_label_text():
    LS_Admission_Number_label_txt_xpath = "//h6[.='Admission Number']"
    adm_label_text = driver.find_element(By.XPATH, LS_Admission_Number_label_txt_xpath)
    adm_label_text.is_displayed()
    print(adm_label_text.text)
    exp_txt = "Admission Number"
    if exp_txt == adm_label_text:
        print("correct")
        assert True


def test_login():
    # admission number textfield in login page
    LS_AdmissionNumber_txt_field_xpath = ("/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div["
                                          "1]/form[1]/input[1]")
    LS_Password_txt_field_xpath = ("/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form["
                                   "1]/div[1]/input[1]")
    LS_login_btn_xpath = "//button[normalize-space()='Login']"
    # error msg2 "Admission number is not registered. Please contact your principal"
    LS_admno_error_text2_xpath = "(//div[@class='input-error'])[1]"
    expected_text = "Admission number is not registered. Please contact your principal"

    driver.find_element(By.XPATH, LS_AdmissionNumber_txt_field_xpath).send_keys("chandan")
    driver.find_element(By.XPATH, LS_Password_txt_field_xpath).send_keys("test@123")
    driver.find_element(By.XPATH, LS_login_btn_xpath).click()
    time.sleep(5)
    errortext = driver.find_element(By.XPATH, LS_admno_error_text2_xpath).text
    if expected_text == errortext:
        print(" text is displayed")
        assert True
    else:
        print("text not displayed")


def test_successful_login():
    # admission number textfield in login page
    LS_AdmissionNumber_txt_field_xpath = ("/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div["
                                          "1]/form[1]/input[1]")
    LS_Password_txt_field_xpath = ("/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form["
                                   "1]/div[1]/input[1]")
    LS_login_btn_xpath = "//button[normalize-space()='Login']"

    driver.find_element(By.XPATH, LS_AdmissionNumber_txt_field_xpath).clear()
    driver.find_element(By.XPATH, LS_AdmissionNumber_txt_field_xpath).send_keys("TP2023045")
    driver.find_element(By.XPATH, LS_Password_txt_field_xpath).clear()

    driver.find_element(By.XPATH, LS_Password_txt_field_xpath).send_keys("test@123")
    driver.find_element(By.XPATH, LS_login_btn_xpath).click()
    time.sleep(5)
    expected_url = "https://stage-nlearn.nspira.in/home"
    current_url = driver.current_url
    if expected_url == current_url:
        print("user on home page")
        assert True




google_play_btn = Login_page(self.driver)
original_window = self.driver.current_window_handle
google_play_btn.click_google_play()
self.driver.implicitly_wait(10)
all_window = self.driver.window_handles
self.assertEqual(len(all_window), 2, "A new tab was not opened")
mew_window = [window for window in all_window if window != original_window][0]
self.driver.close()
self.driver.switch_to.window(original_window)

