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
       self.driver.get(data2.WebData().url3)
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
           self.fillText(locator2.WebLocators().UsernameLocator3, data2.WebData().username3)
           self.fillText(locator2.WebLocators().PasswordLocator3, data2.WebData().password3)
           self.clickButton(locator2.WebLocators().LoginbuttonLocator3)
           sleep(10)
           self.clickButton(locator2.WebLocators().AdminbuttonLocator3)
           print("Admin option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().PIMbuttonLocator3)
           print("PIM option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().LeavebuttonLocator3)
           print("Leave option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().TimebuttonLocator3)
           print("Time option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().RecruitmentbuttonLocator3)
           print("Recuritment option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().MyInfobuttonlocator3)
           print("MyInfo option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().PerformancebuttonLocator3)
           print("Performance option is displaying on admin page")
           sleep(5)
           self.clickButton(locator2.WebLocators().DashboardbuttonLocator3)
           print("Dashboard option is displaying on admin page")
           sleep(10)
           self.clickButton(locator2.WebLocators().DirectorybuttonLocator3)
           print("Directory option is displaying on admin page")
           sleep(10)
           self.clickButton(locator2.WebLocators().MaintencebuttonLocator3)
           print("Maintence option is displaying on admin page")
           sleep(10)
           self.fillText(locator2.WebLocators().PasswordLocator3_1, data2.WebData().password3_1)
           self.clickButton(locator2.WebLocators().ConfirmLocator3)
           sleep(10)
           self.clickButton(locator2.WebLocators().BuzzbuttonLocator3)
           print("Buzz option is displaying on admin page")
           sleep(10)






obj = LoginPage()
obj.login()
