import math
from library import *

def entropy(dict_of_target_cardinalities):
	entrop = 0
	for value in dict_of_target_cardinalities:
		entrop = entrop + (dict_of_target_cardinalities[value]/sum(dict_of_target_cardinalities.values())) * math.log2(dict_of_target_cardinalities[value]/sum(dict_of_target_cardinalities.values()))
	return entrop

def calculate_remainder(dict_of_feature_cardinalities,dict_of_target_cardinalities):
	remainder = 0
	for value in dict_of_feature_cardinalities:
		remainder = remainder + (dict_of_feature_cardinalities[value]/sum(dict_of_feature_cardinalities.values())) * (entropy(dict_of_target_cardinalities))
	return -remainder
