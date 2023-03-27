from django.shortcuts import render
from joblib import load
import numpy as np

model = load("C:\\Users\\apoor\\Desktop\\Internship Work\\Anti-Money Laundering\\lightGBM_model.sav")

# Create your views here.
def input_predict(request):

    if request.method == 'POST':
        step = request.POST['step']
        amount = request.POST['amount']
        oldOrigBal = request.POST['oldOrigBal']
        newOrigBal = request.POST['newOrigBal']
        oldDestBal = request.POST['oldDestBal']
        newDestBal = request.POST['newDestBal']

        input_list = np.array([step, amount, oldOrigBal, newOrigBal, oldDestBal, newDestBal], dtype = float)
        
        predict = model.predict([input_list])

        if predict[0] == 1:
            predict = 'Fraud'
        else:
            predict = 'Not Fraud..'

        return render(request, 'main.html', {'predict': predict})
    
    return render(request, 'main.html')
