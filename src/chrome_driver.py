from config import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import subprocess

def start():


    # Command to launch Chrome with a specific profile
    command = [
        # config['driver-path'],
        "C:\Program Files\Google\Chrome\Application\chrome.exe",
        # "chrome.exe",
        f"--user-data-dir={config['user-data-dir']}",
        f"--profile-directory={config['profile-directory']}",
        "--remote-debugging-port=9222"
    ]

    print(command)


    result = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("Output:", result.stdout)
    print("Errors:", result.stderr)

    """
        Attaches Selenium to an already running Chrome instance.
        """
    options = Options()
    options.debugger_address = "127.0.0.1:9222"  # Address of the remote debugging port

    # Attach to the existing session
    driver = WebDriver(options=options)

    # Launch Chrome.
    return driver

