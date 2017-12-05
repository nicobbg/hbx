"""hbxreserve module."""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HbxReserve(object):
    """A logger to the boxing page."""

    def __init__(self, user_name, user_password, url):
        """HbxReserve object handles a web session to the Logirider website."""
        self.user_name = user_name
        self.user_password = user_password
        self.url = url
        self.driver = webdriver.Firefox()

    def connect(self):
        """Get the webpage."""
        self.driver.get(self.url)
        sleep(5)

    def login(self):
        """Enter username and password."""
        user_email_elem = self.driver.find_element_by_id('email')
        user_email_elem.clear()
        user_email_elem.send_keys(self.user_name)
        user_password_elem = self.driver.find_element_by_id('password')
        user_password_elem.send_keys(self.user_password)
        user_password_elem.send_keys(Keys.ENTER)

    def go_to_reserve(self):
        """Go the reservation menu."""
        button_reserve = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "button-1032"))
        )
        sleep(5)
        ActionChains(self.driver).move_to_element(button_reserve).click().perform()

    def logout(self):
        """Session logout."""
        self.driver.close()
