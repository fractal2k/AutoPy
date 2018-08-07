from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        passw.clear()
        passw.send_keys(self.password)
        self.driver.find_element_by_id("loginbtn").click()

        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "gridiconcontainer")))
        except TimeoutException:
            print("Page timed out")

    def click_on_shit(self):
        self.login()
        num_sections = int(len(self.driver.find_elements_by_xpath('//li[contains(@aria-label, "Section")]')) / 2)
        self.driver.find_element_by_xpath('//li[contains(@aria-label, "Section")]').click()

        for i in range(num_sections - 1):
            element_parent = self.driver.find_element_by_id('gtopics')
            element = element_parent.find_element_by_id(f'section-{i + 1}')
            temp = element.find_elements_by_xpath('.//li[contains(@id, "module-")]')

            for j in temp:
                child = j.find_element_by_xpath('.//a[contains(@href, "http")]')
                ActionChains(self.driver).key_down(Keys.LEFT_CONTROL).click(child).key_up(Keys.LEFT_CONTROL).perform()

            self.driver.find_element_by_xpath('//*[@id="gridshadebox_right"]').click()

    def exit(self):
        self.driver.quit()


auto = AutoPyFirefox(config.USERNAME, config.PASSWORD, config.VIEW_ID_MATH)
auto.click_on_shit()
auto.exit()



