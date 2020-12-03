from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
caps['load-extension'] = True

browser = webdriver.Chrome(desired_capabilities=caps)
browser.set_window_size(1024, 768)
browser.get("https://www.moneycontrol.com/")
browser.implicitly_wait(10)
loginModalBtn = browser.find_element(By.XPATH,"//span[@class ='user_icon']")
loginModalBtn.click()


loginBtn = browser.find_element(By.XPATH,"//a[@title ='Log In']")
loginBtn.click()


# switch to selected iframe
browser.switch_to.frame("myframe")

# browser.find_element(By.ID, "ACCT_SIGNUP_BUTTON").click()

# emailDiv = browser.find_element(By.XPATH,"//*[@id='login_form']/div[1]")
email = browser.find_element(By.XPATH,"(//input[@id='email'])[2]")
pwd = browser.find_element(By.XPATH,"(//input[@id='pwd'])[2]")
SubmitLogin= browser.find_element(By.ID,"ACCT_LOGIN_SUBMIT")

# emailDiv.click()
print(browser.current_window_handle)

browser.implicitly_wait(2)
email.send_keys("prakashranjansingh04@gmail.com")
pwd.send_keys("Mmm@1111")
SubmitLogin.click()
browser.implicitly_wait(15)

welcomeText = browser.find_element(By.XPATH,"//span[@class='usr_nm']").text
print (welcomeText)

#search shriram
print(browser.current_window_handle)
browser.implicitly_wait(15)
browser.find_element(By.XPATH,"(//input[@id='search_str'])[1]").send_keys("shriram")
browser.implicitly_wait(5)
browser.find_element(By.XPATH,"(//div[@id='autosuggestlist']/ul/li)[1]/a").click()

# browser.implicitly_wait(10)

# browser.close()

