"""
locator.py
"""
class WebLocators:


   def __init__(self):
   #AT_project2:TC_PIM_01
       self.ForgotyourpasswordLocator1 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
       self.UsernameLocator1            = "//input[@placeholder='Username']"   
       self.ResetPasswordLocator1 = "//button[text()=' Reset Password ']"
       
   #AT_project2:TC_PIM_02
       self.UsernameLocator2_1 = "//input[@placeholder='Username']"
       self.PasswordLocator2 = "//input[@placeholder='Password']"
       self.LoginbuttonLocator2 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.AdminbuttonLocator2 = "//span[text()='Admin']"
       self.UserManagementLocator2 ="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"
       self.jobLocator2 = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
       self.Organization2="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span"
       self.Qualifications2="//span[text()='Qualifications ']"
       self.Nationalities2="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a"
       self.CorporateBranding2="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a"
       self.Configuration2="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
   # AT_project1:TC_PIM_01
       self.UsernameLocator3 = "//input[@placeholder='Username']"
       self.PasswordLocator3 = "//input[@placeholder='Password']"
       self.LoginbuttonLocator3 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.AdminbuttonLocator3 = "//span[text()='Admin']"
       self.PIMbuttonLocator3 = "//span[text()='PIM']"
       self.LeavebuttonLocator3 = "//span[text()='Leave']"
       self.TimebuttonLocator3  ="//span[text()='Time']"
       self.RecruitmentbuttonLocator3 ="//span[text()='Recruitment']"
       self.MyInfobuttonlocator3 ="//span[text()='My Info']"
       self.PerformancebuttonLocator3 = "//span[text()='Performance']"
       self.DashboardbuttonLocator3 ="//span[text()='Dashboard']"
       self.DirectorybuttonLocator3 = "//span[text()='Directory']"
       self.MaintencebuttonLocator3 = "//span[text()='Maintenance']"
       self.ClaimbuttonLocator3 = "//span[text()='Claim']"
       self.BuzzbuttonLocator3 = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span"
       self.PasswordLocator3_1 = "/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input"
       self.ConfirmLocator3    = "/html/body/div/div[1]/div[1]/form/div[4]/button[2]"