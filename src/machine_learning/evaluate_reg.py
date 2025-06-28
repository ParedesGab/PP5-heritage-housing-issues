import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# Functions code copied from "5-Predict Sales Price" notebook

def regression_performance(X_train, y_train, X_test, y_test, pipeline):

    st.write('#### Model Evaluation')
    st.write('#### Train Set')
    regression_evaluation(X_train, y_train, pipeline)
    st.write('#### Test Set')
    regression_evaluation(X_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):

    prediction = pipeline.predict(X)
    st.write(f"**R2 Score:** {r2_score(y, prediction):.3f}")
    st.write(f"**Mean Absolute Error:** {mean_absolute_error(y, prediction):.3f}")
    st.write(f"**Mean Squared Error:** {mean_squared_error(y, prediction):.3f}")
    st.write(f"**Root Mean Squared Error:** {np.sqrt(mean_squared_error(y, prediction)):.3f}")
	
	#st.metric(label="R2 Score", value=f"{r2:.3f}")
	#st.metric(label="Mean Absolute Error", value=f"{mae:.3f}")
	#st.metric(label="Mean Squared Error", value=f"{mse:.3f}")
	#st.metric(label="Root Mean Squared Error", value=f"{rmse:.3f}")


def regression_evaluation_plots(X_train, y_train, X_test, y_test, pipeline, alpha_scatter=0.5):
    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    sns.scatterplot(x=y_train, y=pred_train, alpha=alpha_scatter, ax=axes[0])
    sns.lineplot(x=y_train, y=y_train, color='red', ax=axes[0])
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predictions")
    axes[0].set_title("Train Set")

    sns.scatterplot(x=y_test, y=pred_test, alpha=alpha_scatter, ax=axes[1])
    sns.lineplot(x=y_test, y=y_test, color='red', ax=axes[1])
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predictions")
    axes[1].set_title("Test Set")

    st.pyplot(fig)