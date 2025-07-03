# The Heritage Housing project 🏠🏠🏠

(Developer: Gabriela Fabiola Paredes Rojas)

![Mockup image](documentation/website-screenshots/1-mockup.png)

**Welcome to the Heritage Housing Issues App!**

This project proposes an Machine Learning-powered solution that
will analyze housing records from Ames, Iowa, to uncover crucial correlations
through data visualization and a predictive regression model in this region.

    🔸 Discover which house attributes most significantly influence Sale Prices!

    🔸 Discover the total value of your 4 inherited houses!

    🔸 Predict the value of any other house in the Ames area!

Are you ready to maximize the sales price of your properties?

Let's go! 🚀

+ The live page can be accessed via this [Render link.](https://pp5-heritage-housing-issues-gp.onrender.com/)

---

## Dataset Content

+ The dataset is sourced from Kaggle, and comprises 1,460 public records of houses sold in Ames, Iowa, constructed between 1872 and 2010.
+ The dataset features 24 attributes, each detailing a specific house characteristic.
+ From these, 20 are numeric and 4 are categorical (objects).
+ For dataset details, please see the table below:

|Variable|Meaning|Units|Data Type|
|:----|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|integer|
|2ndFlrSF|Second-floor square feet|0 - 2065|float|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|float|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|object|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|object|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|integer|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|integer|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|integer|
|GarageArea|Size of garage in square feet|0 - 1418|integer|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|object|
|GarageYrBlt|Year garage was built|1900 - 2010|float|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|integer|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|object|
|LotArea| Lot size in square feet|1300 - 215245|integer|
|LotFrontage| Linear feet of street connected to property|21 - 313|float|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|float|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|float|
|OpenPorchSF|Open porch area in square feet|0 - 547|integer|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|integer|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|integer|
|WoodDeckSF|Wood deck area in square feet|0 - 736|float|
|YearBuilt|Original construction date|1872 - 2010|integer|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|integer|
|SalePrice|Sale Price|34900 - 755000|integer|

---

## Project Terms & Jargon

+ A **house** refers to an individual residential unit in Ames, Iowa.
+ A **house attribute** is a characteristic of the house, such as Floor Area, Year Built or Kitchen Quality.
+ The **SalePrice** is the actual selling price of a property, and our model is built to predict this target value for houses intended to be sold.
  + Throughout this README, a house selling price will be referred to as the target attribute SalePrice.
+ An **inherited property** refers to one of the 4 inherited houses for which the client requires a SalePrice prediction.

---

## Business Requirements

A dear friend has inherited properties in Ames, Iowa, and has turned to you for assistance
in achieving the best possible SalePrices. She's a savvy real estate observer in her own area,
but she's keenly aware that what makes a home valuable there might be entirely different in Ames.

To guide your efforts, she has provided you with a public dataset detailing house prices in that specific Iowa market,
and has the two following business requirements:

    1 - The client is interested in discovering how the house attributes correlate with the SalePrice.
	Therefore, the client expects data visualisations of the correlated variables against the SalePrice to show that.

    2 - The client is interested in predicting the house SalePrice from her four inherited houses.

---

## Hypothesis and how to validate?

+ **HYPOTHESIS 1:** We hypothesize that a property's size is a key driver of its SalePrice, with larger homes generally fetching higher SalePrices.
Consequently, we expect to find strong positive correlations between SalePrice and features indicative of house dimensions, 
such as 1stFlrSF, 2ndFlrSF, BsmtFinSF1, BsmtUnfSF, TotalBsmtSF, GrLivArea, GarageArea, MasVnrArea, EnclosedPorch, OpenPorchSF, and/or WoodDeckSF.

  + A Correlation study can help in this investigation

+ **HYPOTHESIS 2:** A recent survey showed that recently remodeled houses are perceived as more valuable.

  + A Correlation study can help in this investigation.
  + Moreover, machine learning pipeline's feature importance analysis can confirm if YearRemodAdd (remodel date) is identified as a significant predictor among the model's most influential features.

+ **HYPOTHESIS 3:** We hypothesize that a higher OverallQual rating (indicating superior overall material and finish) will directly correlate with increased house SalePrices.

  + A Correlation study can help in this investigation.
  + Moreover, machine learning pipeline's feature importance analysis can confirm if the attribute **OverallQual**
	  is identified as a significant predictor among the model's most influential features.

---

## The rationale to map the business requirements to the Data Visualisations and ML tasks

+ **Business Requirement 1:** Data Visualization and Correlation study

  + We will inspect the house records dataset.
  + We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to SalePrice.
  + We will plot the main variables against SalePrice to visualize insights.

+ **Business Requirement 2:** Regression and Data Analysis

  + We want to predict the SalePrice of a house from Ames, Iowa.
  + Given that it will be a continuous numerical value, we want to build a regression model.

---

## ML Business Case

### Predict SalePrice (SalePrice)

#### Regression Model

+ We want an ML model to predict a house SalePrice in Ames, Iowa.
+ Given that the target variable is a continous value, we consider a **regression model**, which is supervised and uni-dimensional.
+ Our ideal outcome is to provide our client with reliable insights for accurately predicting property SalePrices,
enabling them to optimize sales strategies and maximize value for houses they intend to sell.
+ The model success metrics are:
  + At least 0.75 for R2 score, on both, the train and test set.

+ The ML model is considered a failure if:
  + After 6 months of usage, the model's overall explanatory power significantly degrades. For example, if the R-squared
		(R2) score on newly acquired, unseen data consistently falls below 0.60.
		This indicates that the model is explaining less than 60% of the variance in actual SalePrices,
		which is a substantial drop from the agreed-upon performance goal of 0.75.
		
+ The output is defined as a continuous value for SalePrice in dollars. It is assumed that this model will predict a property SalePrice.
+ The client will gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
+ Heuristics: Currently, there is no established approach to predict house SalePrices in Ames, Iowa.
+ The training data to fit the model comes from the Ames, Iowa housing dataset. This dataset contains about 1.5 thousand house records.
  + Train data - target: SalePrice; features: all other variables, but EnclosedPorch and WoodDeckSF (dropped because they had >80% of missing values).

---

## Dashboard Design (Streamlit App User Interface)

+ Pages style: To enhance visual engagement and break monotony, an alternating green and blue color scheme has been applied to informational text blocks (utilizing st.success and st.info,). This color style is maintained consistently across all application pages.

### Page 1: Project summary

![Dashboard Page 1](documentation/screenshots/page1.png)

+ Project summary
+ Project Terms & Jargon
+ Describe Project Dataset
+ State Business Requirements
+ Link to ReadMe file in case User wants to see the full documentation

### Page 2: House Sales Price Study

![Dashboard Page 2](documentation/screenshots/page2.png)

+ This page answers business requirement 1, but we couldn't know in advance which plots would need to be displayed.
+ Thus, after data analysis, we agreed with stakeholders that the page will:

  + State the page’s title.
  + State **business requirement 1**.
  + Include a **checkbox** allowing users to inspect the House Records Dataset . Toggling this option will:

    + Display the dataset’s dimensions (number of rows and columns in the data).
    + Display the first ten rows of the dataset.
    + Display a note below the table, informing the user about the presence of missing values and direct them to revisit this section for details on how they were handled.

  + Contain  an introduction to the **Correlation Study** that displays the most correlated variables to SalePrice.
  + Contain a summary of its **conclusions**.
  + Include a checkbox to display individual scatter plots, visualizing SalePrice levels against each of the most correlated variables. Scatter plots were selected as the appropriate visualization method because SalePrice and all identified 'most correlated variables' (1stFlrSF, GarageArea, GrLivArea, TotalBsmtSF, YearRemodAdd) can be considered continuous numerical variables, making them the most informative choice for illustrating these relationships (Figures below – Scatter Plots).
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)
![ScatterPlot SalePrice vs ](documentation/screenshots/scatterplot_saleprice_vs_.png)

+ Include a Parallel coordinates plot featuring SalePrice and its correlated variables. This visualization offers a holistic understanding of how these key variables interact with SalePrice (Figure below – Parallel plot).
![Parallel plot](documentation/screenshots/parallelplot.png)

> [!NOTE]
> While not displayed on this page, it's important to note that missing values in the dataset were handled prior to conducting the correlation analysis.
>
> For **categorical variables (Objects)**: Missing entries were imputed with the label 'Missing', and this new 'Missing' category was included in subsequent evaluations.
>
> For **Numerical variables (Floats and Integers):** Given their non-normal distributions, missing values were imputed using the median of each respective variable."

### Page 3: House SalePrice Predictor

![Dashboard Page 3](documentation/screenshots/page3.png)

+ This page answers business requirement 2.
+ After creating and evaluating the ML model, we agreed with stakeholders that the page will:

  + State the page’s title.
  + State **business requirement 2**.
  + Include a collapsible box (st.expander) showcasing the most influential attributes (OverallQual, GarageArea, TotalBsmtSF, and YearRemodAdd) for the client's inherited houses, alongside their predicted SalePrices. These attributes were specifically identified by the machine learning regression model as the most impactful features (best features) for price prediction.

  + Contain a section that shows the summed predicted value (in dollars) of the four inherited properties.
  + Include a section enabling users to predict themselves the SalePrice for any house in Ames, Iowa. The prediction widgets correspond to the most influential features (OverallQual, GarageArea, TotalBsmtSF, and YearRemodAdd) identified by the machine learning model for predicting prospective SalePrice.
  + Include a "Run predictive analysis" button (st.button) that processes the users’ input through our ML pipeline and predicts the house SalePrice (in dollars).

### Page 4: Project Hypothesis and Validation

![Dashboard Page 4](documentation/screenshots/page4.png)

+ Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
  
HYPOTHESIS 1

+ We hypothesize that a property's size is a key driver of its sale with larger homes generally fetching higher SalePrices.
  + Correct: Our house SalePrice correlation study confirms the hypothesis that larger homes generally fetch higher prices and indicated that the variables (house attributes) 1stFlrSF, GarageArea, GrLivArea, and TotalBsmtSF are the most influential variables in their correlation with SalePrice.

HYPOTHESIS 2

+ A recent survey showed that recently remodeled houses are perceived as more valuable.
  + Correct: Correlation analysis placed YearRemodAdd within the top 10 variables for both Pearson and Spearman correlations with SalePrice. Interestingly, however, YearBuilt exhibited a stronger individual correlation. Nonetheless, the subsequent feature importance analysis from our machine learning pipeline confirmed YearRemodAdd as a significant and influential predictor within the model. These combined results collectively suggest that the survey's observation about the increased perceived value of remodeled houses is likely accurate.

HYPOTHESIS 3

+ We hypothesize that a higher OverallQual rating (indicating superior overall material and finish) will directly correlate with increased house SalePrices.
  + Correct: Correlation studies consistently placed OverallQual within the top 5 variables for both Pearson and Spearman correlations with SalePrice. Furthermore, our machine learning pipeline's feature importance analysis identified OverallQual as the most important predictor among the model's influential features. Therefore, our hypothesis that a higher OverallQual rating directly correlates with increased house SalePrices is strongly supported by our analysis and the insights derived from our machine learning model.

### Page 5: Predict SalePrice

![Dashboard Page 5](documentation/screenshots/page5.png)

+ Considerations and conclusions after the pipeline is trained
+ Present ML pipeline steps
+ Feature importance
+ Pipeline performance

---

## Unfixed Bugs


---

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

