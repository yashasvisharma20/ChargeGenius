# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import joblib

# Load the trained regression model (Random Forest in this case)
model = joblib.load('Random_Regression.lb')

# Create a Flask application
app = Flask(__name__)

# Define routes and route handlers
@app.route('/')
def home():
    return render_template('home.html')  # Renders the home page

@app.route('/form')
def form():
    return render_template('form.html')  # Renders the form page for user input

@app.route('/submit_form', methods=['POST'])
def prediction():
    if request.method == "POST":
        try:
            # Extract input features from the submitted form data
            age = float(request.form.get('age', 0))
            bmi = float(request.form.get('bmi', 0))
            child = int(request.form.get('child', 0))
            gender = request.form.get('gender', 'unknown')
            gender_male = 1 if gender == 'Male' else 0
            smoker_yes = int(request.form.get('smoker_yes', 0))
            
            # Extract region information and set corresponding flags
            region_type = request.form.get('region', 'unknown')
            region_northwest, region_southeast, region_southwest = 0, 0, 0
            if region_type == 'northwest':
                region_northwest = 1
            elif region_type == 'southeast':
                region_southeast = 1
            elif region_type == 'southwest':
                region_southwest = 1
            
            # Create an unseen data point based on user input
            UNSEEN_DATA = [[age, bmi, child, gender_male, smoker_yes,
                            region_northwest, region_southeast, region_southwest]]
            
            # Make a prediction using the trained model
            prediction = model.predict(UNSEEN_DATA)[0]
            
            # Render the output page with predicted insurance charges
            return render_template('output.html',
                                   age=age,
                                   bmi=bmi,
                                   child=child,
                                   gender_male=gender_male,
                                   smoker_yes=smoker_yes,
                                   region_northwest=region_northwest,
                                   region_southeast=region_southeast,
                                   region_southwest=region_southwest,
                                   insurance_charges=prediction)
        
        except Exception as e:
            return f"An error occurred: {e}"

# Run the Flask app in debug mode (for development)
if __name__ == "__main__":
    app.run(debug=True)

