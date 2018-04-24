import pandas
import csv
import os

# Import custom functions.
from library import *

# Create directory for Virsualisations (html files).
if not os.path.exists('Visualisations'):
    os.makedirs('Visualisations')

names = ['id','age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','target']

# Read CSV file.
datas = pandas.read_csv('./Data/DataSet.csv')
number = datas.id.count()
data = []

# Define if name is continuous or categorical
continuous_names, categorical_names = make_list_name(datas, names)

# Make csv file for continuous features.
dqr_continuous(datas, continuous_names, number)
# Make csv file for categorical features.
dqr_categorical(datas, categorical_names)

# Generate graphs (html files) for all continuous features.
generate_graphs(datas, continuous_names, 1)
generate_graphs(datas, categorical_names, 0)

# Generate graphs (html files) for all continuous features.
# generate_graphs_for_continuous(datas, continuous_names)
# Generate graphs (html files) for all categorical features.
# generate_graphs_for_categorical_names(datas, categorical_names)
