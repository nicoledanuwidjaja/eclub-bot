import os
from os.path import join, dirname
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# secret secret
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

# store follower username and name
followers = {'rachna.lewis' : 'Rachna Lewis', 'krisp_thins' : 'Kristin', 'stegosaurusuuuuu' : 'Vera', 'liindazeng' : ''}

class FeedPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/neu_eclub')

    # stores list of eclub followers in dictionary
    def collect_followers(self):
        browser.find_element_by_xpath('//a[contains(@href, "%s")]' % "followers").click()
        element = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        sleep(2)
        follower_count = int(element.text.split()[0].replace(',', ''))

        for follower in range(1, follower_count):
            profile_container = browser.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/ul/div/li[%s]/div/div/div' % follower)
            profile_name = browser.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/ul/div/li[%s]/div/div/div[2]/div[1]' % follower).text
            browser.execute_script("arguments[0].scrollIntoView();", profile_container)
            username = browser.current_url
            sleep(1)
            followers[username] = profile_name
            print(followers)

    # spam all followers with a templated message
    def send_messages(self):
        browser.get('https://www.instagram.com/direct/new/')
        sleep(2)

        # get rid of notifications popup
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

        for username, name in followers.items():
            browser.get('https://www.instagram.com/direct/new/')
            sleep(2)
            first_name = name.split()[0] if name else 'there'
            template = "Hey {name}! I hope you're having a wonderful week.\n" \
                      "I just wanted to let you know that Demo Day - Northeastern's largest celebration of student " \
                      "entrepreneurship and innovation - is this Wednesday, November 18th, from 6-8:15pm EST. We would LOVE to see you there!\n" \
                      "You'll meet the Husky Startup Challenge's top 12 startups compete for cash prizes in front of " \
                      "hundreds of people.\n" \
                      " You can sign up here:\n" \
                      " https://tinyurl.com/demodayfall2020\n" \
                      " Feel free to let us know if you have any questions!\n".format(name=first_name)
            print(first_name)
            recipient = self.browser.find_element_by_css_selector("input[name='queryBox']")
            recipient.send_keys(username)
            browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]').click()
            sleep(3)
            # input message
            message_input = self.browser.find_element_by_css_selector("textarea")
            message_input.send_keys(template)
            sleep(5)


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        return LoginPage(self.browser)


def init(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(USERNAME, PASSWORD)
    feed_page = FeedPage(browser)
    # feed_page.collect_followers()
    feed_page.send_messages()

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0


# start bot
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)
init(browser)
# browser.close()
