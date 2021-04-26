import json
import datetime


def get_set(data_in, column):
    """
    Returns the set of given key in an array of dictionaries.
    """
    temp = []
    for dict_ in data_in:
        temp.append(dict_[f"{column}"])
    return set(temp)


def print_read_data_as_set(data_in):
    """
    Function prints all the data from dictionaries with specified schema without the duplicates.
    """
    print(get_set(data_in, "affected_components"))
    print(get_set(data_in, "created_at"))
    print(get_set(data_in, "creator_id"))
    print(get_set(data_in, "issue_code"))
    print(get_set(data_in, "resolution"))
    print(get_set(data_in, "severity"))


def print_read_data(data_in):
    """
    Regular print for the provided dictionary.
    """
    temp = data_in
    if isinstance(temp[0]["created_at"], datetime.datetime):
        for d in temp:
            d["created_at"] = d["created_at"].strftime("%d %b %Y %H:%M:%S")
    print(json.dumps(temp, sort_keys=True, indent=4))


def print_and_save(str_in, filename):
    # save to file
    text_file = open(f"./outcomes/{filename}.txt", "w")
    text_file.write(str_in)
    text_file.close()

    print(str_in)
    return str_in


def print_component_analysis(analysed_dict, scale):
    """
    Print out the analysed dictionary as a string and save it to the .txt file.
    """
    intend = "  "
    ret_str = "Errors produced per hour for component (absolute = without considering severity, relative = with " \
              f"{scale} weight for severity of each component):\n "
    # print(json.dumps(data_in, indent=4))
    # generate the string
    for d in analysed_dict:
        ret_str += f"{intend}{d}:\n"

        for i in analysed_dict[d]:
            ret_str += f"{intend}{intend}{'{:.4f}'.format(round(analysed_dict[d][i], 4))} ({i})\n"

    return ret_str


def print_component_conclusion(analysed_dict, rounding=2):
    """
    Sort the values and print it as a text.
    """
    abs_sorted = sorted(analysed_dict, key=lambda x: analysed_dict[x]['absolute'])[::-1]
    rel_sorted = sorted(analysed_dict, key=lambda x: analysed_dict[x]['relative'])[::-1]
    ret_str = f"\nComponent that was affected with biggest number of bugs was {abs_sorted[0]}, with " \
              f"{int(analysed_dict[abs_sorted[0]]['absolute'] * 6)} bugs, what resulted in " \
              f"{round(analysed_dict[abs_sorted[0]]['absolute'], rounding)} bugs per hour.\n" \
              f"Although, considering the severity of each bug, we can say that component {rel_sorted[0]} is " \
              f"the most bugged, with indicator of {round(analysed_dict[rel_sorted[0]]['relative'], rounding)} " \
              f"weighted bugs per hour.\nThe second biggest value for that scale is " \
              f"{round(analysed_dict[rel_sorted[1]]['relative'], rounding)} for {rel_sorted[1]} and the lowest value " \
              f"is {round(analysed_dict[rel_sorted[-1]]['relative'], rounding)} for {rel_sorted[-1]} component.\n"
    return ret_str
