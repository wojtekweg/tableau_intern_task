"""
This is a recruiting process task for Data Analyst Intern at Tableau.
Author of the solution: Wojciech Węgrzyn.

My solution is written with using of .csv files as a storage for the data. I know that such data structure choice is
not as scalable as SQL database and not as features-rich as Pandas, but it was my first idea and since recruitment task
has limited time and I do not have much free time I decided to not rewriting it for other choice. Although I am aware
that this kind of solution is far from perfect.

Code that you are about to see has some TO-DO comments here and there - I decided to mark that way situations where I
know something should be written better, but due to some limitations (mostly time) I wasn't able to change it.

The task content:
You are facing the new task: yours new PM asked you for help in calculating and visualizing the new KPI, that will
help in process of providing results for the client.

The KPI definition is: amount of accepted errors per hour in first 6 hours since starting the testing cycle. PM told
you that for sake of simplicity you can assume that cycle starts with the first reported error.

If you will be able to show that metric, PM will appreciate analysis of the data, because he has no time for it.

Create the view that will show the given metric and suggest another charts that will be helpful for PM.
"""
from tableau_intern_task.data_reading.cleaning import clean
from tableau_intern_task.data_reading.printing import get_set
from tableau_intern_task.data_reading.selecting import select
from tableau_intern_task.data_reading.csv_operations import *

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
    pass
