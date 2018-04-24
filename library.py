import operator
import csv

# Make csv file for continous features.
def dqr_continuous(datas, continuous_names, number):
    first = number * 25 / 100
    third = number * 75 / 100

    with open('./Data/B-DQR-ContinuousFeatures.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['Feature', 'Count', 'Miss. (%)', 'Card.', 'Min.', '1st Qrt.', 'Mean', 'Median', '3rd Qrt.', 'Max.',
             'Std. Dev.'])
        for feature in continuous_names:
            count = datas[feature].count()
            miss = number - datas[feature].count()
            card = len(list(set(datas[feature])))
            min = datas[feature].min()
            fstQrt = datas[feature][first]
            mean = datas[feature][first]
            median = datas[feature].median()
            trdQrt = datas[feature][third]
            max = datas[feature].max()
            std = datas[feature].std()
            filewriter.writerow([feature, count, miss, card, min, fstQrt, mean, median, trdQrt, max, std])

# Make csv file for categorical features.
def dqr_categorical(datas, categorical_names):
    with open('./Data/B-DQR-CategoricalFeatures.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['Feature', 'Count', 'Miss', 'Card', 'Mode', 'Mode Freq.', 'Mode (%)', '2nd Mode', '2nd Mode Freq',
             '2nd Mode (%)'])
        for feature in categorical_names:
            count = datas[feature].count()
            miss = -count_missing(datas, feature) * 100 / count
            card = count_cardinality(datas, feature)
            mode, mode_freq, second_mode, second_mode_freq = count_modes(datas, feature)
            mode_perc = (count - mode_freq) * 100 / count
            second_mode_perc = (count - second_mode_freq) * 100 / count
            filewriter.writerow(
                [feature, count, miss, card, mode, mode_freq, mode_perc, second_mode, second_mode_freq, second_mode_perc])

# Generate graphs (html files) for all continuous features.
def generate_graphs_for_continuous(datas, continuous_names):
    for feature in continuous_names:
        unique = list(datas[feature])
        values = list()
        for u in unique:
            values.append(datas[feature].tolist().count(u))
        if len(unique) >= 10:
            # We create a histogram.
            chart = [go.Histogram(
                x = unique
            )]
        else:
            # We create a bar plot.
            chart = [go.Bar(
                x = numpy.asarray(unique),
                y = numpy.asarray(values)
            )]
        layout = go.Layout(
            title=feature,
        )

        fig = go.Figure(data=chart, layout=layout)
        plotly.offline.plot(fig, filename="./Visualisations/"+feature+".html")

# Generate graphs (html files) for all categorical features.
def generate_graphs_for_categorical_names(datas, categorical_names):
    for feature in categorical_names:
        unique = list(set(datas[feature]))
        values = list()
        for u in unique:
            values.append(datas[feature].tolist().count(u))
        chart = [go.Bar(
            x = numpy.asarray(unique),
            y = numpy.asarray(values)
        )]
        layout = go.Layout(
            title=feature,
        )
        fig = go.Figure(data=chart, layout=layout)
        plotly.offline.plot(fig, filename="./Visualisations/"+feature+".html")

def count_modes(datas, feature):
    possible_values_with_cardinality = dict()
    for value in datas[feature]:
        if value in possible_values_with_cardinality.keys():
            possible_values_with_cardinality[value] = possible_values_with_cardinality[value] + 1
        else:
            possible_values_with_cardinality[value] = 1
    # Don't forget to import operator !
    sorted_possible_values_with_cardinality = sorted(possible_values_with_cardinality.items(),
                                                     key=operator.itemgetter(1))
    length = len(sorted_possible_values_with_cardinality)
    mode = sorted_possible_values_with_cardinality[length - 1][0]
    mode_freq = sorted_possible_values_with_cardinality[length - 1][1]
    second_mode = sorted_possible_values_with_cardinality[length - 2][0]
    second_mode_freq = sorted_possible_values_with_cardinality[length - 2][1]
    return mode, mode_freq, second_mode, second_mode_freq

def count_missing(datas, feature):
    count = 0
    for value in datas[feature]:
        if value != " ?":
            count = count + 1
    return count

def count_cardinality(datas, feature):
    possible_values = list()
    for value in datas[feature]:
        if value not in possible_values:
            possible_values.append(value)
    return len(possible_values)