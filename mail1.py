import command      

        
mailDict={'me':'dnyaneshwalwadkar10@gmail.com','suarav':'ysaurav132@gmail.com','jayesh':'patiljayesh1421999@gmail.com','mujahid':'hussainmujahid51@gmail.com'}
    
def mail2():
        command.speak("whom you want to send")
        print(mailDict.keys())
        who=command.takeCommand()
        
        try:
            
            to=mailDict[who]
            command.speak("what shoul I say")
            content=command.takeCommand()
            command.sendEmail(to,content)
            command.speak("email has send")
        except Exception:
            command.speak("We not have mail Id, of this person in our database boss")
        
