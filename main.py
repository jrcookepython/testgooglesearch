import time
from question import search_question_via
from text import TextRequest
from speech import SpeechRecording
from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import csv
import pyttsx3

TIMEOUT = 30
GOOGLE_SEARCH_FIELD = '//*[@id="APjFqb"]'

search_question = search_question_via()

if search_question.answer == 0:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(f"Hello!  What question do you have for me today?")
    engine.runAndWait()
    search_for = SpeechRecording()
    search_for = search_for.audio_text
elif search_question.answer == 1:
    search_for = TextRequest()
    search_for = search_for.search_data

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()



GOOGLE_SEARCH_FIELD_wait = expected_conditions.presence_of_element_located((By.XPATH, GOOGLE_SEARCH_FIELD))
WebDriverWait(driver, TIMEOUT).until(GOOGLE_SEARCH_FIELD_wait)

# time.sleep(100)

GOOGLE_SEARCH_FIELD_TEXTAREA = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
GOOGLE_SEARCH_FIELD_TEXTAREA.send_keys(search_for)
GOOGLE_SEARCH_FIELD_TEXTAREA.send_keys(Keys.ENTER)

test_search_request_page = driver.find_element(by=By.XPATH, value='/html/body')
print(test_search_request_page.text)
with open('mygooglesearch.csv' , 'a', encoding='UTF-8') as file:
    file.write(test_search_request_page.text)
with open('mygooglesearch.doc', 'a', encoding='UTF-8') as doc:
    doc.write(test_search_request_page.text)
# test_find = test_search_request_page.find_elements(by=By.CSS_SELECTOR, value='div')
#
# for item in range(0, len(test_find)):
#     print(item.__getattribute__())
#
# print(test_find)
time.sleep(1000)