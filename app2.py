from flask import Flask, jsonify, request
from classifier2 import  get_prediction

app = Flask(__name__)

@app.route("/predict-letters", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("letters")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)