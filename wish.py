import command
import datetime


def wishMe():
        hour =int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            command.speak("Good Morning")
        elif hour>=12 and hour <18:
            command.speak ("Good Afternoon")
        else:
            command.speak("Good Evining")
        command.speak("I am Simhha ,,. bossom buddy of Dnyanesh. I can do so many things for you ")   

