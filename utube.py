import command
import webbrowser
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def openUtube():
            command.speak("openning you tube Boss, Wait a second and it will there for entertainment")
            # webbrowser.open("youtube.com")
            command.speak("What you want to search on youtube boss")
            query=command.takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

def openUtube1():
            command.speak("openning you tube Boss, Wait a second and it will there for entertainment")
            command.speak("What you want to search on youtube boss")
            query=command.takeCommand()
            t=query.split()
            print(t[0])
            print(t[1])
            url="https://www.youtube.com/results?search_query="+t[0]+"+"+t[1]
            Client=urlopen(url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            Video_list=soup_page.findAll("item")
            for video in Video_list[0:4]:
                command.speak(video.title.text)
                

    
                