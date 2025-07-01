import streamlit as st
import pandas as pd
from src.data_management import (
    load_housing_data, 
    load_inherited_housing_data, 
    load_pkl_file
    )
#from src.machine_learning.evaluate_reg import (
# regression_performance, 
# regression_evaluation
#)
from src.machine_learning.predictive_analytics import predict_saleprice


def page_predict_house_sale_price_body():

    # load predict tenure files
    version = 'v1'
    saleprice_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_saleprice/{version}/best_features_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )
    inherited_houses = load_inherited_housing_data()

    st.write("### Interface to Predict House Sale Price")
    st.info(
        f"* This interface answers Business requirement 2"
        f"* The client is interested in predicting the house sale prices from her 4 inherited houses"
        f" so, the client can maximize the sales price for her inherited properties."
    )
    with st.expander("ℹ️ Visualize the 4 inherited Houses attributes"):
        sale_price_inh_houses = predict_saleprice(
        inherited_houses, best_features, saleprice_pipe)

        predicted_price_df = sale_price_inh_houses.to_frame(
        name="Predicted Sale Price")

        best_feat_inh_houses = inherited_houses[best_features]
        merged_display_df = pd.concat([best_feat_inh_houses, predicted_price_df], axis=1)
        st.write(merged_display_df)

    # --- Code for calculating and displaying the sum of predicted prices ---
    st.write("---") 
    st.subheader("Total Predicted Sale Price for Inherited Houses:")

    # Calculate the sum of all predicted sale prices
    total_predicted_price = sale_price_inh_houses.sum()
    st.metric(label="Total Predicted Price for the 4 Inherited Houses:",
               value=f"${total_predicted_price:,.2f}")


    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        price_prediction = predict_saleprice(
        X_live, best_features, saleprice_pipe)
        #st.write(price_prediction)
        st.metric(label="Predicted House Sale Price", value=f"${price_prediction.iloc[0]:,.2f}")


def DrawInputsWidgets():

    # load dataset
    df = load_housing_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 6 features
    col1, col2, col3, col4 = st.columns(4)
    #col5, col6, col7, col8 = st.columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=1,   # Starts at 1
            max_value=10,  # Maximum value is 10
            value=1,       # Initial value displayed is 1
            step=1 
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
        )
    X_live[feature] = st_widget

    with col3:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
        )
    X_live[feature] = st_widget

    return X_live