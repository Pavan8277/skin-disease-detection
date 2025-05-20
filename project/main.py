from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from PIL import Image
import numpy as np
import tensorflow as tf

os.environ['TF_USE_LEGACY_KERAS'] = '1'

app = Flask(__name__)
CORS(app)

# Load model
model_path = r'C:\Users\pavan\OneDrive\Desktop\project\model\skin (2).h5'
model = None
try:
    model = tf.keras.models.load_model(
        model_path,
        custom_objects={'SparseCategoricalCrossentropy': tf.keras.losses.SparseCategoricalCrossentropy}
    )
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# Routes
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/login')
def login():
    return render_template('login.html')

import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf

os.environ['TF_USE_LEGACY_KERAS'] = '1'

app = Flask(__name__)
CORS(app)

# Relative path for model
model_path = os.path.join('model', 'skin_model.h5')  # Adjust filename
model = None
try:
    model = tf.keras.models.load_model(
        model_path,
        custom_objects={'SparseCategoricalCrossentropy': tf.keras.losses.SparseCategoricalCrossentropy}
    )
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# Routes
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        image = Image.open(request.files['file'].stream)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=-1)
        return jsonify({'prediction': predicted_class.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Render-compatible entry point
if __name__ == '__main__':
    print("Starting Flask app...")
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        image = Image.open(request.files['file'].stream)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=-1)
        return jsonify({'prediction': predicted_class.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=False, port=5500)
