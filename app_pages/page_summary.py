import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
		f"**Project Terms & Jargon**\n"
		f"* A **house** refers to an individual residential unit in Ames, Iowa.\n"
		f"* A **house attribute** is a characteristic of the house, such as square footage, quality rating, or year built.\n"
		f"* The **Sale Price** is the actual price a property sold for, which our model aims to predict.\n"
		f"* An **inherited property** refers to one of the 4 inherited houses for which the client requires a precise sale price prediction.\n"
        f"**Project Dataset**\n"
		f"* The dataset represents **housing records from Ames, Iowa, indicating house profile**"
		f"* A house profile contains information on individual house attributes (e.g., Floor Area, Basement Finished Area, Garage Area, Garage Finish, Overall Quality, Kitchen Quality, Lot Size, Porch Area, Wood Deck, Year Built, Remodel Date, etc.) and their respective **Sale Prices**.\n"
		f"* The houses in this dataset were constructed **between 1872 and 2010**.\n")
		
    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/churnometer).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding the patterns from the housing records from Ames, Iowa"
        f" so that the client can learn the most relevant variables (i.e., house attributes) that are correlated to a house sales price.\n"
        f"* 2 - The client is interested in predicting the house sale prices from her 4 inherited houses"
        f" so, the client can maximize the sales price for her inherited properties.")
