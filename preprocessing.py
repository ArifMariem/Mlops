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


# Set path for the input
RAW_DATA_DIR = os.environ["RAW_DATA_DIR"]
train_data_file = 'Iris.csv'
raw_data_path = os.path.join(RAW_DATA_DIR, RAW_DATA_FILE)

# Read dataset
data = pd.read_csv(raw_data_path, sep=",")


#preprocess
df = df.drop('Id', axis=1)
df['Species'] = LabelEncoder().fit_transform(df['Species'])

x = df.drop('Species', axis=1)
y = df['Species']

#split data train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=30)

# Set path to the outputs
PROCESSED_DATA_DIR = os.environ["PROCESSED_DATA_DIR"]
train_path = os.path.join(PROCESSED_DATA_DIR, 'train.csv')
test_path = os.path.join(PROCESSED_DATA_DIR, 'test.csv')

# Save csv
train.to_csv(train_path, index=False)
test.to_csv(test_path,  index=False)