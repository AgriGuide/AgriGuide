from flask import Flask, request, jsonify
from lookup_table import lookup_table

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_crops():
    data = request.get_json()
    
    temp = data.get("temperature")
    rainfall = data.get("rainfall")
    soil_type = data.get("soil_type")
    
    if temp is None or rainfall is None or soil_type is None:
        return jsonify({"error": "Missing parameters"}), 400
    
    crops = lookup_table(temp, rainfall, soil_type)
    return jsonify({"predicted_crops": crops})

if __name__ == '__main__':
    app.run(debug=True)