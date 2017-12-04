"""boxing_logger."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


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

    def logout(self):
        """Session logout."""
        self.driver.close()


def main():
    """Just a test."""
    session = HbxReserve('test@gmail.com', 'xxxxxxxxx',
                         'http://www.logirider.fr/formstationrennes/')
    session.connect()
    session.login()


if __name__ == '__main__':
    main()
