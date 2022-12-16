# DeepL_Final_Project

## Abstract


## Problem Statement
Income data is important for several reasons. On a national scale, it is one of the primary indicators of a nation's economic well being. Census income data also determines the allocation of resources for government-funded programs, such as food distribution and job training programs for following years. Investigating trends in income data can also lead to better understanding of income inequality, and spur the development of mitigation measures. In the United States, an income of 50K a year put an individual at 400% of the federal poverty line and a family of 4 at the 150% mark.

In order to better understand and predict markers of income, we decided to develop a network that will predict whether or not an individual makes above or below 50K a year based on a variety of factors, including location, age, gender and race. We also aim to examine the impact of individual factors on income.

## Related Work

There has been extensive work done on US census income data, ranging from analyzing income distribution to characteristics of integrated health care systems. Every year, the United States Census Bureau releases reports on income, earnings, and poverty data for the previous year. These serve as important research tools for findings such as links between increased state-wide income inequality and increased infant mortality rates (Pabayo et al. 2019), understanding links between income and the spread of diseases like Streptococcus pneumoniae (the most common cause for pneumonia) and how increased income inequality leads to increased spread of drug resistant bacteria (Chen et al. 1998), and how increased income inequality can become a predictor for mental health problems by age 14 (Rivenbark et al. 2019).

In recent years, advanced computational techniques, like machine learning and deep learning, have been applied to census data to create predictive models for urban gentrification using PCA and random forest (Reades et al. 2018), predicting adult obesity (Maharana et al. 2018), and determining healthcase utilization using a decision tree with socioeconomic features (Chen et al. 2020). At the same time, the importance of using unbiased data has also become a concern. With predictions from these models motivating larger scale changes, it has also become a priority to ensure collection and input data is as equitable and fair as possible.

## Dataset

To do this analysis, we used data from the US 1994 census bureau. The data contains 14 different attributes/demograhics for each individual, including age, education, race, occupation and relationship. The data also contains a column specifying total income, whether it is above or below 50K a year (~$98,174 in 2022). This dataset was initially classified by Ronny Kohavi and Barry Becker at UCI.

## Methodology

To develop our initial model, first transformed the output (income level) into one-hot encoding. Then we decided to use a sequential neural network using the keras library. This model took in all 14 attributes, which were also transformed into one-hot encoding, and returned a 1 or 0 depending on whether or not it predicted the income to be above or below 50K respectively. Our network had two RELU layers and one sigmoid layer.

To understand the impacts of different attributes on the model, we then ran several experiments to understand the impact of different attributes on the model's predictions of income. We first identified a threshold number that represented our model predicting an individual would have over 50K of income, where anyone who reached that threshold would be predicted to earn >=50k. This threshold was used in our model's predictions to determine whether or not our model would classify that individual as earning more or less than 50K.

## Experiments/evaluations
We evaluated the results of our model using the keras evaluate function to retrieve the accuracy of the model on a test set. This was done by training the model on 70% of the data, then testing the accuracy on the remaining 30% of the data.

For the experiments, we analyzed each attribute seperately. Specifically, we created datasets with randomized values, then checked the number of people listed as having an income of over 50K with the attribute set to constant. For example, for gender, we randomized all other attributes like race, age, and education, then counted the number of individuals the model predicted as having an income over 50K when they were considered male, vs when they were considered female. To ensure we did not include outliers in our final charts, we ran these experiments several times and found the average of these runs.

## Results

Our model had a 83.9% test accuracy.

The trends we noticed in our data for each attribute are as follows:

* Age
    * The impact of age has a direct relation with income, in that the older one is, the likelier they are to earn >= 50k. Those at age 65 (typical retirement age) were predicted to earn the most. Individuals aged 20 years old (the youngest tested age) were predicted to be the least likely to earn above 50K
    * Overall, the older one is, the more likely they are to earn a higher income

* Education
    * There was a positive correlation between amount of education and income. The two largest jumps were between those with a 9th grade education and those with a high school degree and above, and those with a Doctorate's degree, which has a significantly higher liklihood than the rest. We note that there may be some bias due to there being less information in the original dataset about those with an education lower than 5th grade.
    * Overall, the higher degree of education one has, the more likely they are to earn a higher income

* Gender
    * On average, men were more likely to be predicted to earn more than women, even with randomized characteristics, which makes apparent the gender inequality on income

* Occupation
    * In general, Armed Forces, Professional Specialty and Tech Support had the highest liklihoods of earning >=50k, while a private house servant had the lowest likelihood at 0. We believe this data may have suffered from a similar bias to the age data, where there were many fewer private house servants than occupations like sales, which may have impacted these results.
    * Overall, people with technical/professional jobs are most likely they are to earn a higher income, especially those in Armed Forces, tech, or specialize

* Martial Status
    * The model predicted that married civilian and armed forces spouses were the most likely to earn over 50K. Widows were the least inclined to be predicted to earn above 50K.
    * Overall, spouces are most likely they are to earn a higher income

* Race
    * Generally, white people were the most likely to earn over 50k, followed by Asian/Pacific Islanders. Black people were noticably less likely in comparison, while Amer-Indian-Eskimo had an almost 0 liklihood.
    * Overall, white people and Asian/Pacific Islanders are most likely they are to earn a higher income, while black people are notably less likely, which makes apparent the racial inequality on income

* Relationship
    * Based on the predictions, wives were most likely to earn over 50k, which is surprising considering the model also predicted that men were more likely than women to earn over 50k. Husbands and who are not living with family follow.

* Work class
    * In our model, those who worked in the local government and private businesses were the mostly likely to be predicted to earn above 50K, while those without pay and in state government were the least likely to earn above 50K. We were interested in this, espicially considering changes in the economy since 1994, and were wondering what the distribution might look like with more recent data.

It is noted that our results are limited by the data in the dataset and is missing nuanced aspects of the attributes that could also impact income.


## Examples

* Age
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207785297-cc05a8ad-fb75-4786-9c6e-9ab52b276965.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207785335-619760f4-3ce2-4ae9-ad4b-0debc4d50efa.png)

* Education
   * Single dataset
   *
   ![image](https://user-images.githubusercontent.com/49597852/207786898-e2282d4b-190e-4b98-ace7-6fdd4857c083.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786669-1650abc5-3417-4dd4-8a55-fe797368db01.png)


* Gender
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207786850-b656beae-6ec4-4921-89c7-b10355b6ae54.png)


   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786638-a7712210-09a6-44ab-9459-9055863c24d2.png)


* Employment
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207787675-eab3572f-9681-4102-902f-20e158f3cbb9.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786610-d538ab89-6e7f-405d-9081-4bffd6c6fd85.png)


* Martial Status
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207787703-cd9f6320-5591-496d-a7ce-3d66be936e95.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786559-c50ea8e1-b6d7-4f3a-8376-a6cdcfe9172a.png)


* Race
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207786787-50db6228-9cc6-4b2a-b3e1-cb8cc6bf9f0d.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786502-4ecfba82-ace0-4cfe-bfc8-41d8c461724d.png)


* Relationship
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207786735-a4dadab6-0a13-4f73-8310-7aa828edf0a0.png)


   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786467-dc6584d7-6c2c-4596-9f52-c8fbb535fea8.png)


* Work class
   * Single dataset

   ![image](https://user-images.githubusercontent.com/49597852/207786720-d2771834-9edd-4331-9c43-49a805180efd.png)

   * Average of 10 datasets

   ![image](https://user-images.githubusercontent.com/49597852/207786443-efdfe3e2-4e69-49a8-9b69-1ab5d3d3046b.png)




## File Descriptions
- multilayer_perceptron_network.ipynb: First version of the Jupyter notebook which contains the code used to calculate the model based on the data, had some bugs that needed to be addressed which was done in ver2
- multilayer_perceptron_network_ver2.ipynb: Modification of the first version which addresses the issues
- multilayer_perceptron_network_ver3.ipynb: Added code to visualize predictions of a single randomized dataset
- multilayer_perceptron_network_ver4.ipynb: Added code to visualize predictions of multiple randomized datasets in a single instance + averages

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
- single_plot
    - This folder contains sample plots of predictions for a randomly generated set of data
- multi_plots
    - This folder contains sample plots of predictions for a single run of the multiple randonly generated datasets and their averages

##  Final presentation slides
https://docs.google.com/presentation/d/1GX_dxucB4nZbqpHZgTtSb2tWV4XQmrBGtARi_a1Vtrc/edit?usp=sharing

##  Website
https://among04.wixsite.com/deep-learning-final
