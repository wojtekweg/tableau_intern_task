import os


from data_processing.csv_operations import delete_column_names, read_the_csv


def count_severity_weights(data_in):
    """
    Count weighted average of severity.
    """
    curr_sum = 0
    for d in data_in:
        curr_sum += int(d['severity_weight'])

    return curr_sum / len(data_in)


def generate_analysis(directory):
    """
    For each component generate a dictionary with absolute and relative errors produced per hour.
    """
    analysis = {}
    for file in os.listdir(directory):
        curr_component = read_the_csv(directory + "/" + file)
        curr_component = delete_column_names(curr_component)

        unweighted_severity = len(curr_component) / 6
        weighted_severity = count_severity_weights(curr_component) / 6

        analysis.update({file[:-4]: {"absolute": unweighted_severity, "relative": weighted_severity}})
    return analysis

