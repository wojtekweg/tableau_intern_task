from data_processing.cleaning import clean
from data_processing.printing import *
from data_processing.selecting import *
from data_processing.analysis import *
from data_processing.csv_operations import *
from datetime import timedelta

if __name__ == "__main__":
    # read the data
    curr_data = read_the_csv("cycle_data.csv", is_cleaned=False)
    curr_data = delete_column_names(curr_data)

    # scales for weighting severity of the bugs
    scale_linear = (1, 2, 3, 4)
    scale_log = (10, 100, 1000, 10000)
    scale_custom = (1, 5, 15, 25)
    clean(curr_data, scale_log)
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

    # analyse the data
    analysis = generate_analysis('./by_component')
    print_and_save(print_analysis(analysis) + print_conclusion(analysis), "analysis_and_conclusion(custom_scale)")
