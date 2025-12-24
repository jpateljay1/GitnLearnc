import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class home_page(BaseClass):
    HS_nLearn_logo_xpath = (By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[1]/div[2]/img[1]")
    HS_welcome_text_xpath = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    HS_profile_btn_xpath = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/button[1]/div[1]/div[1]")
    # dropdown button
    HS_dropdown_btn_xpath = (By.XPATH, "//button[@id='dropdown-basic']")
    # Notification button
    HS_notification_btn_xpath = (
        By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/img[1]")

    # left nav bar of home page
    HS_home_nav_btn_xpath = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/div/a")
    HS_schedule_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/img[1]")
    HS_learn_Left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/a[1]/img[1]")
    HS_library_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/a[1]/img[1]")
    HS_practice_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/div[1]/a[1]/img[1]")
    HS_assignments_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/a[1]/img[1]")
    HS_doubt_solving_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[7]/div[1]/a[1]/img[1]")
    HS_tests_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[8]/div[1]/a[1]/img[1]")
    HS_activities_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[9]/div[1]/a[1]/img[1]")
    HS_term_exams_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[10]/div[1]/a[1]/img[1]")
    HS_analytics_left_nav_btn_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[11]/div[1]/a[1]/img[1]")

    # carousel image locator
    HS_first_cursl_img_xpath = (By.XPATH,
                                "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/img[1]")
    HS_second_cursl_img_xpath = (By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[11]/div[1]/div[1]/img[1]")

    # carousel image pointer buttons
    HS_first_cursl_pointer_btn_xpath = (By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]")
    HS_second_cursl_pointer_btn_xpath = (By.XPATH,
                                         "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]")

    # Continue From Where You Left section
    HS_continue_from_where_you_left_text_xpath = (By.XPATH, "//h1[contains(text(),'Continue From Where You Left.')]")
    HS_learn_videos_nav_bar_xpath = (By.XPATH, "//a[contains(text(),'Learn Videos')]")
    HS_practice_nav_bar_xpath = (By.XPATH, "//a[contains(text(),'Practice')]")

    # Pick A Subject To Learn section
    # Pick A Subject To Learn title text
    HS_Pick_A_Subject_To_Learn_title_xpath = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[3]/div[1]/h1[1]")
    HS_subject_card1_xpath = (By.XPATH, "//span[normalize-space()='BIOLOGY']")

    def __init__(self, driver):
        self.driver = driver

    # nlearn logo is displayed or not
    def nLearn_logo_displayed(self):
        log = self.getLogger()
        nLearn_logo = self.driver.find_element(*home_page.HS_nLearn_logo_xpath)
        try:
            if nLearn_logo.is_displayed():
                print("nLearn logo is displayed")
                log.info("***nLearn Logo is Displayed***")
                assert True
            else:
                print("nLearn  logo is not displayed")
                log.info("***nLearn Logo is not Displayed***")
                assert False
        except Exception as e:
            log.error(f'Test Fail, while checking nLearn Logo is  displayed: {e}')

    # Welcome text is displayed or not
    def welcome_text_displayed(self):
        log = self.getLogger()
        welcome_text = self.driver.find_element(*home_page.HS_welcome_text_xpath)
        try:
            if welcome_text.is_displayed():
                print("welcome text is displayed")
                log.info("***Welcome Text is Displayed***")
                assert True
            else:
                print("welcome text is not displayed")
                log.info("***Welcome text is not Displayed***")
                assert False
        except Exception as e:
            log.error(f'Test Fail, while checking welcome text is  displayed: {e}')

    # dropdown button is displayed
    def dropdown_btn_displayed(self):
        log = self.getLogger()
        dropdown_btn = self.driver.find_element(*home_page.HS_dropdown_btn_xpath)
        try:
            if dropdown_btn.is_displayed():
                print("Dropdown button is displayed")
                log.info("***Dropdown button is Displayed***")
                assert True
            else:
                print("Dropdown button  is not displayed")
                log.info("***Dropdown button is not Displayed***")
                assert False
        except Exception as e:
            log.error(f'Test Fail, while checking Dropdown button is  displayed: {e}')

    # Notification button is displayed
    def notification_btn_displayed(self):
        notification_btn = self.driver.find_element(*home_page.HS_notification_btn_xpath)
        try:
            if notification_btn.is_displayed():
                print("Notification button is displayed")
                assert True
            else:
                print("Notification button  is not displayed")
                assert False
        except Exception as e:
            print(e)

    # profile icon button
    def profile_icon_displayed(self):
        profile_icon = self.driver.find_element(*home_page.HS_profile_btn_xpath)
        try:
            if profile_icon.is_displayed():
                print("Profile Icon is displayed")
                assert True
            else:
                print("Profile Icon  is not displayed")
                assert False
        except Exception as e:
            print(e)

    # left nav button
    # schedule left nav button is displayed
    def schedule_left_nav_btn_displayed(self):
        schedule_left_nav_btn = self.driver.find_element(*home_page.HS_schedule_left_nav_btn_xpath)
        try:
            if schedule_left_nav_btn.is_displayed():
                print(" schedule left nav button is displayed")
                assert True
            else:
                print(" schedule left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Learn left nav button is displayed
    def learn_Left_nav_btn_displayed(self):
        learn_Left_nav_btn = self.driver.find_element(*home_page.HS_learn_Left_nav_btn_xpath)
        try:
            if learn_Left_nav_btn.is_displayed():
                print(" Learn left nav button is displayed")
                assert True
            else:
                print(" Learn left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Library left nav button is displayed
    def library_left_nav_btn_displayed(self):
        library_left_nav_btn = self.driver.find_element(*home_page.HS_library_left_nav_btn_xpath)
        try:
            if library_left_nav_btn.is_displayed():
                print(" Library left nav button is displayed")
                assert True
            else:
                print(" Library left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Practice left nav button is displayed
    def practice_left_nav_btn_displayed(self):
        practice_left_nav_btn = self.driver.find_element(*home_page.HS_practice_left_nav_btn_xpath)
        try:
            if practice_left_nav_btn.is_displayed():
                print(" Practice left nav button is displayed")
                assert True
            else:
                print(" practice left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Assignments left nav button is displayed
    def assignments_left_nav_btn_displayed(self):
        assignments_left_nav_btn = self.driver.find_element(*home_page.HS_assignments_left_nav_btn_xpath)
        try:
            if assignments_left_nav_btn.is_displayed():
                print(" Assignments left nav button is displayed")
                assert True
            else:
                print(" Assignments left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Doubt Solving left nav button is displayed
    def HS_doubt_solving_left_nav_btn_displayed(self):
        doubt_solving_left_nav_btn = self.driver.find_element(*home_page.HS_doubt_solving_left_nav_btn_xpath)
        try:
            if doubt_solving_left_nav_btn.is_displayed():
                print(" Doubt Solving left nav button is displayed")
                assert True
            else:
                print(" Doubt Solving left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Tests left nav button is displayed
    def tests_left_nav_btn_displayed(self):
        tests_left_nav_btn = self.driver.find_element(*home_page.HS_tests_left_nav_btn_xpath)
        try:
            if tests_left_nav_btn.is_displayed():
                print("Tests left nav button is displayed")
                assert True
            else:
                print("Tests left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Activities left nav button is displayed
    def activities_left_nav_btn_displayed(self):
        activities_left_nav_btn = self.driver.find_element(*home_page.HS_activities_left_nav_btn_xpath)
        try:
            if activities_left_nav_btn.is_displayed():
                print("Activities left nav button is displayed")
                assert True
            else:
                print("Activities left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Term Exams left nav button is displayed
    def term_exams_left_nav_btn_displayed(self):
        term_exams_left_nav_btn = self.driver.find_element(*home_page.HS_term_exams_left_nav_btn_xpath)
        try:
            if term_exams_left_nav_btn.is_displayed():
                print("Term Exams left nav button is displayed")
                assert True
            else:
                print("Term Exams left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # Analytics left nav button is displayed
    def analytics_left_nav_btn_displayed(self):
        analytics_left_nav_btn = self.driver.find_element(*home_page.HS_analytics_left_nav_btn_xpath)
        try:
            if analytics_left_nav_btn.is_displayed():
                print("Analytics  left nav button is displayed")
                assert True
            else:
                print("Analytics left nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # click on schedule left nav bar
    def click_schedule_left_nav_bar(self):
        schedule_btn = self.driver.find_element(*home_page.HS_schedule_left_nav_btn_xpath)
        schedule_btn.click()

    # click on Learn left nav bar
    def click_Learn_left_nav_bar(self):
        schedule_btn = self.driver.find_element(*home_page.HS_learn_Left_nav_btn_xpath)
        schedule_btn.click()

    # click first carousel  nav button
    def first_cursl_pointer_btn_click(self):
        first_cursl_pointer_btn = self.driver.find_element(*home_page.HS_first_cursl_pointer_btn_xpath)
        first_cursl_pointer_btn.click()

    # click second carousel  nav button
    def second_cursl_pointer_btn_click(self):
        second_cursl_pointer_btn = self.driver.find_element(*home_page.HS_second_cursl_pointer_btn_xpath)
        second_cursl_pointer_btn.click()

    # carousel image locator
    def first_cursl_img_displayed(self):
        try:
            first_cursl_img = self.driver.find_element(*home_page.HS_first_cursl_img_xpath)
            return first_cursl_img.is_displayed()
        except Exception as e:
            print(e)

    def second_cursl_img_displayed(self):
        try:
            second_cursl_img = self.driver.find_element(*home_page.HS_second_cursl_img_xpath)
            return second_cursl_img.is_displayed()
        except Exception as e:
            print(e)

    # Continue From Where You Left section
    # Continue From Where You Left text is displayed
    def continue_from_where_you_left_text_displayed(self):
        continue_from_where_you_left_text = self.driver.find_element(
            *home_page.HS_continue_from_where_you_left_text_xpath)
        exptected_text = "Continue From Where You Left."
        try:
            if continue_from_where_you_left_text.is_displayed():
                print("Continue From Where You Left text is displayed")
                if exptected_text.strip() == continue_from_where_you_left_text.text:
                    print("Continue From Where You Left text matched")
                else:
                    print("Continue From Where You Left text not matched")
            else:
                print("Continue From Where You Left text is not displayed")
                assert False
        except:
            print("test fail")

    # Learn Videos nav button is displayed
    def learn_videos_nav_btn_displayed(self):
        learn_videos_nav_btn = self.driver.find_element(*home_page.HS_learn_Left_nav_btn_xpath)
        try:
            if learn_videos_nav_btn.is_displayed():
                print("Learn Videos nav button is displayed")
                assert True
            else:
                print("Learn Videos nav button is not displayed")
                assert False
        except Exception as e:
            print(e)

    # click on Learn Videos nav button in Continue From Where You Left section
    def click_learn_videos_nav_btn(self):
        learn_video_nav_btn = self.driver.find_element(*home_page.HS_learn_Left_nav_btn_xpath)
        if learn_video_nav_btn.click():
            print("Learn Videos nav button is clickable")
            assert True
        else:
            print("Learn Videos nav button is not clickable")
            assert False

    # click on practice nav button in Continue From Where You Left section
    def click_practice_nav_btn(self):
        practice_nav_btn = self.driver.find_element(*home_page.HS_practice_nav_bar_xpath)
        if practice_nav_btn.click():
            print("Practice  nav button is clickable")
        else:
            print("Practice nav button is not clickable")
            assert False

    # click on subject card 1 in Pick A Subject To Learn section
    def click_subject_card_1(self):
        subject_card_1 = self.driver.find_element(*home_page.HS_subject_card1_xpath)
        try:
            subject_card_1.click()
            print("clickable")
        except Exception as e:
            print(e)

    def pick_A_Subject_To_Learn_title(self):
        pick_a_subject_to_learn_title = self.driver.find_element(*home_page.HS_Pick_A_Subject_To_Learn_title_xpath)
        return pick_a_subject_to_learn_title.text
