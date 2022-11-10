from flask import Flask,render_template,request,redirect
#
import numpy as np
from tensorflow.keras.models import load_model
#
# from tensorflow.k

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('index1.html')


@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method == "POST":
        string = request.form['val']
        string = string.split(',')
        temp_input = [eval(i) for i in string]
        
        x_input = np.zeros(shape=(1, 10))
        x_input.shape
        
        lst_output = []
        n_steps = 10
        i=0
        while(i<10):
            if(len(temp_input)>10):
                x_input = np.array(temp_input[1:])
                x_input = x_input.reshape(1,-1)
                x_input = x_input.reshape((1,n_steps, 1))
                yhat = model.predict(x_input, verbose = 0)
                temp_input.extend(yhat[0].tolist())
                temp_input = temp_input[1:]
                lst_output.extend(yhat.tolist())
                i=i+1
        
            else:
                x_input = x_input.reshape((1, n_steps,1))
                yhat = model.predict(x_input, verbose = 0)
                temp_input.extend(yhat[0].tolist())
                lst_output.extend(yhat.tolist())
                i=i+1
        val = lst_output[9]
        return render_template('web1.html' , prediction = val)
    if request.method=="GET":
        return render_template('web1.html')

if __name__=="__main__":
    model = load_model('C:/Users/rkara/IBM/Crude_oil.h5')
    app.run(debug=True)