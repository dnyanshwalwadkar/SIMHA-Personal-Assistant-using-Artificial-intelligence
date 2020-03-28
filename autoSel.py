import command
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
ans='yes'

def doAuto():
    
    try:
        driver=webdriver.Chrome(executable_path="C:\drive\chromedriver.exe")
        driver.get("https://www.google.com/")
        command.speak("Boss , What you want to search ")
        query=command.takeCommand().lower()
        inputField=drive.find_element_by_name("q")
        inputField.sendKeys(query)

        while( ans == 'yes'):
            command.speak("Boss , Got Desired Result . if not then I can Go back")
            go=command.takeCommand()
            if 'back' in go:
                drive.back()
            else :
                command.speak("boss ok")
    except:
         command.speak("Boss Error Occured")
            