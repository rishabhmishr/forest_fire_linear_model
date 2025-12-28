# Flask: Create the application object
# request: To handle incoming requests
# jsonify: To send JSON responses
# render_template: To render HTML templates

import pickle
from flask import Flask,request,jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

# import the model
model = pickle.load(open('Models/Forest_Fire_Linrear_Regression.pkl', 'rb'))
scalar = pickle.load(open('Models/Forest_Fire_scaler.pkl','rb'))


@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"ERROR in index: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise

@app.route('/predictdata', methods=['POST','GET'])

def predict_datapoint():
    try:
        if request.method == 'POST':
            Classes = float(request.form.get('Classes'))
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Region = float(request.form.get('Region'))

            data = [[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Region,Classes]]
            data_scaled = scalar.transform(data)
            output = model.predict(data_scaled)
            print(f'The predicted area is {output}')

            return render_template('home.html', prediction_text=f'The predicted area is {output[0]:.2f} hectares')
        else:
            return render_template('home.html')    
    except Exception as e:
        print(f"ERROR in predict_datapoint: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True,port=8080)