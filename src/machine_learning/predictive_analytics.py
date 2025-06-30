#import streamlit as st
import pandas as pd
import streamlit as st

def predict_saleprice(X_live, best_features, saleprice_pipeline):

    # from live data, subset features related to this pipeline
    X_live_saleprice = X_live.filter(best_features)

    # predict
    sale_price_prediction = saleprice_pipeline.predict(X_live_saleprice)

    # proba = sale_price_prediction
    # SalePrice = float(proba[0].round(1))
    # amount = '${:,.2f}'.format(SalePrice)

    st.write(sale_price_prediction)
    
    predicted_prices_series = pd.Series(sale_price_prediction, index=X_live.index)
    

    return predicted_prices_series

