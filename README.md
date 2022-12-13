# DeepL_Final_Project

## Abstract


## Problem Statement
Income data is important for several reasons. On a national scale, it is one of the primary indicators of a nation's economic well being. Census income data also determines the allocation of resources for government-funded programs, such as food distribution and job training programs for following years. Investigating trends in income data can also lead to better understanding of income inequality, and spur the development of mitigation measures. In the United States, an income of 50K a year put an individual at 400% of the federal poverty line and a family of 4 at the 150% mark.

In order to better understand and predict markers of income, we decided to develop a network that will predict whether or not an individual makes above or below 50K a year based on a variety of factors, including location, age, gender and race. We also aim to examine the impact of individual factors on income.

## Related Work

There has been extensive work done on US census income data, ranging from analyzing income distribution to characteristics of integrated health care systems. Every year, the United States Census Bureau releases reports on income, earnings, and poverty data for the previous year. These serve as important research tools for findings such as links between increased state-wide income inequality and increased infant mortality rates (Pabayo et al. 2019), understanding links between income and the spread of diseases like Streptococcus pneumoniae (the most common cause for pneumonia) and how increased income inequality leads to increased spread of drug resistant bacteria (Chen et al. 1998), and how increased income inequality can become a predictor for mental health problems by age 14 (Rivenbark et al. 2019).

In recent years, advanced computational techniques, like machine learning and deep learning, have been applied to census data to create predictive models for urban gentrification using PCA and random forest (Reades et al. 2018), predicting adult obesity (Maharana et al. 2018), and determining healthcase utilization using a decision tree with socioeconomic features (Chen et al. 2020). At the same time, the importance of using unbiased data has also become a concern. With predictions from these models motivating larger scale changes, it has also become a priority to ensure collection and input data is as equitable and fair as possible.

## Methodology
To do this analysis, we used data from the US 1994 census bureau. The data contains 14 different attributes/demograhics for each individual, including age, education, race, occupation and relationship. The data also contains a column specifying total income, whether it is above or below 50K a year. This dataset was initially classified by Ronny Kohavi and Barry Becker at UCI.

To develop our initial model, first transformed the output (income level) into one-hot encoding. Then we decided to use a sequential neural network using the keras library. This model took in all 14 attributes and returned a 1 or 0 depending on whether or not it predicted the income to be above or below 50K respectively. Our network had two RELU layers and one sigmoid layer.
To understand the impacts of different attributes on the model, we then ran several experiments to check the accuracy of the model with the different input parameters.

## Experiments/evaluations
We evaluated our results using the keras evaluate function to retrieve the accuracy of the model on a test set.



## Results

Our initial model had an 84% train accuracy

## File Descriptions
- multilayer_perceptron_network_ver2.ipynb: The Jupyter notebook which contains the code used to calculate the model based on the data
- multilayer_perceptron_network.ipynb: Older version of the Jupyter notebook which contains the code used to calculate the model based on the data, had some bugs that needed to be addressed which was done in ver2
- resources
    - data_wrangle.py: Converts the raw data to a usable format for the network (i.e. converting nominal data to one-hot encoding) and outputs to a new csv
    - data_generator.py: Generates randomized sets of data to use in experimentation
    - adult.csv: The original data, sourced from https://www.kaggle.com/code/jieyima/income-classification-model/data
    - input.csv: Wrangled input data (excluding income column)
    - output.csv: Wrangled output data (income column)
    - input_ref.csv: input.csv with column headers
    - output_ref.csv: output.csv with column header
    - composite.csv: Combined input.csv and output.csv dataset, used for the model
- experiment
    - This folder contains randomly-generated csvs of data that are used in the experimentation section
