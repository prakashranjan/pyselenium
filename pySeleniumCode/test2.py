from selenium import webdriver


browser = webdriver.Chrome()
browser.set_window_size(1024, 768)

browser.get("https://www.moneycontrol.com/")



browser.close()

