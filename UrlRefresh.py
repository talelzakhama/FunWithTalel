from selenium import webdriver
from inspect import getmembers, isfunction
import time



# Make sure you have the chromedriver installed in your computer.

class UrlRefresh():
    def url_refresh(self,path_to_chromedriver,url,sleep_time):
        driver = webdriver.Chrome(path_to_chromedriver)
         driver.get(url)
         
        while True:
            time.sleep(sleep_time)
            driver.refresh()
        driver.quit()
s=UrlRefresh()

if __name__ == '__main__':
    path_to_chromedriver='/Users/talelzakhama/Documents/UrlRefresh/chromedriver' #Path to Chrome Driver.
    url='https://realpython.com/python-pep8/' #URL
    sleep_time=5 #Cycle Length
    s.url_refresh(path_to_chromedriver,url,sleep_time)

