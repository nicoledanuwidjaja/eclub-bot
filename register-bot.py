import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from os.path import join, dirname
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# secret secret
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# store follower username and name
followers = {}

## CampusLabs
# Manage Roster -> Prospective
# Click on each name --> Email
# Add date added
# Send message to all: Subject and Message Text (Custom message for upcoming events)
# Approve All (edited)

## Mailchimp
# Login
# Audience > All contacts
# Select E-Club General Newsletter
# Add contacts > Import Contacts > Copy and paste
# Update any existing contacts

class ContactsPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('')

    # Navigate to Add Contacts
    def import_contacts(self):
        # TODO: click clack

    # Update Existing Contacts
    def update_contacts(self):
        browser.get('')
        # grab contacts from Google Sheets
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_secret.json', scope)
        client = gspread.authorize(creds)
        # TODO: Add fields
        sleep(2)

        # get rid of notifications popup
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


class HomePage:
    def __init__(self, browser):
        self.browser = browser


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://login.mailchimp.com/')

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        # click on cookies popup
        browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div[2]/div/button[2]').click()
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        # verification
        sleep(5)

    def go_to_home_page(self):
        return HomePage(self.browser)


def init(browser):
    login_page = LoginPage(browser)
    login_page.login(USERNAME, PASSWORD)
    home_page = login_page.go_to_home_page()
    contacts_page = ContactsPage(browser)
    contacts_page.import_contacts()
    contacts_page.update_contacts()

    # errors = browser.find_elements_by_css_selector('#error_message')


# start bot
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)
init(browser)
browser.close()
