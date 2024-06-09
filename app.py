from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.pipeline.prediction_pipeline import PredictionPipeline




text:str = 'What is the Text Summarization?'

app = FastAPI()

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


# @app.get('/train')
# async def train():
#     try:
#         os.system('python main.py')
#         return Response(status_code=200)
    
#     except Exception as e:
#         return Response(status_code=500)
    
@app.get('/predict')
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        return e
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    
