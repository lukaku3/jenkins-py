# -*- conding:utf8 -*-
import os
import re
import unittest
import utils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class SimpleTest(unittest.TestCase):
    def setUp(self):
        baseurl = 'http://192.168.11.102:18002/?site_id=&status=&sort=9'
        self.wait = 10 # seconds
        self.url = baseurl
        #self.driver = webdriver.Chrome('../lib/chromedriver')
        self.driver = webdriver.Firefox()
        self.dir = './saved/'
        self.new_fle_ext = '.txt'
        self.user = ''
        self.password = ''

    def tearDown(self):
        self.driver.quit()


    def test_login_out(self):
        driver = self.driver
        driver.get( self.url )
        driver.find_element_by_name('login_id').send_keys(self.user)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/form/div[3]/div/button').click()

        driver.find_element_by_xpath('//*[@id="form-list-change"]/select[3]').click()
        driver.find_element_by_xpath('//*[@id="form-list-change"]/select[3]/option[6]').click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination")))

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        tbl = soup.find_all("table", class_="table table-condensed")
        print(tbl)

if __name__ == "__main__":
  unittest.main()

