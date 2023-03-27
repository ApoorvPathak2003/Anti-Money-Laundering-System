import numpy as np
import joblib
import streamlit as st

def predict(data):
    best_model = joblib.load("C:\\Users\\apoor\\Desktop\\Internship Work\\Anti-Money Laundering\\lightGBM_model.sav")
    return best_model.predict(data)

def fraud_prediction(steps, amount, original_old_balance, original_new_balance, destination_old_balance, destination_new_balance):

    model_prediction = predict(np.array([[steps, amount, original_old_balance, original_new_balance, destination_old_balance, destination_new_balance]]))

    return model_prediction

def main():
    st.title('Fraud Detection System')

    st.markdown('Input amount, Original Old Balance, Original New Balance, Destination Old Balance, Destination New Balance to predict the fraud transaction', unsafe_allow_html = True)
    st.markdown("Output: 1 means 'FRAUD' ")
    st.markdown("Output: 0 means 'NOT FRAUD'")

    step = st.number_input("Step")
    amount = st.number_input("Amount")
    original_old_balance = st.number_input("Original Old Balance")
    original_new_balance = st.number_input("Original New Balance")
    destination_old_balance = st.number_input("Destination Old Balance")
    destination_new_balance = st.number_input("Destination New Balance")
    result = 1

    predict_button = st.button('Predict')

    if predict_button:
        result = fraud_prediction(step, amount, original_old_balance, original_new_balance, destination_old_balance, destination_new_balance)
        st.write("Output: {}".format(result[0]))

if __name__ == '__main__':
    main()