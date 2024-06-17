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
       self.driver.get(data2.WebData().url2)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()
       
   def fillText(self, locator, value):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(value)


   def clickButton(self, locator):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()


   def login(self):
       #try:
           self.boot()
           sleep(10)
           self.fillText(locator2.WebLocators().UsernameLocator2_1, data2.WebData().username2)
           self.fillText(locator2.WebLocators().PasswordLocator2, data2.WebData().password2)
           self.clickButton(locator2.WebLocators().LoginbuttonLocator2)
           sleep(10)
           self.clickButton(locator2.WebLocators().AdminbuttonLocator2)
           sleep(5)
           self.clickButton(locator2.WebLocators().UserManagementLocator2)
           print("UserManagement option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().jobLocator2)
           print("Job option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().Organization2)
           print("Organization option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().Qualifications2)
           print("Qualifications option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().Nationalities2)
           print("Nationalities option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().CorporateBranding2)
           print("CorporateBranding2 option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().Configuration2)
           print("Configuration option is displaying on admin page")
           sleep(10)




obj = LoginPage()
obj.login()
