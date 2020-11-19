from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
#driver = webdriver.Chrome() 
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
#driver=webdriver.Chrome(r"../browsers/chromedriver",options=chrome_options) 
driver=webdriver.Chrome(r"../browsers/chromedriver")   
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("https://www.instagram.com/?hl=en")  
#identify the Google search text box and enter the value  
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]').click()
time.sleep(3)
driver.find_element_by_name("email").send_keys("prs786") 
driver.find_element_by_name("pass").send_keys("chapal") 
driver.find_element_by_name("login").click()
time.sleep(5)  
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
# #click on the Google search button  
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
# time.sleep(3)  
#close the browser
time.sleep(3)  
driver.close()  
print("sample test case successfully completed")  