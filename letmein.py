import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from pyscreeze import ImageNotFoundException
import requests
import pyautogui
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os


def createTwilioClient():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    return Client(account_sid, auth_token)


def sendTextMessage(client):
    try:
        message = client.messages \
                    .create(
                         body="Did you realize you were a champion in their eyes? The foo-bar script worked.",
                         from_=os.environ['SENDER_PHONE_NUMBER'],
                         to=os.environ['USER_PHONE_NUMBER']
                     )
    except TwilioRestException:
        pass


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
    if userIsOnAGoogleWebpage(browser):
        scrollUpAndDown()
        time.sleep(60)
    else:
        time.sleep(4)
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
        assert "No results found." not in browser.page_source
        browser.find_element_by_xpath('.//*[@id="rso"]/div[1]/div/div/div/div/h3/a').click()
    except NoSuchElementException:
        assert "No results found." not in browser.page_source
        browser.find_element_by_xpath('.//*[@id="rso"]/div[1]/div/div/div/div/h3/a').click()


def thereIsAInvitation():
    try:
        coordinates = pyautogui.locateOnScreen('images/foobar-invitation.png', confidence=0.5)
    except ImageNotFoundException:
        coordinates = None
    if coordinates is None:
        return False
    return True


def afterReceivingInvitation(browser):
    client = createTwilioClient()
    if client is not None:
        sendTextMessage(client)
    time.sleep(10000000)
    browser.quit()


def scrollUpAndDown():
    pyautogui.scroll(-10)
    time.sleep(5)
    pyautogui.scroll(10)


def haveUserSignIn(browser):
    browser.get('https://google.com')
    search = browser.find_element_by_name('q')
    search.send_keys("Sign into your account and just wait")
    time.sleep(30)


# There is a feature where if you are on an official google API page, the challenge can show up
# if you wait for longer than 5 minutes or something
def userIsOnAGoogleWebpage(browser):
    url = browser.current_url
    if "google.com" in url:
        return True
    return False


def main():
    '''browser = createDriverInstance()
    haveUserSignIn(browser)
    while True: # Runs until it finds the invitation
        payload = grabTopQuestions()
        if payload is not None:
            querrys = creatingListOfQuestions(payload)
            for i in range(len(querrys) - 1):
                navigateThroughQuerry(querrys[i], browser)
        else: 
            print("Error: Could not access or pull questions from stackexchange API")
            browser.quit()'''
    client = createTwilioClient()
    sendTextMessage(client)



if __name__ == "__main__":
    main()