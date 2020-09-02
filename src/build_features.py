import pandas as pd

import sklearn

def build_features(input_file):

    df = pd.read_csv(input_file,  sep = ";")

    #change 'male' and 'female' to 0 and 1 for numeric calculations
    #df.replace({'Sex': {"male": 0,"female": 1}} )
    df['Sex']=df["Sex"].replace(["female", "male"], [1,0])





    df['FamilySize'] = df['SibSp'] + df['Parch']+1
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1
    output_file = input_file.split('.')[0] + "_bf.csv"
    df.to_csv(output_file,  sep = ";")



