import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_housing_data, load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance, regression_evaluation_plots


def page_predict_sales_price_body():

    # load House Sales Price pipeline files
	
    version = 'v1'
    saleprice_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_saleprice/{version}/best_features_regressor_pipeline.pkl")
		
    saleprice_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_saleprice/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_saleprice/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_saleprice/{version}/y_test.csv")
    
    st.write("")
    st.write("")
    st.write("### ML Pipeline: Predict House Sale Price")
    st.write("")
    # display pipeline training summary conclusions
    st.success(
        f"* A Regressor model was used to predict house sale prices in Ames, Iowa.\n"
        f"* The regressor performance met the client requirement: "
        f" an R2 score of **at least 0.75 on both, the train and test set.**\n"
        f"* The regressor performance metric was CHANGE on both sets.\n")
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline: Ames, Iowa House Price Prediction.")
    st.write(saleprice_pipe)
    st.write("---")

    # show best features
    st.write("### The features the model was trained on, and their importance.")
    st.write(X_train.columns.to_list())
    st.image(saleprice_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance - Model Evaluation")
    st.write("")
    regression_performance(X_train, y_train, X_test, y_test, saleprice_pipe)
    