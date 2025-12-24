import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://stage-nlearn.nspira.in/")
    driver.maximize_window()
    return driver