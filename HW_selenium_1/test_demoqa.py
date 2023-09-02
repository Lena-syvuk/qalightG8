
from selenium.webdriver.common.by import By
import logging
import time


def test_1(chrome):
    chrome.get('https://demoqa.com/text-box')
    full_name_field = chrome.find_element(By.XPATH, '//input[@id="userName"]')
    full_name_field.send_keys('Lena')
    email_field = chrome.find_element(By.XPATH,'//input[@id="userEmail"]')
    email_field.send_keys('Lena@gmail.com')
    curr_addr_text_area = chrome.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    curr_addr_text_area.send_keys('London,Baker Street')
    perm_addr_text_area = chrome.find_element(By.XPATH, '//textarea[@id ="permanentAddress"]')
    perm_addr_text_area.send_keys('London,Baker Street')
    button = chrome.find_element(By.XPATH, '//button[@id="submit"]')
    button.click()
    time.sleep(4)

#Task_2
    result_name = chrome.find_element(By.XPATH, '//p[@id="name"]').text
    result_email = chrome.find_element(By.XPATH, '//p[@id ="email"]').text
    result_curr_addr = chrome.find_element(By.XPATH, '//p[@id="currentAddress"]').text
    result_perm_addr = chrome.find_element(By.XPATH, '//p[@id="permanentAddress"]').text

    logging.info(result_name)
    logging.info(result_email)
    logging.info(result_curr_addr)
    logging.info(result_perm_addr)









