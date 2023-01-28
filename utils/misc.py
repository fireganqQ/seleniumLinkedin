# by https://github.com/fireganqQ #

from colorama import Fore
import os, time, selenium

from language import language

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class misc:
    def headBar():
        '''
            blue color header
        '''
        print(Fore.BLUE, "\tLINKLEDIN USER DATA", Fore.RESET)
    
    def clear():
        '''
            console clean up
        '''
        os.system('cls') # cleaning the console #
        misc.headBar()
    
    def infoMagenta(head, text):
        '''
            red color header and magenta clarification
        '''
        print(Fore.RED, head+":"+"\n\t", Fore.MAGENTA, text, Fore.RESET)
    
    def error(text):
        '''
            red color error message
        '''
        misc.clear()
        print(Fore.RED, text, Fore.RESET)

class handler:
    def __init__(self) -> None:
        '''
            Selenium module
        '''
        options = Options()
        # options.headless = True # Open web page in background

        self.driver  = webdriver.Chrome(options=options)

    def getPage(self, url):
        '''
            Open the web browser and login to the user page.
        '''
        try:
            self.driver.get(url)
        except selenium.common.exceptions.InvalidArgumentException:
            return language.get('pageError')
        except Exception as r:
            return str(r)
        time.sleep(5)
        return True
    
    def __content__(self):
        '''
            Web page content
        '''
        return self.driver.page_source
    
    def __about__(self):
        '''
            Getting information about.
        '''
        try:
            about = self.driver.find_element(By.XPATH, '//section[@class="core-section-container my-3 core-section-container--with-border border-b-1 border-solid border-color-border-faint m-0 py-3 pp-section summary"]/div/p').text
        except selenium.common.exceptions.NoSuchElementException:
            return language.get('aboutError')
        except Exception as r:
            return str(r)
        return about
    
    def __name__(self):
        '''
            name: User name
            lastName: User last name
        '''
        try:
            a = self.driver.find_element(By.XPATH, '//div[@class="top-card-layout__entity-info flex-grow flex-shrink-0 basis-0 babybear:flex-none babybear:w-full babybear:flex-none babybear:w-full"]/h1').text
        except selenium.common.exceptions.NoSuchElementException:
            return language.get('nameError'), language.get('lastnameError')
        except Exception as r:
            return str(r), str(r)
        a = a.split();lastName = a[-1];a.pop(-1);name = " ".join(a)
        return name, lastName
    
    def quit(self):
        '''
            close the browser.
        '''
        return self.driver.quit()