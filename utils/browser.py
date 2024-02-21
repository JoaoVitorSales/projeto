import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOM_PATH = Path(__file__).parent.parent
CHORMEDRIVER_NAME = 'chromedriver.exe'
CHORMEDRIVER_PATH = ROOM_PATH / 'bin' / CHORMEDRIVER_NAME


def make_browser_chrome(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHORMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser