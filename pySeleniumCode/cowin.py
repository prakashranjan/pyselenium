from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as re
import json

data = {}
data['userDetails'] = []

for x in range(2000,9999,1):
    status="No"
    phoneNo= "99999"+str(x)+"9"
    link = "https://www.cowin.gov.in/api/v1/user/verifyPhoneNumber/"+phoneNo
    # print (link)
    phoneData = re.get(link)
    # print(phoneData.json())
   
    if 'error' not in phoneData.json():
        status = "Yes"
        data['userDetails'].append({
        'PhoneNumber': phoneNo,
        'registered': status
        })
        with open('./Cowin_data/cowin_phone_data.json', 'w') as json_file:
            json.dump(data, json_file)

    


    









