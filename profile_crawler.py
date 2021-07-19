from selenium import webdriver
from bs4 import BeautifulSoup as bs


class LinkedInProfileCrawler():
    def __init__(self, driver_path, login, password):
        self.driver_path = driver_path
        self.login = login
        self.password = password
        # intiate driver and log in
        self.initiate_driver()
        self.log_in()

    def initiate_driver(self):
        # create options
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("detach", True)
        options.add_argument("--incognito")

        self.browser = webdriver.Chrome(options=options, executable_path=self.driver_path)

    def log_in(self):
        # open login page
        self.browser.get(
            r"https://www.linkedin.com/login/pl?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

        # update login, password and submit
        elementID = self.browser.find_element_by_id("username")
        elementID.send_keys(self.login)
        elementID = self.browser.find_element_by_id("password")
        elementID.send_keys(self.password)
        elementID.submit()

    def open_contact_details(self):
        self.browser.get(self.url + "detail/contact-info/")
        contact_page = self.browser.page_source
        return bs(contact_page)

    def collect_data(self, profile_url):
        self.url = profile_url
        self.browser.get(self.url)
        self.html = self.browser.page_source
