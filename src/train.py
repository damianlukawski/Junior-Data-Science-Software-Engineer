import numpy as np
import pandas as pd
import sklearn
import pickle as pkl

# Split the data for training.
def train(input_file)
    df = pd.read_csv(input_file, sep = ";")

    y = df["Survived"]

    features = []
    for feature in df.columns:
        if feature == "Survived" or feature == "Embarked":
            pass
        else:
            features.append(feature)

    # Create a classifier and select scoring methods.
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=10)


    # Fit full model and predict on both train and test.
    clf.fit(df[features], y)
    preds = clf.predict(df[features])
    metric_name = "train_accuracy"
    metric_result = sklearn.metrics.accuracy_score(y, preds)

    model_pickle = open("C:\\Users\\Damian\\PycharmProjects\\Roche\\Junior-Data-Science-Software-Engineer\\data\\model.pkl", 'wb')
    pkl.dump(clf, model_pickle)
    model_pickle.close()

    # Return metrics and model.
    info = '%s  for the model is %s' %(metric_name, metric_result)
    print(info)