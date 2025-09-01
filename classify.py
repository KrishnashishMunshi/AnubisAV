import numpy as np
import lightgbm as lgb
import thrember
import os

# --- Global Objects ---
# These are loaded only once when the module is imported, making subsequent calls fast.
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'EMBER2024_all.model')
MODEL = None
EXTRACTOR = None

def initialize_classifier():
    """
    Loads the model and feature extractor into memory.
    This should be called once when your application starts.
    """
    global MODEL, EXTRACTOR
    try:
        if MODEL is None:
            print("Loading LightGBM model...")
            MODEL = lgb.Booster(model_file=MODEL_PATH)
        if EXTRACTOR is None:
            print("Initializing PE Feature Extractor...")
            EXTRACTOR = thrember.features.PEFeatureExtractor()
        print("Classifier initialized successfully.")
        return True
    except Exception as e:
        print(f"Error initializing classifier: {e}")
        return False


def get_malice_score(file_path):
    """
    Analyzes a given executable file and returns its malice probability score.

    Args:
        file_path (str): The full path to the file to be analyzed.

    Returns:
        float: A probability score between 0.0 and 1.0, where a higher value
               indicates a higher probability of being malicious.
        None: If the file cannot be found, read, or processed.
    """
    if MODEL is None or EXTRACTOR is None:
        print("Error: Classifier is not initialized. Call initialize_classifier() first.")
        return None

    # 1. Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return None

    try:
        # 2. Read the file's binary content
        with open(file_path, "rb") as f:
            file_bytes = f.read()

        # 3. Extract the feature vector
        features = EXTRACTOR.feature_vector(file_bytes)
        
        # Handle cases where features can't be extracted (e.g., not a valid PE file)
        if features is None:
            print(f"Warning: Could not extract features from {os.path.basename(file_path)}. It may not be a valid PE file.")
            # Returning a score of -1 can help the GUI identify this specific case
            return -1.0 

        # 4. Reshape features and predict
        features = features.reshape(1, -1)
        probability = MODEL.predict(features)[0]

        return probability

    except Exception as e:
        print(f"An error occurred during analysis of {os.path.basename(file_path)}: {e}")
        return None

# --- Example Usage ---
# This block will only run if you execute this script directly (e.g., `python classify.py`)
# It's useful for testing the function without needing the GUI.
if __name__ == "__main__":
    # Initialize the classifier first
    if initialize_classifier():
        # Create a dummy file for testing purposes if it doesn't exist
        test_file = 'dummy_test_file.exe'
        if not os.path.exists(test_file):
            print(f"Creating a dummy file for testing: {test_file}")
            with open(test_file, 'w') as f:
                f.write("This is not a real executable.")
        
        print("\n--- Testing with a non-PE file ---")
        score = get_malice_score(test_file)
        if score is not None:
             print(f"Malice score for '{test_file}': {score:.4f}")
        
        # IMPORTANT: Replace this with a path to a REAL executable file for a valid test
        # real_exe_path = "/path/to/your/test.exe" 
        # print(f"\n--- Testing with a real PE file (replace path) ---")
        # score = get_malice_score(real_exe_path)
        # if score is not None:
        #     print(f"Malice score for '{os.path.basename(real_exe_path)}': {score:.4f}")
