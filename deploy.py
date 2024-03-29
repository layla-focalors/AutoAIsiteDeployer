import os
import datetime

def gettime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def makegit(location:str, git_url:str):
    
    if(git_url == None):
        print('No Location Specified')
        return
    
    if(location == None):
        location = './deploy'
    
    os.chdir(location)
    os.system('git init')
    os.system('git add .')
    os.system('git status')
    os.system('git branch -M main')
    os.system('git remote add origin ' + git_url)
    os.system(f'git commit -m "Auto Deployed {gettime()}"')
    os.system(f'git push -u origin main')
    print(f'[{gettime()}] Upload Site File Complete')