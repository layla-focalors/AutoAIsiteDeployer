import os
import datetime
# import handler
import hashlib
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pymysql
from pydantic import BaseModel
import uvicorn

def sha1_for_largefile(filepath, blocksize=8192):
    sha_1 = hashlib.sha1()
    filepath = filepath + '/index.html'
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    # return sha_1.hexdigest()
    return {'Hash': sha_1.hexdigest(), 'Status': 'Success'}

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
    
def deploy_to_fastapi(location:str, git_url:str):
    print('debug : call-hook is called')

    templates = Jinja2Templates(directory=f"{location}")
    app = FastAPI(docs_url="/documentation", redoc_url=None)
    @app.get("/")
    async def home(request: Request):
        ORIGIN_ID = sha1_for_largefile(location)
        print(ORIGIN_ID)
        makegit(location, git_url)
        if(ORIGIN_ID != sha1_for_largefile(location)):
            print(f'[{gettime()}] Web File Changed\norigin {ORIGIN_ID["Hash"]} : now {sha1_for_largefile(location)["Hash"]}')
            ORIGIN_ID = sha1_for_largefile(location)
            makegit(location, git_url)
        return templates.TemplateResponse("index.html",{"request":request})
    
    uvicorn.run(app, host="", port=3000)
    return {'response':{'http://localhost:3000 : FastAPI Server Started'}}