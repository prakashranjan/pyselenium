from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.set_window_size(1024, 768)
browser.get("https://www.moneycontrol.com/")
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
email.send_keys("prakashranjansingh04@gmail.com")
pwd.send_keys("Mmm@1111")
SubmitLogin.click()
browser.find_element(By.XPATH,"//span[@class='usr_nm']").text









browser.close()

