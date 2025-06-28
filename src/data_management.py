import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_housing_data():
    df = pd.read_csv("outputs/datasets/collection/house_prices_after_inspection.csv")
    return df

@st.cache_data
def load_inherited_housing_data():
    df = pd.read_csv("input/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df 


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)