from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(""))

driver.get('http://127.0.0.1:5001/users/get_user_data/0')
user_element = driver.find_element(By.ID, value='user')
if user_element:
    print(user_element.text)
