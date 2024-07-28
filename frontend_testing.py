import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_driver():
    chrome_service = Service("/usr/local/bin/chromedriver" if platform.system() == "Linux" else "")
    chrome_options = Options()

    # Set headless options if running on Linux (server)
    if platform.system() == "Linux":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--remote-debugging-port=9222')

    return webdriver.Chrome(service=chrome_service, options=chrome_options)


driver = get_driver()
driver.get('http://127.0.0.1:5001/users/get_user_data/0')
user_element = driver.find_element(By.ID, value='user')
if user_element:
    print(user_element.text)
driver.quit()
