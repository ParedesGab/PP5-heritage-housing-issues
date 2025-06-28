import plotly.express as px
import streamlit as st
from src.data_management import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# hard copied from "2-House Sales Price Study" notebook
vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea',
						'OverallQual', 'TotalBsmtSF', 'YearBuilt']

def page_house_sales_price_study_body():

    # load data
    df = load_housing_data()

    st.write("")
    st.write("")
    st.write("### House Sales Price Study")
    st.write("")
    st.info(f"* The client is interested in understanding the patterns "
            f"from housing records from Ames, Iowa, so that the client " 
            f"can learn the most relevant house attributes that correlate "
            f"to a house sales price.")

    # inspect data
    if st.checkbox("Inspect House Records Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below, please find the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables correlated with a House Sales Price. \n"
        f"* The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "2-House Sales Price Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* Sale prices are typically higher for homes with larger first-floor square footage. \n"
        f"* Sale prices are typically higher for homes with larger garages. \n"
        f"* Sale prices are typically higher for homes with larger above-grade living areas. \n"
        f"* Sale prices are typically higher when the overall quality of the house's materials and finish improves. \n"
        f"* Sale prices are typically higher for homes with larger total basement area. \n"
		f"* Sale prices are typically higher for homes that were recently constructed. \n"
    )

    # Code copied from "2-House Sales Price Study" notebook - "EDA on variables to study" section
	
	# Code from Step 1:
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price per Variable"):
        sale_price_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Red indicates houses sold at the highest prices")
        parallel_plot_sale_price(df_eda)


# function created using "2-House Sales Price Study" notebook code - "Step 2: Plot their variable distribution"
def sale_price_per_variable(df_eda):
    target_var = 'SalePrice'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical_vs_continuous(df_eda, col, target_var)


# Functions copied from "2-House Sales Price Study" notebook - "Step 2: Plot their variable distribution"
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

# function created using "2-House Sales Price Study" notebook code - Parallel Plot section
def parallel_plot_sale_price(df_eda):
    fig = px.parallel_coordinates(df_eda, color="SalePrice", dimensions = vars_to_study,
                              color_continuous_scale = 'Jet')
    st.plotly_chart(fig)