import pandas as pd
import numpy as np


def preprocess(input_file):
    """
    Deleting useless data: names of passengers, ticket no.
    Deleting cabin no. as there are lots of missing data
    Deleting rows with missing data

    """
    data = pd.read_csv(input_file, sep = ";")
    data = data.dropna()
    del(data["Name"])
    del(data["Ticket"])
    del(data["Cabin"])

    output_file=input_file.split('.')[0]+"_preprocessed.csv"
    data.to_csv(output_file, sep = ";")
