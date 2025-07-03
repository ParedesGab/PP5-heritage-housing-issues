import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
from src.data_management import load_housing_data

# Hard copied from "2-HouseSalesPriceStudy" notebook
vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'OverallQual',
                  'TotalBsmtSF', 'YearBuilt']


def page_house_sales_price_study_body():
    # Load the housing data
    df = load_housing_data()

    st.write("")
    st.write("")
    st.write("### House Sales Price Study")
    st.write("")
    st.success(
        f"This page answers **Business requirement 1:**\n\n"
        f"* The client is interested in understanding the patterns from the "
        f"housing records from Ames, Iowa, so that the client can learn the "
        f"most relevant variables (house attributes) correlated with a "
        f"house sales price.\n\n"
    )

    # Inspect and display the original dataset
    if st.checkbox("Inspect House Records Dataset 🏠🏠🏠"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and "
            f"{df.shape[1]} columns.\n"
            f"* The Table below displays the first 10 rows of the dataset:\n")
        st.write(df.head(10))
        st.write(
            f"* Note that the dataset has missing values (None), to learn "
            f"how they were handled please revise the [Project README file]"
            f"(https://github.com/ParedesGab/PP5-heritage-housing-issues).\n"
            )

    st.write("---")

    # Correlation Study Summary
    st.info(
        f"**CORRELATION STUDY**\n\n"
        f"* Pearson and Spearman correlation studies were conducted to better "
        f"understand how the variables correlate with the target Sales Price.\n"
        f"* The most correlated variables with Sales Price are: "
        f"**{vars_to_study}**\n"
    )
    st.write("")

    # Text based on "2-HouseSalesPriceStudy" notebook:
    # Conclusions" section
    st.success(
        f"**CONCLUSIONS**\n\n"
        f"The correlation analysis indicates that:\n"
        f"* Sale prices are typically higher for homes with larger first-floor "
        f"square footage.\n"
        f"* Sale prices are typically higher for homes with larger garages.\n"
        f"* Sale prices are typically higher for homes with larger above-grade "
        f"living areas.\n"
        f"* Sale prices are typically higher when the overall quality of the "
        f"house's materials and finish improves.\n"
        f"* Sale prices are typically higher for homes with larger "
        f"total basement area.\n"
		f"* Sale prices are typically higher for homes that were recently "
        f"constructed.\n"
    )
    st.write("")
    st.write("")

    # Individual plots per variable
    st.write(
        f"The boxes below display data visualisations of the "
        f"top correlated variables against the sale price.\n"
    )

    # Code copied from "2-HouseSalesPriceStudy" notebook:
    # "EDA on variables to study" section
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Sale Price per Variable"):
        sale_price_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Red: Houses sold at the highest prices.\n"
            f"* Dark Blue: Houses sold at the lowes prices.\n"
            )
        parallel_plot_sale_price(df_eda)


# function created using "2-HouseSalesPriceStudy" notebook code:
# "Step 2: Plot their variable distribution"
def sale_price_per_variable(df_eda):
    target_var = 'SalePrice'
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical_vs_continuous(df_eda, col, target_var)


# Functions copied from "2-HouseSalesPriceStudy" notebook:
# "Step 2: Plot their variable distribution"
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def plot_numerical_vs_continuous(df, col, target_var):
    fig, axes = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x=col, y=target_var, alpha=0.6)
    sns.regplot(data=df, x=col, y=target_var, scatter=False, color='red', line_kws={'linestyle':'--'}) # Adds a regression line
    plt.title(f'{col} vs. {target_var} (Scatter Plot with Regression Line)', fontsize=16)
    plt.xlabel(col, fontsize=12)
    plt.ylabel(target_var, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig) 


# function created using "2-HouseSalesPriceStudy" notebook code - Parallel Plot section
def parallel_plot_sale_price(df_eda):
    fig = px.parallel_coordinates(df_eda, color="SalePrice", dimensions = vars_to_study,
                              color_continuous_scale = 'Jet')
    st.plotly_chart(fig)