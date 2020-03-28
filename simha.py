import pyttsx3
import  sys, os
import datetime
import time
import command
#import ConfigParser
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
#for getting news
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
#for getting wether report
import requests, json 
import pyaudio
#err = Pa_Initialize();
from weather import Weather, Unit
import chat1
import jock
import mail1
import re
import birthday
import wish
import googleSearch




if __name__=="__main__":
   
    wish.wishMe()
    answer='yes'
    while answer == 'yes':
        command.speak("Please , Tell me what can I do ?")
        
        query = command.takeCommand().lower()
    
        if 'talk' in query:
            command.speak("Ok boss , its seems like you have a free time  I am ready")
            chat1.chatty()
        elif 'birthday' in query:
            birthday.handle()
        
        elif 'bye' in query:
            command.speak("by boss , come back again . i will be there for sure")
            
        elif 'what can you do' in query:
            command.speak("I can do , whatever which you taught me")
        elif 'news' in query:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            speak('now  ,I will read news for you boss , please listen it carefully,,')
            for news in news_list[0:4]:
                command.speak(news.title.text)
        elif ' weather report' in query:
            pi_key = "Your_API_Key"
  
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
             
            command.speak("boss tell me city name")
            city_name = command.takeCommand().lower()
  
            
            complete_url = base_url + "appid=" + pi_key + "&q=" + city_name 
            
            response = requests.get(complete_url) 
  
             
            x = response.json() 
             
            if x["cod"] != "404": 
  
                
                  y = x["main"] 
  
                  current_temperature = y["temp"] 
   
                  current_pressure = y["pressure"] 
  
                  current_humidiy = y["humidity"] 
   
                  z = x["weather"] 
  
                  weather_description = z[0]["description"] 
                  speak(f'current tempreture is {current_tempreture}')
                  speak(f'current pressure is {current_pressure}')
                  speak(f'current humidity is {current_humidity}')
                  
        elif 'wikipedia' in query :
            
            command.speak("Searching wikipedia boss ,wait a second")
            query =query.replace("wikipedia",'')
            results=wikipedia.summary(query,sentences=2)
            command.speak("According to Wikipedia")
            print(results)
            command.speak(results)
        elif "open youtube" in query:
            command.speak("openning you tube Boss, Wait a second and it will there for entertainment")
            webbrowser.open("youtube.com")
            time.sleep(3)
   
        elif 'open google' in query:
             command.speak("openning Google Boss, Wait a second")
             webbrowser.open("google.com")
             
        elif 'open facebook' in query:
            command.speak("openning Facebook Boss ,Wait a second")
            webbrowser.open("facebook.com")
            time.sleep(3)
        elif 'play music' in query:
            command.speak("playing your Favorite song Boss, Wait a second")
            music_dir ='E:\\Hindi\\00  3 Idiots'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            command.speak(f"Sir ,the time is {strTime}")
        elif 'email' in query:
            try:
                mail1.mail2()
            except Exception as e:
                print(e)
                command.speak("sorry friend email cants send")
        elif 'define yourself '  in query:
            command.speak("YOu want to know about me , I like it . I am Simhha ,. Personal Assistant of Dnyanesh . i devolped by my boss as part of his study . my date of birth 27 july 2019 . i am getting new features ")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open file' in query:
            command.speak("ok boss , which file you want to open")
            content=command.takeCommand()
            try:
                path="E:/"+content
                path=os.path.realpath(path)
                os.startfile(path)
            except Exception :
                command.speak("file not Found boss , sorry")
        elif 'joke' in query:
            jock.jock1()
        elif 'finance' in query:
            command.speak("boss , i getting todays Finance update for you , look at your screen")
            webbrowser.open("www.google.com/finance")
            command.speak("how much time you want to stay on this Finance site boss")
            tt=takeCommand()
            command.speak("ok boss , i will remind you after time over")
            time.sleep(4)
            #time.sleep(int(re.search(r'\d+', tt).group()))
            command.speak("time over boss , come back . ")
        elif 'close' in query:
            webbrowser.close()
        elif 'map' in query:
            webbrowser.open("https://www.google.com/maps/@18.4699367,73.8213773,14z")
        elif 'search' in query:
            googleSearch.opening()
        elif 'hear' in query:
            command.speak("yes bosssss , i am there, for sure, always ")
        else:
            command.speak("command not understood boss")
        
        answer='no'    
            
        command.speak("you want to continue boss")
        
        answer=command.takeCommand().lower()
        if 'no' in answer :
            command.speak("Ok boss , see you Again , bye")
        
            
    
    
    
    
    


 
