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
