from pathlib import Path
from selenium import webdriver
import os

def getGFGDetails(username):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SCRIPTS_DIR = BASE_DIR / 'scripts'

    URL = f'https://auth.geeksforgeeks.org/user/{username}/practice/'

    # options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    # options.headless = True
    # browser = webdriver.Chrome(f'{SCRIPTS_DIR}/chromedriver', options=options)
    browser.get(URL)

    try:
        if browser.current_url != URL:
            raise Exception(
                "Check the username you have entered")

        # Total Solved Questions
        total_questions_element = browser.find_element_by_xpath(
            '//*[@id="detail1"]/div[1]/div[6]/div[2]/a')
        total_questions_string = str(
            total_questions_element.get_attribute('innerHTML'))
        total_questions = ''
        for i in range(22, len(total_questions_string)):
            total_questions += total_questions_string[i]
        total_questions = int(total_questions)

        # Overall Coding Score
        coding_score_element = browser.find_element_by_xpath(
            '//*[@id="detail1"]/div[1]/div[6]/div[1]')
        coding_score_string = str(
            coding_score_element.get_attribute('innerHTML'))
        coding_score = ''
        for i in range(34, len(coding_score_string)):
            coding_score += coding_score_string[i]
        coding_score = int(coding_score)

        # Types of Questions Solved
        pie_chart_script_tag = browser.find_element_by_xpath(
            '//*[@id="detail1"]/div[2]/script')
        pie_chart_script_tag_string = str(
            pie_chart_script_tag.get_attribute('innerHTML'))
        pie_chart_array_start = pie_chart_script_tag_string.find('[', 2615)
        pie_chart_array_end = pie_chart_script_tag_string.find(']', 2625)
        pie_chart_array = ''

        for i in range(pie_chart_array_start + 1, pie_chart_array_end):
            pie_chart_array += pie_chart_script_tag_string[i]

        pie_chart_array = pie_chart_array.split(',')
        pie_chart_array_name = ['school', 'basic', 'easy', 'medium', 'hard']
        pie_chart_questions_data = {}
        for i in range(0, len(pie_chart_array)):
            pie_chart_questions_data[pie_chart_array_name[i]] = int(
                pie_chart_array[i])

        browser.quit()
        return {
            'total_questions': total_questions,
            'coding_score': coding_score,
            **pie_chart_questions_data
        }
    except Exception as inst:
        return {
            'error': inst.args[0]
        }
