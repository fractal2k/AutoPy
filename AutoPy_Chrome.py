#dirtiest implementation of this thing possible, because who needs classes and methods anyways

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import config

#Opening browser window for the first time, logging in
user = config.USERNAME
chromedriver = "" #put your chromedriver.exe location here
url = f"http://mydy.dypatil.edu/rait/login/index.php?uname={user}&wantsurl="
driver = webdriver.Chrome(chromedriver)
driver.get(url)
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys(config.PASSWORD)
elem.send_keys(Keys.RETURN)

#initializing the subject buttons' list for the first time
subjects = driver.find_elements_by_link_text("Launch")

#iterating through subjects
for i in range(len(subjects)):
    subjects[i].click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # in subject tab
    sections = driver.find_elements_by_xpath("//*[contains(@id,'section-')]")
    no_of_sections = int(len(driver.find_elements_by_xpath("//*[contains(@id,'section-')]"))/2)
    driver.find_element_by_xpath("//*[contains(@aria-label,'Section')]").click()

    #iterating through modules in each section
    for i in range(no_of_sections - 1):
        element_parent = driver.find_element_by_id('gtopics')
        element = element_parent.find_element_by_id(f'section-{i + 1}')
        temp = element.find_elements_by_xpath(".//li[contains(@id,'module-')]")
        for item in temp:
            link = item.find_element_by_xpath('.//a[contains(@href, "http")]')
            ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        driver.find_element_by_xpath('//*[contains(@src,"http://mydy.dypatil.edu/rait/theme/image.php/essential/format_grid/1524215314/fa-arrow-circle-right-w")]').click()
    driver.quit()

    #who needs methods when you can copy paste stuff
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    elem = driver.find_element_by_id("password")
    elem.clear()
    elem.send_keys(config.PASSWORD)
    elem.send_keys(Keys.RETURN)
    subjects = driver.find_elements_by_link_text("Launch")
