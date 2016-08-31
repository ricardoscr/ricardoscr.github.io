---
title: "Exploratory Analysis of Several Datasets"
excerpt: "Describes several reports of different exploratory data analysis."
header:
  teaser: montyhall.png
---

This page gathers several exploratory data analysis and their respective reports created using R Markdown.

Currently we describe three main data analysis:

1) Analysis and Modeling of Breast Cancer Data
2) Time Series Analysis of Milk Production
3) Exploratory Analysis of Auto Data

As other explorations became available, this page will be updated.

---

## Analysis and Modeling of Breast Cancer Data

This document is intended to be a concise report to explain a few takeaways of a dataset containing information about breast cancer (available here) obtained at UCI Machine Learning Repository on this link. The analysis was created as part of the Data Science Certificate in the class Methods for Data Analysis at University of Washington.

The idea is to perform an exploratory analysis of the information contained in the dataset, figuring out ways of making the dataset tidier. The ultimate objective is to, in the end, build and compare models to predict if a given tumor is benign or malignant (breast cancer) using the information available on this dataset. Some functions created for this purpose are included in the appendix.

The analysis show that, with a Random Forest model, we can predict if a given tumor is malignant with 97.86% of Accuracy. This result is 1.96% higher than the Accuracy of 95.90% reported in the UCI Machine Learning as the highest for this dataset. We also conclude that the most important information for this prediction is the ‘uniformity of the cell size’.

* Link for the report: <a href="http://rpubs.com/ricardosc/breast-cancer" target='_blank' class="btn btn--info btn--small">Analysis and Modeling of Breast Cancer Data</a>

---

## Time Series Analysis of Milk Production

This document is intended to be a concise report to explain the Time Series analysis performed on a dataset containing information about Milk Production (available here). The analysis was created as part of the Data Science Certificate in the class Methods for Data Analysis at University of Washington.

The idea is to analyze trend and seasonality of the production of Milk from 1995 until 2013, decomposing the time series and analysing the remainder. After that we also intend to create a model to forecast the production of 2014.

The analysis show that the time series is not stationary, as it has a trend, and that after removing trend and season efftects, the remainder of the decomposition is ARMA(1,0). The forecasting for 2014 showed good results with milk production data with confidence intervals reasonably small compared to the means.

* Link for the report: <a href="http://rpubs.com/ricardosc/milk-timeseries" target='_blank' class="btn btn--info btn--small">Time Series Analysis of Milk Production</a>

---

## Exploratory Analysis of Auto Data

This document is intended to be a concise report to explain a few takeaways of a dataset containing information about cars (available here). The analysis was created as part of the Data Science Certificate in the class Methods for Data Analysis at University of Washington.

The idea is to show some findings regarding information related to the price of the cars. Some functions created for this purpose are included in the appendix.

The report starts with data loading/cleaning, followed by the exploratory analysis with three sections with takeaways for price related to weight, make and drive wheel of cars. Finally, some initial basic modeling for exploration is done to close the report.

* Link for the report: <a href="http://rpubs.com/ricardosc/auto-hypothesis-testing" target='_blank' class="btn btn--info btn--small">Hypothesis Testing of Auto Data</a>
* Link for the report: <a href="http://rpubs.com/ricardosc/auto-categorical-variables" target='_blank' class="btn btn--info btn--small">Analysis of Categorical Variables of Auto Data</a>
* Link for the report: <a href="http://rpubs.com/ricardosc/auto-exploration" target='_blank' class="btn btn--info btn--small">Exploratory Analysis of Auto Data</a>

---

