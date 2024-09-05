import env 
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def search_movies(driver):
    driver.find_element(By.NAME, 'q').send_keys("Movies"+Keys.RETURN)

def assert_search_title(driver):
    print(driver.title)
    assert driver.title == "Movies - Google Search", "Title does not match"

def click_signin(driver):
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()

def main():
    driver = setup_driver(env.URL)
    search_movies(driver)
    assert_search_title(driver)

if __name__ == "__main__":
    main()