import pandas
import csv
import os

# Import custom functions.
from DQR_CSVFileManagment import *
from DQR_PlotGraphicalDisplay import *

# Create directory for Virsualisations (html files).
if not os.path.exists('Visualisations'):
	os.makedirs('Visualisations')

# Read CSV file.
try:
	datas = pandas.read_csv('./Data/DataSet.csv').replace(" ?","?")
except:
	print("Error: ./data/DataSet.csv is missing.")
	exit()


# Define if name is continuous or categorical
continuous_names, categorical_names = make_list_name(datas)

# Write in a new csv file for continuous features.
dqr_continuous(datas, continuous_names)
# Write in a new csv file for categorical features.
dqr_categorical(datas, categorical_names)

# Generate graphs (html local files) for all continuous features.
generate_graphs(datas, continuous_names, True)
generate_graphs(datas, categorical_names, False)
	
