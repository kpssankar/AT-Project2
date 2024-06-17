#Forgot password link validation on login page
from Data2 import data2
from Locator2 import locator2
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
  
   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       sleep(10)
       self.driver.implicitly_wait(10)
       self.wait = WebDriverWait(self.driver, 15)


   def boot(self):
       self.driver.get(data2.WebData().url1)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()
       
   def fillText(self, locator, value):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(value)


   def clickButton(self, locator):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()


   def login(self):
       try:
           self.boot()
           sleep(10)
           self.clickButton(locator2.WebLocators().ForgotyourpasswordLocator1)
           self.fillText(locator2.WebLocators().UsernameLocator1, data2.WebData().Username1)
           self.clickButton(locator2.WebLocators().ResetPasswordLocator1)
           sleep(10)


           if self.driver.current_url == data2.WebData().dashboardURL1:
               print("Reset password link sent successfully")
           else:
               print("Error in login")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()

obj = LoginPage()
obj.login()
