from pathlib import Path
from selenium import webdriver
import os


def getLeetcodeData(username):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SCRIPTS_DIR = BASE_DIR / 'scripts'

    URL = f'https://leetcode.com/{username}/'

    """DEVELOPMENT"""
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # browser = webdriver.Chrome(f'{SCRIPTS_DIR}/chromedriver', options=options)

    """PRODUCTION"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    browser.get(URL)
    browser.implicitly_wait(10)

    try:
        # Total Questions Solved
        total_problems_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[2]')
        total_problems = total_problems_element.get_attribute('innerHTML')

        # Types of Questions
        easy_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/span[1]')
        easy = easy_element.get_attribute('innerHTML')

        medium_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/span[1]')
        medium = medium_element.get_attribute('innerHTML')

        hard_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/span[1]')
        hard = hard_element.get_attribute('innerHTML')

        # Points
        points_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/li[1]/span')
        points = points_element.get_attribute('innerHTML')

        return {
            'leetcode_handle': username,
            'points': points,
            'total_questions': total_problems,
            'easy': easy,
            'medium': medium,
            'hard': hard,
        }
    except:
        return {
            'error': ['Check the username you have entered!']
        }

