from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import config


class AutoPyFirefox:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = f"http://mydy.dypatil.edu/rait/login/index.php?uname={username}&wantsurl="
        self.browser = webdriver.Firefox()
        self.delay = 5

    def login(self):
        self.browser.get(url=self.url)
        passw = self.browser.find_element_by_id("password")
        passw.send_keys(self.password)
        self.browser.find_element_by_id("loginbtn").click()

        try:
            wait = WebDriverWait(self.browser, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "inst986")))
        except TimeoutException:
            print("Page timed out")

    def math_launch(self):
        self.browser.find_element_by_link_text('Launch').click()


auto = AutoPyFirefox(config.DY_USERNAME, config.DY_PASSWORD)
auto.login()
auto.math_launch()

