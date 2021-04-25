from data_reading.cleaning import clean
from data_reading.printing import get_set
from data_reading.selecting import select
from data_reading.csv_operations import *

if __name__ == "__main__":
    # read the data
    curr_data = read_the_csv("cycle_data.csv")
    curr_data = delete_column_names(curr_data)

    clean(curr_data)
    # save_the_csv(curr_data, "cleaned")

    first_reported_error_date = min(get_set(curr_data, "created_at"))
    curr_data = select(curr_data, first_reported_error_date)
    # save_the_csv(curr_data, "selected")

    # save the data as all rows are selected and cleaned for analysis
    save_the_csv(curr_data, "done")
