import math
def get_cardinalities(datas):
	possible_values_with_cardinality = dict()
	for value in datas:
		if value in possible_values_with_cardinality.keys():
			possible_values_with_cardinality[value]=possible_values_with_cardinality[value]+1
		else:
			possible_values_with_cardinality[value]=1
	return possible_values_with_cardinality

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

feature = [True,False,True,False,False,True]
target = ['a','a','b','b','a','b']
print(calculate_remainder(get_cardinalities(feature), get_cardinalities(target)))