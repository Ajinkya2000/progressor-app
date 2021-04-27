from selenium import webdriver
import sys

options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome('./chromedriver', options=options)

user = sys.argv[1]


def getLeetcodeData(username=user):
    browser.get(f'https://leetcode.com/{username}/')

    # Total Solved Questions


print(getLeetcodeData())
