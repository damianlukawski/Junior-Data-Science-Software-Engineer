import pandas as pd

import sklearn

def build_features(input_file):
    """Builds features

    Args:
        input_file (str): input file.
    """


    df = pd.read_csv(input_file)

    #change 'male' and 'female' to 0 and 1 for numeric calculations
    df["Sex"] = df["Sex"].replace("male", 0)
    df["Sex"] = df["Sex"].replace("female", 1)


    embarked_dict = {}
    embarked_dict_values = 0
    for i in df.Embarked:
        if i in embarked_dict.keys():
            pass
        else:
            embarked_dict_values = embarked_dict_values + 1
            embarked_dict[i] = embarked_dict_values
    
    for i in embarked_dict.keys():
        df["Embarked"].replace(i, embarked_dict[i], inplace = True)

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1
    output_file = input_file.split('.')[0] + "_bf.csv"
    df.to_csv(output_file)