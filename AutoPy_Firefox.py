from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import config


class AutoPyFirefox:

    def __init__(self, username, password, view_id):
        self.username = username
        self.password = password
        self.url = f"http://mydy.dypatil.edu/rait/login/index.php?uname={username}&wantsurl=http://mydy.dypatil.edu/rait/course/view.php?id={view_id}"
        self.driver = webdriver.Firefox()
        self.delay = 5

    def login(self):
        self.driver.get(url=self.url)
        passw = self.driver.find_element_by_id("password")
        passw.send_keys(self.password)
        self.driver.find_element_by_id("loginbtn").click()

        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "gridiconcontainer")))
        except TimeoutException:
            print("Page timed out")

    def click_on_shit(self):
        self.login()
        self.driver.find_element_by_xpath('//*[contains(@aria-label, "Section 1")]').click()


auto = AutoPyFirefox(config.USERNAME, config.PASSWORD, config.VIEW_ID_MATH)
auto.click_on_shit()

