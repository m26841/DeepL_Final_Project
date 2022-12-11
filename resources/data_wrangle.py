import pandas as pd
import numpy as np

# this part may need to be changed to address directory issues
df = pd.read_csv("resources/adult.csv")

# focus data on United States
df = df[df["native-country"] != "United-States"]

# convert specified columns into one-hot encoding
workclass = pd.get_dummies(df["workclass"])
education = pd.get_dummies(df["education"])
marital = pd.get_dummies(df["marital-status"])
occupation = pd.get_dummies(df["occupation"])
relationship = pd.get_dummies(df["relationship"])
race = pd.get_dummies(df["race"])
gender = pd.get_dummies(df["gender"])

# merge one-hot encodings back to original
merged = pd.concat([df,workclass,education,marital,occupation,relationship,race,gender],axis='columns')
final = merged.drop(['workclass', 'fnlwgt', 'education', 'educational-num', 'marital-status', 'occupation', 'relationship', 'race', 'gender','native-country'], axis='columns')

# convert output column to binary values
final["income"] = np.where(final["income"] == "<=50K", 0, 1)

# split into input and output
input = final.drop(['income'], axis=1)
output = final['income']
final = pd.concat([input, output], axis='columns')

# export data
pd.DataFrame(final).to_csv("resources/composite.csv", index=False)
pd.DataFrame(input).to_csv("resources/input_ref.csv", index=False)
pd.DataFrame(output).to_csv("resources/output_ref.csv", index=False)
pd.DataFrame(input).to_csv("resources/input.csv", index=False, header=False)
pd.DataFrame(output).to_csv("resources/output.csv", index=False, header=False)