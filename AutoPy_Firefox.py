from selenium import webdriver
import config

class AutoPyFirefox:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = f"http://mydy.dypatil.edu/rait/login/index.php?uname={username}&wantsurl="
        self.browser = webdriver.Firefox()

    def login(self):
        self.browser.get(url=self.url)
        passw = self.browser.find_element_by_id("password")

        passw.send_keys(self.password)
        self.browser.find_element_by_id("loginbtn").click()


auto = AutoPyFirefox(config.DY_USERNAME, config.DY_PASSWORD)
auto.login()
