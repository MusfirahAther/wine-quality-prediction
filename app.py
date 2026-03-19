from flask import Flask, request, render_template
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        input_features = [float(x) for x in request.form.values()]
        
        # Convert into numpy array
        final_features = [np.array(input_features)]
        
        # Make prediction
        prediction = model.predict(final_features)

        # Show result
        return render_template('index.html', prediction_text=f"Prediction Result: {prediction[0]}")
    
    except:
        return render_template('index.html', prediction_text="Error: Please enter valid numbers")

# Run app
if __name__ == "__main__":
    app.run(debug=True)