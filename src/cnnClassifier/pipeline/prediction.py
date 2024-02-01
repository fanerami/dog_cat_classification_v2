import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from cnnClassifier import logger
from pathlib import Path

STAGE_NAME = "Prediction"
class PredictionPipeline:
    def __init__(self, filename) -> None:
        self.filename= filename


    def predicition(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)/255

        test_image = np.expand_dims(test_image, axis = 0)

        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'Cat'
            return [{ "image" : prediction}]



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PredictionPipeline(Path("artifacts/data_ingestion/dog_cat_data/cat/cat.8.jpg"))
        print(obj.predicition())
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
