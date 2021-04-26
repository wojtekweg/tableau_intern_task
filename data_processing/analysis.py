import json
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


def print_and_save(str_in, filename):
    # save to file
    text_file = open(f"{filename}.txt", "w")
    text_file.write(str_in)
    text_file.close()

    print(str_in)
    return str_in


def print_analysis(analysed_dict):
    """
    Print out the analysed dictionary as a string and save it to the .txt file.
    """
    intend = "  "
    ret_str = "Errors produced per hour for component (absolute = without considering severity, relative = with " \
              "linear weight for severity of each component):\n "
    # print(json.dumps(data_in, indent=4))
    # generate the string
    for d in analysed_dict:
        ret_str += f"{intend}{d}:\n"

        for i in analysed_dict[d]:
            ret_str += f"{intend}{intend}{'{:.4f}'.format(round(analysed_dict[d][i], 4))} ({i})\n"

    return ret_str


def print_conclusion(analysed_dict, rounding=2):
    abs_sorted = sorted(analysed_dict, key=lambda x: analysed_dict[x]['absolute'])[::-1]
    rel_sorted = sorted(analysed_dict, key=lambda x: analysed_dict[x]['relative'])[::-1]
    ret_str = f"\nComponent that was affected with biggest number of bugs was {abs_sorted[0]}, with " \
              f"{int(analysed_dict[abs_sorted[0]]['absolute'] * 6)} bugs, what resulted in " \
              f"{round(analysed_dict[abs_sorted[0]]['absolute'], rounding)} bugs per hour.\n" \
              f"Although, considering the severity of each bug, we can say that component {rel_sorted[0]} is " \
              f"the most bugged, with indicator of {round(analysed_dict[rel_sorted[0]]['relative'], rounding)} " \
              f"weighted bugs per hour.\nThe second biggest value for that scale is " \
              f"{round(analysed_dict[rel_sorted[1]]['relative'], rounding)} and the lowest value " \
              f"is {round(analysed_dict[rel_sorted[-1]]['relative'], rounding)} for {rel_sorted[-1]} component.\n"
    return ret_str
