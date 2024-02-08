from fastapi import FastAPI
from pydantic import BaseModel
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

app = FastAPI()

prediction_pipeline = PredictionPipeline("temp_image.jpg")



@app.get("/")
async def hello_world():
    return {"message": "Hello World, you can use this api to predict dog or cat from image. Go to /prediction endpoint"}

@app.get("/{name}")
async def hello_custom(name):
    return {"message": f"Hello {name}"}




class ImageBase64(BaseModel):
    value: str

@app.post("/prediction")
async def prediction(image_base64: ImageBase64):

    decodeImage(image_base64.value, prediction_pipeline.filename)
    result = prediction_pipeline.predict()
    return result



