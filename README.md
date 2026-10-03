# Wine Quality Prediction Web App

This repository contains a simple Flask web application that predicts wine quality from chemical properties entered by the user through a browser form.

The project combines three pieces:

1. A trained machine learning model saved as `model.pkl`
2. A Flask backend in `app.py`
3. A frontend form in `index.html`
 https://wine-quality-prediction-theta.vercel.app/

The overall idea is straightforward: the user enters 11 wine features, the Flask app converts those values into a numeric array, the trained model makes a prediction, and the result is shown back on the page.


## Repository Structure

- `app.py`: Flask application and prediction logic
- `index.html`: user interface for collecting feature values and displaying the prediction
- `model.pkl`: trained machine learning model used for inference

## Project Goal

The purpose of this project is to make a machine learning model usable through a web interface instead of only from a notebook or Python script.

From a developer point of view, this repo turns a saved classification model into a small deployable app.

## Tech Stack

This project uses:

- Python
- Flask
- NumPy
- Pickle
- scikit-learn
- HTML + CSS

## How the App Works

The application flow is:

1. Flask starts the web server.
2. The root route loads the input form.
3. The user enters 11 wine-related values.
4. The form sends those values to the `/predict` route using `POST`.
5. Flask reads the form values from `request.form`.
6. The values are converted from strings to `float`.
7. The values are wrapped into a NumPy-compatible 2D input shape.
8. The pickled model predicts the wine quality class.
9. The prediction is sent back to the same page and displayed to the user.

## Backend Explanation

The backend logic lives in ## Live Demo

### 1. Import dependencies

```python
from flask import Flask, request, render_template
import pickle
import numpy as np
```

Why they are used:

- `Flask`: creates the web app
- `request`: reads submitted form values
- `render_template`: renders the HTML page
- `pickle`: loads the trained model from disk
- `numpy`: formats the input for model prediction

### 2. Create the Flask app

```python
app = Flask(__name__)
```

This initializes the application object that defines routes and runs the server.

### 3. Load the trained model

```python
model = pickle.load(open('model.pkl', 'rb'))
```

This loads the saved machine learning model into memory once, when the application starts.

### 4. Home route

```python
@app.route('/')
def home():
    return render_template('index.html')
```

This route serves the main page containing the input form.

### 5. Prediction route

```python
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = [float(x) for x in request.form.values()]
        final_features = [np.array(input_features)]
        prediction = model.predict(final_features)
        return render_template('index.html', prediction_text=f"Prediction Result: {prediction[0]}")
    except:
        return render_template('index.html', prediction_text="Error: Please enter valid numbers")
```

This is the main inference workflow.

What happens inside it:

1. Read all submitted values from the form.
2. Convert each value into a floating-point number.
3. Put the features into a single row so the model receives the shape it expects.
4. Call `model.predict(...)`.
5. Render the same page again with the prediction result inserted.
6. If conversion fails, show an error message instead of crashing.

### 6. Run the app

```python
if __name__ == "__main__":
    app.run(debug=True)
```

This starts the Flask development server locally.

## Frontend Explanation

The user interface lives in [[index.html](C:\Users\Hp_Ed\OneDrive\Desktop\wine-quality-prediction\index.html).](https://wine-quality-prediction-x1pm.vercel.app/predict)

### What the page contains

- A title: `Wine Quality Predictor`
- A short instruction line
- A form with 11 inputs
- A submit button
- A result section that displays the prediction returned by Flask

### Input Features Collected

The form collects these 11 values:

1. Fixed Acidity
2. Volatile Acidity
3. Citric Acid
4. Residual Sugar
5. Chlorides
6. Free Sulfur Dioxide
7. Total Sulfur Dioxide
8. Density
9. pH
10. Sulphates
11. Alcohol

These align with the features stored in the trained model.

### UI Design Notes

The page uses inline CSS and includes:

- a full-screen gradient background
- a centered glassmorphism-style card
- a two-column input grid
- a styled prediction button
- a colored result section for the returned output

This makes the project more user-friendly than a plain HTML form while keeping the frontend lightweight.

## Model Explanation

The saved model in [model.pkl](C:\Users\Hp_Ed\OneDrive\Desktop\wine-quality-prediction\model.pkl) is:

- `RandomForestClassifier`
- `n_estimators = 100`
- trained for `11` input features
- output classes: `0` and `1`

The model expects these feature names in order:

1. `fixed acidity`
2. `volatile acidity`
3. `citric acid`
4. `residual sugar`
5. `chlorides`
6. `free sulfur dioxide`
7. `total sulfur dioxide`
8. `density`
9. `pH`
10. `sulphates`
11. `alcohol`

From the saved metadata, this is a binary classification model, so the prediction result shown in the app is a class label rather than a continuous quality score.

## End-to-End Workflow

Here is the full workflow as a developer would describe it:

### Phase 1: Model preparation

A machine learning model was trained separately and exported into `model.pkl` using Pickle.

### Phase 2: App startup

When `app.py` starts, Flask initializes the app and loads the trained model into memory.

### Phase 3: User interaction

The user opens the homepage and enters 11 numerical values describing the wine sample.

### Phase 4: Inference

The backend converts those values into the numeric structure expected by the model and generates a prediction.

### Phase 5: Response rendering

Flask sends the prediction back into the HTML template so the result appears on the same page.

## Strengths of This Project

- Clean beginner-friendly Flask structure
- Uses a real trained machine learning model in a web app
- Simple user workflow
- Good separation of roles between model, backend, and UI
- Friendly interface for quick manual testing

## Important Notes and Current Limitations

### 1. Flask template location

The code uses `render_template('index.html')`, which means Flask normally expects the HTML file inside a `templates/` folder.

At the moment, `index.html` is stored in the project root. Unless Flask is configured with a custom template folder, the file should usually be moved to:

```text
templates/index.html
```

### 2. Broad exception handling

The prediction route uses a plain `except:` block. This prevents crashes, which is helpful for beginners, but it also hides the exact error.

A stronger production version would catch specific exceptions and log them.

### 3. No input validation rules in the form

The inputs are currently plain text fields. The app would be more robust with:

- `type="number"`
- `step` values for decimals
- required field validation
- range checks for realistic chemistry values

### 4. Prediction label meaning is not explained in the UI

The model outputs `0` or `1`, but the interface does not explain what those classes mean. It would be better to show a more readable result such as:

- `Good Quality Wine`
- `Not Good Quality Wine`

### 5. Version compatibility warning

When reading `model.pkl`, scikit-learn reports that the model was saved with version `1.6.1` and loaded under version `1.7.2`.

That does not always break the app, but it is worth documenting because pickled scikit-learn models are version-sensitive.

## How to Run the Project

1. Install the required packages:

```bash
pip install flask numpy scikit-learn
```

2. Make sure `model.pkl` is in the same directory as `app.py`.

3. Place `index.html` inside a `templates/` folder if you want Flask's default template loading to work correctly.

Example structure:

```text
wine-quality-prediction/
|-- app.py
|-- model.pkl
|-- templates/
|   |-- index.html
```

4. Start the app:

```bash
python app.py
```

5. Open the local Flask URL in your browser, usually:

```text
http://127.0.0.1:5000/
```

## Skills Demonstrated

This project demonstrates:

- Flask web application development
- HTML form handling
- Machine learning model deployment
- Model loading with Pickle
- NumPy-based input formatting
- Classification prediction workflow
- Frontend and backend integration
- Basic exception handling in a web app

## Future Improvements

If I were continuing this repo as the developer, I would improve it in this order:

1. move `index.html` into `templates/`
2. replace text inputs with numeric inputs and validation
3. map prediction labels `0/1` to human-readable quality messages
4. add a `requirements.txt`
5. show prediction probabilities with `predict_proba()` if useful
6. separate CSS into a static stylesheet
7. add logging and more specific error handling
8. document how the model was trained

## Summary

This repository is a small machine-learning deployment project that wraps a trained `RandomForestClassifier` inside a Flask web app.

The app takes 11 wine chemistry features from the user, sends them to the backend, runs the prediction through the saved model, and displays the result in a simple browser interface. It is a solid beginner project for understanding how a trained model moves from Python code into an interactive web application.
