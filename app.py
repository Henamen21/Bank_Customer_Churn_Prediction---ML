import streamlit as st
import pickle
import numpy as np
import pandas as pd

pickle_in = open("pipeline.pkl" , "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def main():
    st.title("Churn prediction")

    col1, col2 = st.columns(2)

    with col1:
        CreditScore = st.text_input("Credit Score")
        Age = st.text_input("Age")
        Tenure = st.text_input("Tenure")
        NumOfProducts = st.text_input("Number of Products")
        Balance = st.text_input("Balance")
        EstimatedSalary = st.text_input("Estimated Salary")
        SatisfactionScore = st.text_input("Satisfaction Score")
        PointEarned = st.text_input("Points Earned")

    with col2:

        HasCrCard = st.selectbox("Has Card?", options=["Select", "Yes", "No"])
        if HasCrCard == "Yes":
            HasCrCard = 1
        else:
            HasCrCard = 0

        IsActiveMember = st.selectbox("Is Active Member?", options=["Select", "Yes", "No"])
        if IsActiveMember == "Yes":
            IsActiveMember = 1
        else:
            IsActiveMember = 0

        Complain = st.selectbox("Has a Complaint?", options=["Select", "Yes", "No"])
        if Complain == "Yes":
            Complain = 1
        else:
            Complain = 0

        CardType = st.selectbox("Choose Card Type", options=["Select", "PLATINUM", "DIAMOND", "GOLD", "SILVER"])
        Gender = st.selectbox("Choose Gender", options=["Select", "Male", "Female"])
        Geography = st.selectbox("Choose Geography", options=["Select", "France", "Spain", "Germany"])

    data_dict = {
        'CreditScore': [CreditScore],
        'Geography': [Geography],
        'Gender': [Gender],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts], 
        'HasCrCard': [HasCrCard],
        'IsActiveMember': [IsActiveMember],
        'EstimatedSalary': [EstimatedSalary],
        'Complain': [Complain],
        'Satisfaction Score': [SatisfactionScore],
        'Card Type': [CardType],
        'Point Earned': [PointEarned]
    }

    df = pd.DataFrame(data_dict)

    if st.button("predict"):
        # Display the DataFrame for debugging
        st.write("Input Data:")
        st.write(df)
        
        result = classifier.predict(df)

        # Display the result
        if result == 1:
            st.success("Churn: The customer is likely to churn.")
        else:
            st.success("Not Churn: The customer is unlikely to Stay.")


if __name__ == "__main__":
    main()
