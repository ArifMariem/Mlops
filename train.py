import os
import pandas as pd
import numpy as np
from joblib import dump
import pickle
from sklearn.model_selection import StratifiedKFold, cross_val_score


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


# Set path to inputs
PROCESSED_DATA_DIR = os.environ["PROCESSED_DATA_DIR"]
train_data_file = 'train.csv'
train_data_path = os.path.join(PROCESSED_DATA_DIR, train_data_file)


#read data
df = pd.read_csv(train_data_path, sep=",")


#model
model = LogisticRegression()
model=model.fit(x_train, y_train)



# Cross validation
cv = StratifiedKFold(n_splits=3) 
val_logit = cross_val_score(model, x_train, y_train, cv=cv).mean()

# Validation accuracy to JSON
train_metadata = {
    'validation_acc': val_logit
}

#serialize and save model 
dump(logit_model, model_path)


# Set path to output (metadata)
RESULTS_DIR = os.environ["RESULTS_DIR"]
train_results_file = 'train_metadata.json'
results_path = os.path.join(RESULTS_DIR, train_results_file)

# Serialize and save metadata
with open(results_path, 'w') as outfile:
    json.dump(train_metadata, outfile)