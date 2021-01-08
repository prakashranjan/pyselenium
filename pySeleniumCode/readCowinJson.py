from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as re
import json


with open('./Cowin_data/cowin_phone_data.json') as f:
  data = json.load(f)

for x in data["userDetails"]:
    if x["registered"] == "Yes":
        print(x["PhoneNumber"])








