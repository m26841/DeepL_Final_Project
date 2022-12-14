# DeepL_Final_Project

## Abstract


## Problem Statement
Income data is important for several reasons. On a national scale, it is one of the primary indicators of a nation's economic well being. Census income data also determines the allocation of resources for government-funded programs, such as food distribution and job training programs for following years. Investigating trends in income data can also lead to better understanding of income inequality, and spur the development of mitigation measures. In the United States, an income of 50K a year put an individual at 400% of the federal poverty line and a family of 4 at the 150% mark.

In order to better understand and predict markers of income, we decided to develop a network that will predict whether or not an individual makes above or below 50K a year based on a variety of factors, including location, age, gender and race. We also aim to examine the impact of individual factors on income.

## Related Work

There has been extensive work done on US census income data, ranging from analyzing income distribution to characteristics of integrated health care systems. Every year, the United States Census Bureau releases reports on income, earnings, and poverty data for the previous year. These serve as important research tools for findings such as links between increased state-wide income inequality and increased infant mortality rates (Pabayo et al. 2019), understanding links between income and the spread of diseases like Streptococcus pneumoniae (the most common cause for pneumonia) and how increased income inequality leads to increased spread of drug resistant bacteria (Chen et al. 1998), and how increased income inequality can become a predictor for mental health problems by age 14 (Rivenbark et al. 2019).

In recent years, advanced computational techniques, like machine learning and deep learning, have been applied to census data to create predictive models for urban gentrification using PCA and random forest (Reades et al. 2018), predicting adult obesity (Maharana et al. 2018), and determining healthcase utilization using a decision tree with socioeconomic features (Chen et al. 2020). At the same time, the importance of using unbiased data has also become a concern. With predictions from these models motivating larger scale changes, it has also become a priority to ensure collection and input data is as equitable and fair as possible.

To do this analysis, we used data from the US 1994 census bureau. The data contains 14 different attributes/demograhics for each individual, including age, education, race, occupation and relationship. The data also contains a column specifying total income, whether it is above or below 50K a year. This dataset was initially classified by Ronny Kohavi and Barry Becker at UCI.


## Methodology

To develop our initial model, first transformed the output (income level) into one-hot encoding. Then we decided to use a sequential neural network using the keras library. This model took in all 14 attributes and returned a 1 or 0 depending on whether or not it predicted the income to be above or below 50K respectively. Our network had two RELU layers and one sigmoid layer.

To understand the impacts of different attributes on the model, we then ran several experiments to understand the impact of different attributes on the model's predictions of income. We first identified a threshold number that represented our model predicting an individual would have over 50K of income. This threshold was used in our model's predictions to determine whether or not our model would classify that individual as earning more or less than 50K. 

## Experiments/evaluations
We evaluated the results of our initial model using the keras evaluate function to retrieve the accuracy of the model on a test set. This was done by training the model on 70% of the data, then testing the accuracy on the remaining 30% of the data.

For the experiments, we analyzed each attribute seperately. Specifically, we created datasets with randomized values, then checked the number of people listed as having an income of over 50K with the attribute set to constant. For example, for gender, we randomized all attributes like race, age, and education, then counted the number of individuals the model predicted as having an income over 50K when they were considered male, vs when they were considered female. To ensure we did not include outliers in our final charts, we ran these experiments several times and found the average of these runs.




## Results

Our initial model had an 84% test accuracy.

The trends we noticed in our data for each attribute are as follows:

* Age
    * The impact of age appeared to be similar to a bell-curve, where people between the ages 45 and 55 were the most likely to earn above 50K and individuals younger or older than were less likely to earn above 50K. Those at age 65 (the oldest age in the dataset) were predicted to earn over 50K as often as those at around age 35. Individuals aged 20 years old were predicted to be the least likely to earn above 50K
    
* Education
    * There was a positive correlation between amount of education and income. The two largest jumps were between those with a 9th grade education and those with a high school degree and above, and those with a Doctorate's degree. We note that there may be some bias due to there being less information in the original dataset about those with an education lower than 5th grade.
    
* Gender
    * On average, men were more likely to be predicted to earn more than women, even with randomized characteristics
    
* Occupation
    * In general, a specialty profession had the highest likelihood of being predicted to earn over 50K while a private house servant had the lowest likelihood. We believe this data may have suffered from a similar bias to the age data, where there were many fewer private house servants than occupations like sales, which may have impacted these results.

* Martial Status
    * The model predicted that married civilian spouses were the most likely to earn over 50K, followed closely by married spouses in the armed forces. Those who lived seperately, or had never been married were the least inclined to be predicted to earn above 50K. We believe this may be a result of a joint income being shared.

* Race
    * [TODO]

* Relationship
    * [TODO]
    
* Work class 
    * In our model, those who worked in the government, specifically federal and local, were the mostly likely to be predicted to earn above 50K, while those without pay were the least likely to earn above 50K. We were interested in this, espicially considering changes in the economy since 1994, and were wondering what the distribution might look like with more recent data. 

It is noted that our results are limited by the data in the dataset and is missing nuanced aspects of the attributes that could also impact income. 

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
