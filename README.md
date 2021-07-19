# LinkedIn-scrapper

This program iterates over a list of LinkedIn profile links `links_to_profiles.txt` and retrieves data from them.
Five pieces of information are retrieved from each profile: 
- First name and last name
- Location
- Current job
- Education
- e-mail adress

The new data is appended to the CSV file `scrapper_output.csv`.

Due to the protection of personal data, only my own LinkedIn account has been used as an example.

### Setup

To use this program, you need to specify the path to the chromedriver file and enter emile and password for linkedin profile.
```py
    crawler = LinkedInProfileCrawler(driver_path=r"/path/to/your/chromedriver"
                                     , login="email@example.com"
                                     , password="Y0UR P4$$WORD")
 ```
                                     
 It is recommended to use the libraries versions contained in `requirements.txt`
