import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from pyscreeze import ImageNotFoundException
import requests
import pyautogui


def createDriverInstance():
    return webdriver.Chrome(ChromeDriverManager().install())


def grabTopQuestions():
    response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
    if response.status_code == 200:
        return response.json() 
    else:
        return None


def creatingListOfQuestions(payload):
    querrys = []
    items = payload['items']
    for item in items:
        querrys.append(item['title'])
    return querrys


def navigateThroughQuerry(querry, browser):
    browser.get('https://google.com')
    time.sleep(3) # Let the user actually see something!
    searchForQuerry(querry, browser)
    time.sleep(3)
    if thereIsAInvitation():
        afterReceivingInvitation(browser)
    navigateToFirstLink(browser)
    time.sleep(5)
    scrollUpAndDown()
    time.sleep(60)
    if thereIsAInvitation():
        afterReceivingInvitation(browser)

def searchForQuerry(querry, browser):
    search = browser.find_element_by_name('q')
    search.send_keys(querry)
    search.send_keys(Keys.RETURN)
    

def navigateToFirstLink(browser):
    try:
        browser.find_element(By.XPATH, '(//h3)[1]/../../a').click()
    except ElementNotInteractableException:
        print("we are here!")
        browser.find_element(By.XPATH, '(//h2)[1]/../../a').click()


def thereIsAInvitation():
    try:
        coordinates = pyautogui.locateOnScreen('images/foobar-invitation.png', confidence=0.5)
    except ImageNotFoundException:
        coordinates = None
    if coordinates is None:
        return False
    return True


def afterReceivingInvitation(browser):
    time.sleep(10000000)
    browser.quit()


def scrollUpAndDown():
    pyautogui.scroll(-10)
    time.sleep(5)
    pyautogui.scroll(10)


def main():
    payload = grabTopQuestions()
    if payload is not None:
        querrys = creatingListOfQuestions(payload)
        browser = createDriverInstance()
        for i in range(len(querrys) - 1):
            navigateThroughQuerry(querrys[i], browser)
        browser.quit()


if __name__ == "__main__":
    main()