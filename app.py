# Importing essential libraries
from flask import Flask, render_template, request
# To load model
import pickle
# Linear Algebra
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

# Main app
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')  # Renders template

@app.route('/predict', methods=['POST'])      
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])  # Stores Pregnancies
        glucose = int(request.form['glucose'])   # Stores Glucose
        bp = int(request.form['bloodpressure'])  # Stores BloodPressure
        st = int(request.form['skinthickness'])  # Stores Skinthickness
        insulin = int(request.form['insulin'])   # Stores Insulin
        bmi = float(request.form['bmi'])         # Stores BMI
        dpf = float(request.form['dpf'])         # Stores Diabetes Pedigree Function
        age = int(request.form['age'])           # Stores Age
        
	# Stores into numpy array
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
	# Calls classifers' predict method
        my_prediction = classifier.predict(data)
        
	# Renders result template
        return render_template('result.html', prediction=my_prediction)

# Call main app
if __name__ == '__main__':
	app.run(debug=True)