import random as r
import pandas as pd

def random_age_gen():
    return [r.randint(18, 65)]

def random_nominal(size):
    output = [0] * size
    output[r.randint(0, size - 1)] = 1
    return output

def generate_age_data():
    total_data = []
    for i in range(50):
        constant = [0, 0, 40, 0] + \
                   random_nominal(7) + \
                   random_nominal(16) + \
                   random_nominal(7) + [0] + \
                   random_nominal(14) + \
                   random_nominal(6) + \
                   random_nominal(5) + \
                   random_nominal(2)
        for age in range(20, 66, 5):
            data = [age] + constant
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/age.csv", index=False)

def generate_workclass_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0]

        constantB = random_nominal(16) + \
                    random_nominal(7) + [0] + \
                    random_nominal(14) + \
                    random_nominal(6) + \
                    random_nominal(5) + \
                    random_nominal(2)
        for i in range(0, 7):
            onehot = [0] * 7
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/workclass.csv", index=False)

def generate_education_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0] + \
                    random_nominal(7)

        constantB = random_nominal(7) + [0] + \
                    random_nominal(14) + \
                    random_nominal(6) + \
                    random_nominal(5) + \
                    random_nominal(2)
        for i in range(0, 16):
            onehot = [0] * 16
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/education.csv", index=False)

def generate_marital_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0] + \
                    random_nominal(7) + \
                    random_nominal(16)

        constantB = [0] + \
                    random_nominal(14) + \
                    random_nominal(6) + \
                    random_nominal(5) + \
                    random_nominal(2)
        for i in range(0, 7):
            onehot = [0] * 7
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/marital.csv", index=False)

def generate_job_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0] + \
                    random_nominal(7) + \
                    random_nominal(16) + \
                    random_nominal(7) + [0]

        constantB = random_nominal(6) + \
                    random_nominal(5) + \
                    random_nominal(2)
        for i in range(0, 14):
            onehot = [0] * 14
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/job.csv", index=False)

def generate_relationship_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0] + \
                    random_nominal(7) + \
                    random_nominal(16) + \
                    random_nominal(7) + [0] + \
                    random_nominal(14)

        constantB = random_nominal(5) + \
                    random_nominal(2)
        for i in range(0, 6):
            onehot = [0] * 6
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/relationship.csv", index=False)

def generate_race_data():
    total_data = []
    for i in range(50):
        constantA = random_age_gen() + \
                    [0, 0, 40, 0] + \
                    random_nominal(7) + \
                    random_nominal(16) + \
                    random_nominal(7) + [0] + \
                    random_nominal(14) + \
                    random_nominal(6)

        constantB = random_nominal(2)
        for i in range(0, 5):
            onehot = [0] * 5
            onehot[i] = 1
            data = constantA + onehot + constantB
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/race.csv", index=False)

def generate_gender_data():
    total_data = []
    for i in range(50):
        constant = random_age_gen() + \
                   [0, 0, 40, 0] + \
                    random_nominal(7) + \
                    random_nominal(16) + \
                    random_nominal(7) + [0] + \
                    random_nominal(14) + \
                    random_nominal(6) + \
                    random_nominal(5)
        for i in range(0, 2):
            onehot = [0] * 2
            onehot[i] = 1
            data = constant + onehot
            total_data.append(data)
    pd.DataFrame(total_data).to_csv("experiment/gender.csv", index=False)

generate_age_data()
generate_workclass_data()
generate_education_data()
generate_marital_data()
generate_job_data()
generate_relationship_data()
generate_race_data()
generate_gender_data()