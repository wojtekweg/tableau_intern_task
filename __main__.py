from data_processing.cleaning import clean
from data_processing.printing import get_set
from data_processing.selecting import *
from data_processing.csv_operations import *
from datetime import timedelta
import os

if __name__ == "__main__":
    # read the data
    curr_data = read_the_csv("cycle_data.csv")
    curr_data = delete_column_names(curr_data)

    clean(curr_data)
    # save_the_csv(curr_data, "cleaned")

    first_reported_error_date = min(get_set(curr_data, "created_at"))
    error_date_range = timedelta(hours=6)
    curr_data = select(curr_data, first_reported_error_date, error_date_range)
    # save_the_csv(curr_data, "selected")

    # save the data as all rows are selected and cleaned for analysis
    save_the_csv(curr_data, filename="cycle_data", suffix="done")

    # group the columns by the affected components
    for component in get_set(curr_data, "affected_components"):
        temp = select_given_key(curr_data, "affected_components", component)
        save_the_csv(temp, filename=component, directory="by_component")

    # for creator in get_set(curr_data, "creator_id"):
    #     temp = select_given_key(curr_data, "creator_id", creator)
    #     save_the_csv(temp, filename=creator, directory="by_creator")

    # print out the analysis, by writing out:
    # (1) simply the errors produced per hour
    # (2) errors produced per hour, but each bug scaled by its severity
    dir_to_search = './by_component'
    for file in os.listdir(dir_to_search):
        curr_component = read_the_csv(dir_to_search + "/" + file)
        delete_column_names(curr_component)
        print(curr_component)
        print(len(curr_component))

