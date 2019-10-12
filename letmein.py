import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


SEARCH_TERMS = ["mutex lock", "how to run javascript on chrome extension"]
index = 0


browser = webdriver.Chrome(ChromeDriverManager().install())
while True and index < len(SEARCH_TERMS):
    browser.get('https://google.com')
    time.sleep(3) # Let the user actually see something!
    search = browser.find_element_by_name('q')
    search.send_keys(SEARCH_TERMS[index])
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    browser.find_element(By.XPATH, '(//h3)[1]/../../a').click()
    time.sleep(4)
    browser.back()
    time.sleep(2)
    browser.find_element(By.XPATH, '(//h3)[2]/../../a').click()
    time.sleep(4)
    browser.back()
    time.sleep(2)
    index += 1
browser.quit()