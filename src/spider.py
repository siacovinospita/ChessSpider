import sys

from config import config
import chrome_driver
from random import randrange
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
import time


def randsleep ():
    human_check()
    """
    Delay execution with 2 or 3 seconds.
    """
    sleep(randrange(2, 4))
    human_check()

def human_check():

    global human_check_bol

    text_to_find = "Verify you are human by completing the action below."
    try:
        if text_to_find in driver.page_source:
            print(f'Text "{text_to_find}" is present on the screen.')
            human_check_bol = True

    except NoSuchWindowException:
        pass

    if human_check_bol:
        checkInput()



        human_check_bol = False
        # start_waiting_input_thread()



def checkInput ():
    user_input = input("Enter \"c\" to continue: ").strip().lower()
    if user_input == 'c':
        print("Continuing...")
    if user_input == "restart":
        global page_nr
        page_nr = 1
    else:
        print("Exiting.")
        exit()

import threading

human_check_bol = False
# event = threading.Event()


def wait_for_input():
    user_input = input("Input \"exit\" to stop the program...\n")
    global human_check_bol
    if user_input == "exit":
        print("exit")
        sys.exit()
    if user_input == "c":
        print("You pressed c")
        human_check_bol = False
        wait_for_input()
    if user_input == "h":

        human_check_bol = True
        # wait_for_input()


def start_waiting_input_thread():
    # Start a thread to wait for user input
    input_thread = threading.Thread(target=wait_for_input)
    input_thread.start()

# start_waiting_input_thread()

start_time = time.time()
page_nr = config['start-page']

last_page_nr = config['end-page']


driver = chrome_driver.start()
# checkInput()

driver.maximize_window()
# checkInput()


while page_nr <= last_page_nr :
    print(f"Crawling page number {page_nr}...")


    "https://www.chess.com/games/archive/djeffries?page=1" #for other people
    f"https://www.chess.com/games/archive?gameOwner=my_game&gameType=live&page={page_nr}" #for myself

    person = "?gameOwner=my_game&gameType=live&"
    # person = "/djeffries?"


    driver.get(f"https://www.chess.com/games/archive{person}page={page_nr}")
    overview_tab = driver.current_window_handle
    games = driver.find_elements(By.XPATH, '//a[contains(@class,"archive-games-link") and contains(text(), "Review")]')
    if len(games) > 0:
        print (f"Begin analysing {len(games)} games...")
        for idx, game in enumerate(games):
            game_url = game.get_attribute('href')
            driver.switch_to.new_window('tab')
            driver.get(game_url)
            randsleep()

            driver.close()
            print(f"Analysed game {idx + 1}: {game_url}")
            randsleep()

            driver.switch_to.window(overview_tab)
    else:
        print("No games found on the current page.")
    page_nr = page_nr + 1
    randsleep()

print("Analysis complete.")
print("--- %s seconds ---" % (time.time() - start_time))