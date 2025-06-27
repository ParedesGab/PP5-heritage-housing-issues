import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_house_sales_price_study import page_house_sales_price_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_sales_price import page_predict_sales_price_body

#from app_pages.page_prospect import page_prospect_body





app = MultiPage(app_name= "Homelytics") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Sales Price Study", page_house_sales_price_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Prospect House Sales Price", page_predict_sales_price_body)

#app.add_page("Prospect Churnometer", page_prospect_body)



app.run() # Run the  app