import pandas as pd
import pickle as pkl
import preprocess
import build_features

#predicting whether someone survived Titanic crash based on recent training
def predict(input_file):
    df = pd.read_csv(input_file, sep = ";")

    y = df["Survived"]

    with open("C:\\Users\\Damian\\PycharmProjects\\Roche\\Junior-Data-Science-Software-Engineer\\data\\model.pkl", 'rb') as model_unpickle:
        model = pkl.load(model_unpickle)


    features = []
    for feature in df.columns:
        if feature == "Survived" or feature == "Embarked":
            pass
        else:
            features.append(feature)
    print(features)
    predictions = model.predict(df[features])
    print(predictions)
    df["prediction"] = predictions
    print(df)


#This part is not ready yet, it is going to estimate the accuracy of our model
'''
# Reassign target (if it was present) and predictions.

df["target"] = target

ok = 0
for i in df.iterrows():
    if (i[1]["target"] == i[1]["prediction"]):
        ok = ok + 1

print("accuracy is", ok / df.shape[0])
'''