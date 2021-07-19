from bs4 import BeautifulSoup as bs
from linkedin_profile_crawler import LinkedInProfileCrawler
import csv
import time


class Person():
    def __init__(self, html):
        self.html = html
        self.soup = bs(self.html, features="html.parser")

    def extract_pers_info(self):
        section = self.soup.find_all('section', {'class': 'pv-top-card'})[0]

        name = section.find_all('h1')[0].text
        address = section.find_all('span')[0].text.strip()
        job = section.find_all('h2')[0].text.strip()
        edu = section.find_all('h2')[1].text.strip()
        email_soup = crawler.click_contact_details()
        email = email_soup.find_all(
            'a', {"class": "pv-contact-info__contact-link link-without-visited-state t-14"})[1].text.split()[0]
        return name, address, job, edu, email


if __name__ == "__main__":

    # intiate crawler instance
    crawler = LinkedInProfileCrawler(driver_path=r"/path/to/your/chromedriver"
                                     , login="email@example.com"
                                     , password="Y0UR P4$$WORD")

    # Loop through links in links_to_profiles.txt
    linksList = open("links_to_profiles.txt", "r")

    for line in linksList:
        # Open csv file
        csv_file = open('scrapper_output.csv', 'a')
        csv_writer = csv.writer(csv_file)

        # Colect Data
        profile_url = fr"{line}"
        crawler.collect_data(profile_url)
        d = Person(html=crawler.html)

        # Save Data
        csv_writer.writerow(d.extract_pers_info())
        csv_file.close()
        time.sleep(1)

    linksList.close()

