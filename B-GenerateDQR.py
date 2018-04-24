import pandas
import plotly
import plotly.graph_objs as go
import csv
import numpy
import os

# Import custom functions.
from library import *

# Create directory for Virsualisations (html files).
if not os.path.exists('Visualisations'):
    os.makedirs('Visualisations')

# TODO : Try to determine programmatically if continous or categorical.
continuous_names = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categorical_names = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex',
                     'native-country', 'target']
# Read CSV file.
datas = pandas.read_csv('./Data/DataSet.csv')
number = datas.id.count()
data = []

# Make csv file for continuous features.
dqr_continuous(datas, continuous_names, number)
# Make csv file for categorical features.
dqr_categorical(datas, categorical_names, number)

# Generate graphs (html files) for all continuous features.
generate_graphs_for_continuous(datas, continuous_names)
# Generate graphs (html files) for all categorical features.
generate_graphs_for_categorical_names(datas, categorical_names)