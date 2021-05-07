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
        levels = ['Easy', 'Medium', 'Hard']
        levels_dict = {'total_questions': 0}

        # Types of Questions
        for level in levels:
            level_div = browser.find_element_by_css_selector(f"div[data-difficulty='{level}']")
            levels_dict[level.lower()] = int(level_div.find_element_by_tag_name('span').get_attribute('innerHTML'))
            levels_dict['total_questions'] += levels_dict[level.lower()]

        # Points
        points_element = browser.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/li[1]/span')
        points = int(points_element.get_attribute('innerHTML'))

        return {**levels_dict, 'points': points}
    except:
        return {
            'error': ['Check the username you have entered!']
        }