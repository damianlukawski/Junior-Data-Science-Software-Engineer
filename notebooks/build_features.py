import pandas as pd

import sklearn

def build_features(input_file):

    df = pd.read_csv(input_file)

    #change 'male' and 'female' to 0 and 1 for numeric calculations
    df["Sex"] = df["Sex"].replace("male", 0)
    df["Sex"] = df["Sex"].replace("female", 1)



    
    for i in embarked_dict.keys():
        df["Embarked"].replace(i, embarked_dict[i], inplace = True)

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1
    output_file = input_file.split('.')[0] + "_bf.csv"
    df.to_csv(output_file)