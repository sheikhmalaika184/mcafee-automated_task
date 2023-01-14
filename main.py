
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re

DRIVER_PATH = '/Users/malaikasheikh/python/chromedriver'

#reading emails
registered_file = open("registered_email.txt","a")
check_file = open("check.txt","r")
emails = check_file.readlines()
count = 0

for email in emails:
  driver = webdriver.Chrome(executable_path=DRIVER_PATH)
  driver.get('https://www.mcafee.com/')
  time.sleep(3)
  navbar = driver.find_element(By.CLASS_NAME , "navbarContent")
  ul_tags = navbar.find_elements(By.TAG_NAME,"ul")
  for i in range(len(ul_tags)):
    try:
      a_tag = ul_tags[i].find_element(By.TAG_NAME,"a")
      if(a_tag.get_attribute("id") == "loginbtn"):
        a_tag.click()
        time.sleep(5)
        break
    except:
      continue
  #switch to second tab 
  driver.switch_to.window(driver.window_handles[1])
  time.sleep(2)
  buttons_tags = driver.find_elements(By.TAG_NAME,"button")
  for button in buttons_tags:
    if(button.get_attribute("id") == "sign-in-with-onetime-passcode-button"):
      button.click()
      time.sleep(3)
      break
  print(email)
  form_tag = driver.find_element(By.TAG_NAME,"form")
  input_tags = form_tag.find_elements(By.TAG_NAME,"input")
  buttons = form_tag.find_elements(By.TAG_NAME,"button")
  #entering email 
  for input_tag in input_tags:
    if(input_tag.get_attribute("id")== "email"):
      input_tag.send_keys(email)
      break
  #clicking continue button
  for button in buttons:
    if(button.get_attribute("id")== "otp-login-continue-button"):
      button.click()
      time.sleep(3)
      break
  body_tag = driver.find_element(By.TAG_NAME,"body")
  #saving emails
  if(f"We sent it to you at " in body_tag.text):
    print("Registered")
    registered_file.write(email + "\n")
  else:
    print("Not Registered")
  driver.close()
  driver.switch_to.window(driver.window_handles[0])
  driver.close()

registered_file.close()
check_file.close()