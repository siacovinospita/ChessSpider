from webdriver_manager.chrome import ChromeDriverManager

from config import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import SessionNotCreatedException

def start ():
    """
    Configures and starts a Selenium Chrome WebDriver.
    """
    # Set up Chrome options.
    options = Options()
    options.add_argument(f"--user-data-dir={config['user-data-dir']}")
    options.add_argument(f"profile-directory={config['profile-directory']}")

    # Set up Chrome driver service.
    service = Service(config['driver-path'])
    ChromeDriverManagerExecutableDirectory = ChromeDriverManager(driver_version="131.0.6778.140").install()
    # ChromeDriverManagerExecutableDirectory = ChromeDriverManager().install()

    service = Service(ChromeDriverManagerExecutableDirectory)

    # Launch Chrome.
    driver = initialiseChromeDriver(options, service)
    return driver


def initialiseChromeDriver(options, service):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except SessionNotCreatedException as exp:
        print("Check that Chrome is currently closed")
        user_input = input("Enter \"c\" to continue: ").strip().lower()
        if user_input == 'c':
            print("Continuing...")
            return initialiseChromeDriver(options, service)
        if user_input == "restart":
            global page_nr
            page_nr = 1
        else:
            print("Exiting.")
            exit()




