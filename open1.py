import os
import command

def open_app(input): 
  
    if "chrome" in input: 
        command.speak("Google Chrome") 
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        command.speak("Opening Mozilla Firefox") 
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') 
        return
  
    elif "word" in input: 
        command.speak("Opening Microsoft Word") 
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2015\\Word 2015.lnk') 
        return
  
    elif "excel" in input: 
        command.speak("Opening Microsoft Excel") 
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2015\\Excel 2015.lnk') 
        return
  
    else: 
  
        command.speak("Application not available") 
        return