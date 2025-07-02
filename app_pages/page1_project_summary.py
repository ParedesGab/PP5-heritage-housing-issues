import streamlit as st


def page_summary_body():
    st.write("")
    st.write("")
    st.write("### Project Summary")
    st.write("")

    # text based on README file - " Project Terms & Jargon" section
    st.success(
		f"**PROJECT TERMS & JARGON**\n"
		f"* A **house** refers to an individual residential unit in Ames, Iowa.\n"
		f"* A **house attribute** is a characteristic of the house, such as Floor "
    f"Area, Year Built, Kitchen Quality, etc.\n"
		f"* The **Sale Price** is the actual selling price of a house, and our "
    f"model is built to predict this value for houses intended to be sold.\n"
		f"* An **inherited property** refers to one of the 4 inherited houses for "
    f"which the client requires a sale price prediction.\n"
    )
    st.write("")

    # Text based on README file - "Dataset Content" section
    st.info(
    f"**PROJECT DATASET**\n"
		f"* The dataset comprises 1,460 public records of houses sold in Ames, "
    f"Iowa, and constructed between 1872 and 2010.\n"
		f"* The dataset features 24 attributes, each detailing a specific house "
    f"characteristic (e.g., Floor Area, Garage Area, Overall Quality, Year "
    f"Built, Sale Price, etc.).\n"
    )
    st.write("")

    # Text from "Business Requirements" from README but adapted for the app page 
    st.success(
        f"**PROJECT BUSINESS REQUIREMENTS**\n\n"
        f"1 - The client is interested in understanding the patterns from the "
        f"housing records from Ames, Iowa, so that the client can learn the "
        f"most relevant variables (house attributes) correlated with a "
        f"house sales price.\n\n"
        f"2 - The client is interested in predicting the house sale prices "
        f"from her 4 inherited houses, so that the client can maximize the "
        f"sales price for her properties.\n"
    )
    st.write("")

    # Full documentation in README
    st.write(
        f"🔶 For additional information, please revise the "
        f"[Project README file]"
        f"(https://github.com/ParedesGab/PP5-heritage-housing-issues)."
        )
    
