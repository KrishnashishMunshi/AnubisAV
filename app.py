import os
import sys
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import lightgbm as lgb
from werkzeug.utils import secure_filename

# --- Add the 'app' directory to Python's path ---
# This allows importing modules directly from the 'app' directory,
# such as your 'ember' module located at app/ember.
current_dir = os.path.dirname(os.path.abspath(__file__))
app_module_path = os.path.join(current_dir, 'app')
sys.path.insert(0, app_module_path)

# Now, you can import 'ember' as if it were a top-level package
import ember

# --- Configuration ---
# IMPORTANT: Adjust these paths and settings to match your setup!

# Path to your trained LightGBM model file
# Based on your screenshot, your model is likely named 'ember_model_2018.txt' or similar.
# Please replace 'ember_model_201X.txt' with the exact name of your model file.
MODEL_FILE_NAME = "ember_model_2018.txt" # e.g., "ember_model_2018.txt"
MODEL_PATH = os.path.join("models", MODEL_FILE_NAME)

# Set the EMBER feature version that your model was trained with
# For EMBER 2018, this is typically 2. If you are using EMBER2024, it would be 3.
EMBER_FEATURE_VERSION = 2 # Adjust this based on your model

# Directory where uploaded files will be temporarily stored.
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'exe', 'dll', 'sys', 'ocx', 'scr', 'cpl', 'drv', 'efi', 'mui', 'pif'}

# --- Flask App Setup ---
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkeyforthisdemo' # Change this to a strong, random key in production!

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# Ensure the models folder exists (and remind user to place model there)
os.makedirs("models", exist_ok=True)

# --- Global Model Loading ---
lgbm_model = None
try:
    if os.path.exists(MODEL_PATH):
        lgbm_model = lgb.Booster(model_file=MODEL_PATH)
        print(f"Successfully loaded LightGBM model from {MODEL_PATH}")
    else:
        print(f"ERROR: Model file not found at {MODEL_PATH}. Please train a model and place it there.")
        print("The application will run, but predictions will not work without a model.")
except Exception as e:
    print(f"ERROR: Could not load LightGBM model: {e}")
    print("Please ensure 'lightgbm' and 'ember' libraries are correctly installed.")
    lgbm_model = None

def allowed_file(filename):
    """Checks if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Renders the main upload form page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles file upload, prediction, and returns results as JSON.
    This route is now an API endpoint for the frontend.
    """
    if lgbm_model is None:
        return jsonify({"error": "ML model not loaded. Cannot make predictions."}), 500

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        prediction_score = None
        prediction_label = "Unknown"
        try:
            with open(filepath, "rb") as f:
                file_data = f.read()

            prediction_score = ember.predict_sample(lgbm_model, file_data, EMBER_FEATURE_VERSION)

            if prediction_score is not None:
                if prediction_score > 0.5: # Common threshold for binary classification probabilities
                    prediction_label = "Malicious"
                else:
                    prediction_label = "Benign"
            else:
                prediction_label = "Prediction Failed"

        except Exception as e:
            print(f"Error during prediction for {filename}: {e}")
            prediction_label = "Error" # Generic error for frontend
            # Return a more specific error message for debugging if needed
            return jsonify({"error": f"An error occurred during prediction: {str(e)}",
                            "filename": filename}), 500
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"Cleaned up temporary file: {filepath}")

        # Return JSON response
        return jsonify({
            "filename": filename,
            "score": float(prediction_score) if prediction_score is not None else None,
            "label": prediction_label
        })
    else:
        return jsonify({"error": "Allowed file types are " + ', '.join(ALLOWED_EXTENSIONS)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)