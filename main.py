import os
import io
import json
import base64
import hashlib
import asyncio 
import uvicorn
import pandas as pd
from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI, Header,Request,File, UploadFile,status,Form
from fastapi.responses import StreamingResponse,FileResponse,Response
from typing import Dict,List,Any,Union
from fastapi.middleware.cors import CORSMiddleware
from CaesarAIGemini.CaesarAIGemini import CaesarAIGemini



load_dotenv(".env")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


caesargemini = CaesarAIGemini()

JSONObject = Dict[Any, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@app.get('/')# GET # allow all origins all methods.
async def index():
    return "Welcome to CaesarAIGemini!"

@app.get('/sendmessage')# GET # allow all origins all methods.
async def sendmessage(message:str):
        try:
            result = caesargemini.send_message(message)

            return StreamingResponse(result,media_type='text/event-stream')
  
        except Exception as ex:
            return {"error":f"{type(ex)},{ex}"}

@app.get('/gethistory')# GET # allow all origins all methods.
async def gethistory():
        try:
            if len(caesargemini.chat.history) == 0:
                 return {"message":"no previous history"}
            else:
                result = caesargemini.get_history()
                #return {"history":result}
                return StreamingResponse(result,media_type="application/stream+json")
  
        except Exception as ex:
            return {"error":f"{type(ex)},{ex}"}

@app.post('/sendvision')# GET # allow all origins all methods.
async def sendvision(file: UploadFile = File(...)):
        try:
            img_content =  await file.read()
    
            result = caesargemini.describe_image(img_content)
            return {"output_text":result}
     
  
        except Exception as ex:
            return {"error":f"{type(ex)},{ex}"}
@app.post('/sendcsv')# GET # allow all origins all methods.
async def sendcsv(message : Annotated[str, Form()],file: UploadFile = File(...)):
        try:
            csv_content =  await file.read()
            csv_stream = io.BytesIO(csv_content)
            csv_stream.seek(0)
            df = pd.read_csv(csv_stream).head(30) 
            if "statements" in df.columns:
                return StreamingResponse(caesargemini.send_message_csv(df,message),media_type='text/event-stream')
            else:
                return {"error":"Make sure that there is a column with column name 'statements'."}
                

  
                
                

            #result = caesargemini.send_message(message)

#            

    

     
  
        except Exception as ex:
            return {"error":f"{type(ex)},{ex}"}

if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
    #uvicorn.run()
    #asyncio.run(main())