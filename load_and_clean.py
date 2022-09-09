"""Load the data from the file and clean it"""
__author__ = "Per Starke"

import pandas as pd

# Read data, drop unnecessary columsn and rename from full questions to shorter column names
df = pd.read_csv('data/UmfrageOnline-Beantwortungen-1423358-2022-08-27.csv')

columns_to_drop = ['ID', 'Gestartet am', 'Zuletzt aktualisiert am', 'Collector', 'Sprache', 'IP-Adresse', 'Gerät']
df.drop(columns_to_drop, axis=1, inplace=True)

rename_columns_dict = {'What is your gender?': 'Gender',
                       'What is your age?': 'Age',
                       'What is your main profession?': 'Profession',
                       'Do you deal a lot with computers / IT?': 'IT_expertise',
                       'Would you call the Amper AI "creative"?': 'Amper_creative',
                       'Would you call the DeepBach AI "creative"?': 'DeepBach_creative',
                       'First of all, do you agree with this definition of "creativity"?': 'Creativity_definition_'
                                                                                           'agreement',
                       'After reading the above definition of creativity, would you call the Amper AI "creative"?':
                           'Amper_creative_2',
                       'After reading the above definition of creativity, would you call the DeepBach AI "creative"?':
                           'DeepBach_creative_2'}
df.rename(rename_columns_dict, axis=1, inplace=True)

# Only keep answers where survey has been completed fully
df = df[df.Status == 'Abgeschlossen']
