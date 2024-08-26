# Crop Prediction API and Script

This repository contains a Python script and a Flask API for predicting crops based on temperature, rainfall, and soil type. The prediction is made using a lookup table stored in an Excel file.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
  - [Command-Line Script](#command-line-script)
  - [Flask API](#flask-api)
- [Files](#files)
- [Extra info](#extra-information)

## Requirements

- Python 3.x
- Flask
- pandas

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/crop-prediction.git
    cd crop-prediction
    ```

2. **Install dependencies:**

    ```bash
    pip install Flask pandas
    ```

3. **Prepare the lookup table:**

   - Ensure the Excel file `lookup.xlsx` is located in the `lookup-table/data/` directory. This file should contain columns such as `soil-type`, `soil-type-2`, `temp-opt-min`, `temp-opt-max`, `rainfall-opt-min`, `rainfall-opt-max`.

## Usage

### Command-Line Script

You can use the script `lookup_table.py` to predict crops from the command line.

**Usage:**

```bash
python lookup_table.py <temp> <rainfall> <soil_type>
```

**Example:**

```bash
python lookup_table.py 25 1000 alluvial
```

This will output the top 3 predicted crops based on the provided parameters.

### Flask API

The API allows you to make POST requests with JSON payloads to predict crops.

1. **Run the Flask API:**

    ```bash
    python api.py
    ```

   The API will start on `http://127.0.0.1:5000`.

2. **Make a POST request:**

   You can use `curl`, Postman, or any other HTTP client to make a request.

   **Example:**

   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
   -H "Content-Type: application/json" \
   -d "{\"temperature\": 25, \"rainfall\": 1000, \"soil_type\": \"alluvial\"}"
   ```

   **Response:**

   ```json
   {
       "predicted_crops": ["Crop1", "Crop2", "Crop3"]
   }
   ```

## Files

- `lookup_table.py`: The script for predicting crops from the command line.
- `api.py`: The Flask API for predicting crops via POST requests.
- `lookup-table/data/lookup.xlsx`: The Excel file containing the lookup table.

## Extra Information

- `lookup.xlsx` is created from the `data.xlsx` file using the `data_cleansing.ipynb`. You can recreate it with it but the finished version is included under the data directory.

