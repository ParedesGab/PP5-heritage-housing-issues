import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page1_project_summary import page_summary_body
from app_pages.page2_house_sales_price_study import page_house_sales_price_study_body
from app_pages.page3_house_sale_price_predictor import page_predict_house_sale_price_body
from app_pages.page4_project_hypothesis import page_project_hypothesis_body
from app_pages.page5_technical_overview import page_display_technical_overview


app = MultiPage(app_name= " Heritage Housing Sales Price Prediction 🏠🏠🏠") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("House Sales Price Study", page_house_sales_price_study_body)
app.add_page("Predict House Sale Price", page_predict_house_sale_price_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: House Sales Price", page_display_technical_overview)

# Run the  app
app.run() 