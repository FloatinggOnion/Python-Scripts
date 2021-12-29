from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Moodle_Email = input("Enter Email: ")
Moodle_Password = input("Enter Password: ")

#Opening Chrome and Going to the website
driver = webdriver.Chrome()
driver.get("https://moodle.cu.edu.ng/")

#Clicking the login button
Login_Button = driver.find_element_by_link_text("Log in").click()

#Filling the username
Username_Filler = driver.find_element_by_name("username").send_keys(Moodle_Email)

#Filling the password
Password_Filler = driver.find_element_by_id("password").send_keys(Moodle_Password)

#Clicking the 'submit' button
SignIn_Button = driver.find_element_by_id("kc-login").click()