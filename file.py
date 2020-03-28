import command
import sys,os

def openFile():
    
    command.speak("ok boss , which from which directory you want to open File")
    dire=command.takeCommand().lower()
    try:
        if 'e directory' in dire:
            command.speak("Enterd into E directory boss , Now You can See fIles Of this Directory on your Screen")
            path="E:/"
            list11=[x[0] for x in os.walk(path)]
            for each_dir in list11:
                     
                     print(each_dir)
            file=command.takeCommand().lower()
            path="E:/"+file
            path=os.path.realpath(path)
            os.startfile(path)
            command.speak("boss , this file contain Following directories ")
            list=[x[0] for x in os.walk(path)]
            for each_dir in list[1:10]:
                command.speak(" "+each_dir)
                print(each_dir)   
           
            command.speak("Which one you would like to open")
            file1=command.takeCommand()
            if file1 in list:
                path=path+file1
                path=os.path.realpath(path)
                os.startfile(path)
            elif file1.upper() in list:
                path=path+file1
                path=os.path.realpath(path)
                os.startfile(path)
            else:    
                
                command.speak("File Not Found Boss")
        elif 'd directory' in dire:
            command.speak("Enterd into D directory boss , Now You can See fIles Of this Directory on your Screen")
            path="D:/"
            list11=[x[0] for x in os.walk(path)]
            for each_dir in list11:
                     
                     print(each_dir)
            command.speak("Which one YOu Want Boss")  
            file=command.takeCommand().lower()
            path="D:/"+file
            path=os.path.realpath(path)
            os.startfile(path)
            command.speak("boss , this file contain Following directories ")
            list=[x[0] for x in os.walk(path)]
            for each_dir in list[1:10]:
                command.speak(" "+each_dir)
                print(each_dir)   
           
            command.speak("Which one you would like to open")
            file1=command.takeCommand()
            if file1 in list:
                path=path+file1
                path=os.path.realpath(path)
                os.startfile(path)
            elif file1.upper() in list:
                path=path+file1
                path=os.path.realpath(path)
                os.startfile(path)
            else :    
                command.speak("File Not Found Boss")
        elif 'f directory'  in dire:
                  command.speak("Enterd into F directory boss , Now You can See fIles Of this Directory on your Screen")
                  path="F:/"
                  list11=[x[0] for x in os.walk(path)]
                  for each_dir in list11:
                     
                     print(each_dir)
                  command.speak("Which one YOu Want Boss")  
                  file=command.takeCommand().lower()
                  path="F:/"+file
                  path=os.path.realpath(path)
                  os.startfile(path)
                  command.speak("boss , this file contain Following directories ")
                  list=[x[0] for x in os.walk(path)]
            
                  for each_dir in list[1:10]:
                     command.speak(" "+each_dir)
                     print(each_dir)   
           
                  command.speak("Which one you would like to open")
                  file1=command.takeCommand()
                  if file1 in list:
                    path=path+file1
                    path=os.path.realpath(path)
                    os.startfile(path)
                  elif file1.upper() in list:
                      path=path+file1
                      path=os.path.realpath(path)
                      os.startfile(path)  
                  else :
                     command.speak("File Not Found Boss") 
        elif 'c directory'  in dire:
                  command.speak("Enterd into C directory boss , Now You can See fIles Of this Directory on your Screen")
                  path="C:/"
                  list11=[x[0] for x in os.walk(path)]
                  for each_dir in list11[1:3]:
                     command.speak(" "+each_dir)
                     print(each_dir)
                  command.speak("Which one YOu Want Boss")      
                    
                  file=command.takeCommand().lower()
                  path="C:/"+file
                  path=os.path.realpath(path)
                  os.startfile(path)
                  command.speak("boss , this file contain Following directories ")
                  list=[x[0] for x in os.walk(path)]
            
                  for each_dir in list[1:10]:
                     command.speak(" "+each_dir)
                     print(each_dir)   
           
                  command.speak("Which one you would like to open")
                  file1=command.takeCommand()
                  if file1 in list:
                    path=path+file1
                    path=os.path.realpath(path)
                    os.startfile(path)
                  elif file1.upper() in list:
                     path=path+file1
                     path=os.path.realpath(path)
                     os.startfile(path)
                  else :
                     command.speak("File Not Found Boss")               
    except Exception:
            command.speak("file not Found boss , sorry")
