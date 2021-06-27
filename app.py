import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle

 

app = Flask(__name__) #Initialize the flask App


model = pickle.load(open('sathish.pkl', 'rb'))
scaler = MinMaxScaler()

@app.route('/')
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/abstract')
def abstract():
	return render_template('abstract.html')

@app.route('/future')
def future():
	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/test.html', methods = ['GET', 'POST'])
def single():
    return render_template('test.html')


#@app.route('/upload')
#def upload_file():
#   return render_template('BatchPredict.html')



@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	print(int_feature)
	int_feature = [float(i) for i in int_feature]
	final_features = [np.array(int_feature)]
	prediction = model.predict(final_features)

	output = prediction
	print(output)
	return render_template('test.html', prediction_text= output)
@app.route('/chart/')
@app.route('/chart/<prediction_text>')
def hello(prediction_text):
	return render_template('chart.html', prediction=prediction_text)
@app.route('/existing')
def existing():
	return render_template('existing.html')    
    
    
if __name__ == "__main__":
    app.run(debug=False)
