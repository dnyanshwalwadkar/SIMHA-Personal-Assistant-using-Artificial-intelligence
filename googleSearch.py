import webbrowser
import command
import time

timeDict={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}


def opening():
            command.speak("ok ,boss What you want to search , on google")
            se= command.takeCommand()
            command.speak("got it boss ,opening site")
            webbrowser.open('https://www.google.com/search?source=hp&ei=NMM9XcOUMZum9QONxqX4Dg&q='+se+'&oq='+se+'&gs_l=psy-ab.3..0i131j0l4j0i131j0l2j0i131j0.4879.5182..7055...0.0..0.119.346.0j3......0....1..gws-wiz.....0.006_ngXOeMs&ved=0ahUKEwjD_vHe-tfjAhUbU30KHQ1jCe8Q4dUDCAU&uact=5')
            command.speak("how much seconds, you want you spend here, boss?")
            try:
                t= command.takeCommand().lower()
                for key in timeDict:
                    if key == t:
                        value=timeDict[t]
                        command.speak("ok Boss, i will remind you after Time over !")
                        print(value)
                        time.sleep(value)
                        command.speak("Time Over Boss")
            except Exception :
                 command.speak("Boss Time Not Understood , Default Timer I will set For You")
                    
                   
                    
           
            
            
                
                
