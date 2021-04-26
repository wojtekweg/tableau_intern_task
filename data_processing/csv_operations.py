import csv
import os

csv_columns_cleaned = [
    "id_maj",
    "id_min",
    "issue_code",
    "severity",
    "severity_weight",
    "affected_components",
    "resolution",
    "resolution_status",
    "created_at",
    "creator_id",
    "notes"]

csv_columns_not_edited = [
    "issue_code",
    "created_at",
    "severity",
    "resolution",
    "affected_components",
    "creator_id"
]


def read_the_csv(filename, is_cleaned=True):
    """
    Reads the .csv file in format specified in cycle_data.csv file.
    Expected format should contain columns specified in above variables.
    :param filename: Path to the file that we want to be read.
    :param is_cleaned: Specify whether the file was already cleaned.
    :return: Array of dictionary objects with all parameters read.
    """
    read_data = []
    csv_schema = csv_columns_cleaned if is_cleaned else csv_columns_not_edited

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            temp = {}
            for i in range(len(csv_schema)):
                temp.update({csv_schema[i]: row[i]})
            read_data.append(temp)

    return read_data


def save_the_csv(dict_in, filename="cycle_data", suffix="", directory=""):
    if directory != "":
        directory = f"./{directory}/"
        try:
            os.mkdir(f"./{directory}")
        except OSError:
            pass
    if suffix != "":
        suffix = f"_{suffix}"
    csv_file = f"{directory}{filename}{suffix}.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns_cleaned)
            writer.writeheader()
            for data in dict_in:
                writer.writerow(data)
    except IOError:
        print("[ ERROR ] Couldn't save the .csv file due to I/O error.")


def delete_column_names(dict_in):
    """
    Function deletes the first element from given array.
    """
    # TODO add check for the input data, that each next dict is in the given schema, so deleting of the first row
    #  won't cause in lost any meaningful data.
    return dict_in[1:]
