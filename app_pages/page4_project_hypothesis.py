import streamlit as st


def page_project_hypothesis_body():
    st.write("")
    st.write("")
    
    st.write("### Project Hypothesis and Validation")
    st.write("")
    st.write("")

   # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"**HYPOTHESIS 1**\n\n"
        f"*We hypothesize that a house's dimensional attributes will "
        f"exhibit a significant correlation with its sale price (e.g., larger "
        f"above grade living area (GrLivArea) fetch higher sale prices). "
        f"Consequently, we expect to find strong positive correlations between "
        f"SalePrice and features indicative of house dimensions, such as: "
        f"1stFlrSF, 2ndFlrSF, BsmtFinSF1, BsmtUnfSF, TotalBsmtSF, GrLivArea, "
        f"GarageArea, MasVnrArea, EnclosedPorch, OpenPorchSF, and/or "
        f"WoodDeckSF.*\n\n"
        f"**Conclusion:**\n"
        f"  * Our house sale price correlation study confirmed the hypothesis "
        f"that a property's dimensional attributes significantly correlate "
        f"with its sales price. Indeed, the analysis identified 1stFlrSF, "
        f"GarageArea, GrLivArea, and TotalBsmtSF as the most influential "
        f"variables, exhibiting strong to moderate correlation with SalePrice. "
        f"Importantly, GrLivArea (above-grade living area) showed the highest "
        f"correlation (higher than 0.7), indicating that larger living areas "
        f"tend to fetch higher sale prices.\n"
        )
    
    st.write("")
    st.info(
        f"**HYPOTHESIS 2**\n\n"
        f"*A recent survey showed that recently remodeled houses are "
        f"perceived as more valuable.*\n\n"
        f"**Conclusion:**\n"
        f"  * Our correlation analysis identified YearRemodAdd as being within "
        f"the top 10 variables exhibiting a moderate correlation to SalePrice "
        f"(Pearson coefficient: 0.51, Spearman coefficient: 0.57).\n"
        f"  * Furthermore, feature importance analysis from our "
        f"machine learning pipeline confirmed YearRemodAdd as a significant "
        f"and influential predictor within the model.\n"
        f"  * These combined results collectively suggest that the survey's "
        f"observation about the increased perceived value of remodeled houses "
        f"is likely accurate.\n"
        )
    
    st.write("")
    st.success(
        f"**HYPOTHESIS 3**\n\n"
        f"*We hypothesize that a higher OverallQual rating (indicating "
        f"superior overall material and finish) will directly "
        f"correlate with increased house sale prices.*\n\n"
        f"**Conclusion:**\n"
        f"  * Correlation studies consistently placed OverallQual within the "
        f"top 5 variables for both Pearson and Spearman correlations "
        f"with SalePrice.\n"
        f"  * Furthermore, our machine learning pipeline's feature importance "
        f"analysis identified OverallQual as the most important predictor "
        f"among the model's influential features.\n"
        f"  * Therefore, our hypothesis that a higher OverallQual rating "
        f"directly correlates with increased house sale prices is strongly "
        f"supported by our analysis and the insights derived from "
        f"our machine learning model.\n"
        )
    
    st.success(
        f"Considering the consistent high correlation observed and its top "
        f"ranking in our machine learning model's feature importance analysis, "
        f"**OverallQual** emerges as the most significant feature in "
        f"predicting house sale prices!"
    )
