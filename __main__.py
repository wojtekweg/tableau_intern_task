from data_processing.cleaning import clean
from data_processing.printing import *
from data_processing.selecting import *
from data_processing.analysis import *
from data_processing.csv_operations import *
from datetime import timedelta


def user_input_scale():
    scale_linear = (1, 2, 3, 4)
    scale_log = (10, 100, 1000, 10000)
    scale_custom = (1, 5, 25, 50)

    user_input = input("Choose a scale for weighting the severity from:\n"
                       f" - 'linear' {scale_linear}\n"
                       f" - 'log' {scale_log}\n"
                       f" - 'custom' {scale_custom}\n"
                       " - any other input to enter four integers to define a scale\n")

    if user_input == 'linear':
        chosen_scale = scale_linear
    elif user_input == 'log':
        chosen_scale = scale_log
    elif user_input == 'custom':
        chosen_scale = scale_custom
    else:
        chosen_scale = []
        while len(chosen_scale) < 4:
            try:
                n = input(f"Enter {len(chosen_scale) + 1} number: \n")
                chosen_scale.append(int(n))
            except ValueError:
                print("Not an int number entered, try again.")
    return user_input, chosen_scale


if __name__ == "__main__":
    # read the data
    curr_data = read_the_csv("cycle_data.csv", is_cleaned=False)
    curr_data = delete_column_names(curr_data)

    # scales for weighting severity of the bugs
    scale_in, scale = user_input_scale()
    clean(curr_data, scale)
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

    # It seems to be reasonable to analise the data, based on the creator_id. Since I don't know much
    # about the product and I would probably misinterpret that metric, I won't analise it. But I tried
    # to make this code as generic as possible, so uncommenting below lines will save the grouped data
    # in separate .csv files and further analysis shouldn't be hard to rewrite for that point of view.
    #
    # for creator in get_set(curr_data, "creator_id"):
    #     temp = select_given_key(curr_data, "creator_id", creator)
    #     save_the_csv(temp, filename=creator, directory="by_creator")

    # analyse the data
    analysis = generate_component_analysis('./by_component')
    print_and_save(print_component_analysis(analysis, f"{scale_in} {scale}") +
                   print_component_conclusion(analysis),
                   f"analysis_and_conclusion({scale_in}_scale)")
