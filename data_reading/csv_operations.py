import csv


def read_the_csv(filename):
    """
    Reads the .csv file in format specified in cycle_data.csv file.
    Expected format should contain following columns:
    "issue_code": row[0]
    "created_at": row[1]
    "severity": row[2]
    "resolution": row[3]
    "affected_components": row[4]
    "creator_id": row[5]
    :param filename: Path to the file that we want to be read.
    :return: Array of dictionary objects with all parameters read.
    """
    read_data = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            the_row = {
                "issue_code": row[0],
                "created_at": row[1],
                "severity": row[2],
                "resolution": row[3],
                "affected_components": row[4],
                "creator_id": row[5]
            }
            read_data.append(the_row)

    return read_data


def save_the_csv(dict_in, suffix):
    csv_columns = [
        "id_maj",
        "id_min",
        "issue_code",
        "severity",
        "affected_components",
        "resolution",
        "resolution_status",
        "created_at",
        "creator_id",
        "notes"]
    csv_file = f"cycle_data_{suffix}.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_in:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def delete_column_names(dict_in):
    """
    Function deletes the first element from given array.
    """
    # TODO add check for the input data, that each next dict is in the given schema, so deleting of the first row
    #  won't cause in lost any meaningful data.
    return dict_in[1:]
