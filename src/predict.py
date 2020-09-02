import pandas as pd
import pickle as pkl
import preprocess
import build_features


df = pd.read_csv("C:\\Users\\Damian\\PycharmProjects\\Roche\\Junior-Data-Science-Software-Engineer\\data\\val_preprocessed_bf.csv", sep = ";")

y = df["Survived"]

with open("C:\\Users\\Damian\\PycharmProjects\\Roche\\Junior-Data-Science-Software-Engineer\\data\\model.pkl", 'rb') as model_unpickle:
    model = pkl.load(model_unpickle)


features = []
for feature in df.columns:
    if feature == "Survived" or feature == "Embarked": #or feature == "Unnamed: 0" or feature =="Unnamed: 0.1" :
        pass
    else:
        features.append(feature)
print(features)
predictions = model.predict(df[features])
print(predictions)
df["prediction"] = predictions
print(df)

'''
# Reassign target (if it was present) and predictions.

df["target"] = target

ok = 0
for i in df.iterrows():
    if (i[1]["target"] == i[1]["prediction"]):
        ok = ok + 1

print("accuracy is", ok / df.shape[0])
'''