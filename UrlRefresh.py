from selenium import webdriver
from inspect import getmembers, isfunction
import time



# Make sure you have the chromedriver installed in your computer.

class UrlRefresh():
    def url_refresh(self,path_to_chromedriver,url,sleep_time):
        driver = webdriver.Chrome(path_to_chromedriver)
        # driver.quit()
        ## Enter URL here.
        driver.get(url)

        # Edit Varialbes here
        while True:
            time.sleep(sleep_time)
            driver.refresh()
        driver.quit()

s=UrlRefresh()
path_to_chromedriver='/Volumes/GoogleDrive/My Drive/TZ.KK/Academic Work_related_resources/Codes_Scripts/Talel_Draft_Codes/URL_Refresh/chromedriver'
url='https://realpython.com/python-pep8/'
sleep_time=5
s.url_refresh(path_to_chromedriver,url,sleep_time)

