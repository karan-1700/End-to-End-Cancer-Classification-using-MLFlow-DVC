import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from CNN_Classifier.utils.common import decodeImage
from CNN_Classifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# initialize flask
app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# create a default route
@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

# create a training route
@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py") # you can also write `dvc repro` command instead of `python main.py`.
    return "Training done successfully!"

# create a prediction route
@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json["image"]
    decodeImage(image, client_obj.filename)
    result = client_obj.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    client_obj = ClientApp()
    app.run(host="0.0.0.0", port=8080)

