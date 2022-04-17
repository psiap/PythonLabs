import multiprocessing
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def parser_tw(tag):
    final_count = 0
    options = Options()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.headless = True  #
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'), options=options)

    driver.get(f'https://twitter.com/search?q={tag}&src=typed_query&f=user')
    time.sleep(5)
    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        turbo_array = []
        new_height = driver.execute_script("return document.body.scrollHeight")
        [turbo_array.append(username.text) for username in driver.find_elements(by=By.CLASS_NAME, value='css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l')]
        time.sleep(1)
        turbo_array = list(set(turbo_array))
        final_count += len(turbo_array)
        print(f'Спарсило: {len(turbo_array)}/{final_count}')
        with open('filepars.txt', 'a+', encoding='utf-8') as file:
            for row in turbo_array:
                file.write(str(row) + '\n')
        if new_height == last_height:
            break
        last_height = new_height
        with open('filepars.txt', 'r+', encoding='utf-8') as file:
            print('Спарсило всего - ',len([link for link in file.readlines()]))
        #break

    driver.quit()

#

with open('links_coin.txt', 'r+',encoding='utf-8') as file:
    mass_array = [link.split('/')[-2] for link in file.readlines()]
mass_array.reverse()
print(mass_array)
with multiprocessing.Pool(3) as pool:
    pool.map(parser_tw, mass_array)
#with open('filepars.txt') as in_fh, open('deduplicated.txt', 'w') as out_fh:
#    out_fh.write(''.join(set(in_fh)))



