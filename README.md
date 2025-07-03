# The Heritage Housing project 🏠🏠🏠

(Developer: Gabriela Fabiola Paredes Rojas)

![Mockup image](documentation/website-screenshots/1-mockup.png)

**Welcome to the Heritage Housing Issues App!**

This project proposes an Machine Learning-powered solution that
will analyze housing records from Ames, Iowa, to uncover crucial correlations
through data visualization and a predictive regression model in this region.

    🔸 Discover which house attributes most significantly influence sale prices!

    🔸 Visualize the total value of your 4 inherited houses!

    🔸 Predict the value of any other house in the Ames area!

Are you ready to maximize the sales price of your properties?

Let's go! 🚀

+ The live page can be accessed via this [Heroku link.](https://my-finances-tracker-5a1726e2723f.herokuapp.com/)

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
+ The **Sale Price** is the actual selling price of a property, and our model is built to predict this value for houses intended to be sold.
+ An **inherited property** refers to one of the 4 inherited houses for which the client requires a sale price prediction.

---

## Business Requirements

A dear friend has inherited properties in Ames, Iowa, and has turned to you for assistance
in achieving the best possible sale prices. She's a savvy real estate observer in her own area,
but she's keenly aware that what makes a home valuable there might be entirely different in Ames.

To guide your efforts, she has provided you with a public dataset detailing house prices in that specific Iowa market,
and has the two following business requirements:

    1 - The client is interested in discovering how the house attributes correlate with the sale price.
	Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

    2 - The client is interested in predicting the house sale price from her four inherited houses.

---

## Hypothesis and how to validate?

+ **HYPOTHESIS 1:** We hypothesize that a property's size is a key driver of its sale price, with larger homes generally fetching higher sale prices.
Consequently, we expect to find strong positive correlations between SalePrice and features indicative of house dimensions, 
such as 1stFlrSF, 2ndFlrSF, BsmtFinSF1, BsmtUnfSF, TotalBsmtSF, GrLivArea, GarageArea, MasVnrArea, EnclosedPorch, OpenPorchSF, and/or WoodDeckSF.

  + A Correlation study can help in this investigation

+ **HYPOTHESIS 2:** A recent survey showed that recently remodeled houses are perceived as more valuable.

  + A Correlation study can help in this investigation.
  + Moreover, machine learning pipeline's feature importance analysis can confirm if YearRemodAdd (remodel date) is identified as a significant predictor among the model's most influential features.

+ **HYPOTHESIS 3:** We hypothesize that a higher OverallQual rating (indicating superior overall material and finish) will directly correlate with increased house sale prices.

  + A Correlation study can help in this investigation.
  + Moreover, machine learning pipeline's feature importance analysis can confirm if the attribute **OverallQual**
	  is identified as a significant predictor among the model's most influential features.

---

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

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

