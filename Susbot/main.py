import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import GradientBoostingRegressor
import json

with open("config.json", 'r') as env:
    environment = json.load(env)
    loc_train = environment['train_data']
    loc_input = environment['input_data']

learning_data = pd.read_csv(loc_train)

input_train = learning_data.drop(columns="CO2 Emissions(g/km)")
output_train = learning_data["CO2 Emissions(g/km)"]

number_columns = input_train.select_dtypes(exclude='object').columns
word_columns = input_train.select_dtypes(include='object').columns

number_feature = Pipeline(
    steps=[(
        'missing',
        SimpleImputer(strategy='median')),
        (
            'scale',
            StandardScaler(with_mean=False)
        )
    ])

words_feature = Pipeline(steps=[('missing',
                                 SimpleImputer(strategy='most_frequent')),
                                ('encode',
                                 OneHotEncoder()),
                                ('scale',
                                 StandardScaler(with_mean=False))])

processing = ColumnTransformer([('number',
                                 number_feature, number_columns),
                                ('word',
                                 words_feature, word_columns)])

SusBot = Pipeline(steps=[('processing',
                          processing),
                         ("pca",
                          TruncatedSVD(n_components=210, random_state=0)),
                         ('model',
                          GradientBoostingRegressor())])

SusBot.fit(input_train, output_train)

print(SusBot.score(input_train, output_train))

input_test = pd.read_csv(loc_input)
result = SusBot.predict(input_test)

print(result)
