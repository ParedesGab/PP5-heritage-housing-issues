import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance


def page_display_technical_overview():
    # load House Sales Price pipeline files
    version = 'v1'
    saleprice_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_saleprice/{version}/"
        f"best_features_regressor_pipeline.pkl")
		
    saleprice_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_saleprice/{version}/"
        f"features_importance.png")
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
        f"* A Regressor model was used to predict house sale prices in "
        f"Ames, Iowa.\n"
        f"* The regressor performance met the client's requirement of an: "
        f"R2 score of **at least 0.75 on both, the train and test set.**\n"
        f"* Namely, the regressor performance metric was for:\n "
        f"  * Train set -  R2 Score: 0.959 \n"
        f"  * Test set - R2 score: 0.778 \n"
        )
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline: Ames, Iowa House Price Prediction.")
    st.write(saleprice_pipe)
    st.write("---")

    # show best features
    st.write("### Feature Importance: What Drives House Prices?")
    st.write("Our analysis shows that we didn't need every feature from" \
    " the Housing Prices Dataset to train an effective model. Instead, we " \
    "identified the most influential features that truly impact sale prices. " \
    "The model was trained on these key features, and their importance "
    "is as follows:")
    st.write(X_train.columns.to_list())
    st.image(saleprice_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance - Model Evaluation")
    st.write("")
    regression_performance(X_train, y_train, X_test, y_test, saleprice_pipe)