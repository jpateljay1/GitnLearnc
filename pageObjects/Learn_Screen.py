
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Learn_page(BaseClass):
    LS_dropdown_btn_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")


    def dropdown_btn_clicked(self):
        log = self.getLogger()
        dropdown_btn = self.driver.find_element(*Learn_page.LS_dropdown_btn_xpath)
        dropdown_btn.click()



    def __init__(self, driver):
        self.driver = driver
