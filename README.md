# Recruiting process task for Data Analyst Intern at Global App Testing.

## The task content

You are facing the new task: yours new PM asked you for help in calculating and visualizing the new KPI, that will
help in process of providing results for the client.

The KPI definition is: amount of accepted errors per an hour in first 6 hours since starting the testing cycle. PM told
you that for sake of simplicity you can assume that cycle starts with the first reported error.

If you will be able to show that metric, PM will appreciate analysis of the data, because he has no time for it.

Create the view that will show the given metric and suggest another charts that will be helpful for PM.

File that you have to analyze: cycle_data.csv

## Running my solution 

To run the script that will generate an answer for this task, just simply execute the `__main__.py` script. 

After that, follow the instructions and proceed to `./outcomes` folder, where you will be able to read analysis.

The script was written with use of Python 3.9, and some libraries specified in `requirements.txt`.


## The steps

In order to analise the given data I have taken the following steps:

- Handling I/O operations

    - Reading and saving to/from .csv file with given schema of data.

- Data cleaning

    - If possible, matching the words for given pattern (for example removing parenthesis).
    
    - Handling the date as `datetime` objects.
    
    - Estimating the dates of bugs with lack of date.
    
    - Fitting the `resolution` and `cycle_id` columns to the pattern.
    
    - Representing `severity` as a number in scale selected by the user.

- Selecting

    - Rejecting bugs with status different from `Confirmed`.
    
    - Rejecting bugs that does not fit the given time delta.

- Analysis and printing

    - Automatically printing of the analysis written in human-readable format.

## Final outcomes

Head to folder `./outcomes` if you wish to read the answer of the task. I focused only on severity and amount of the 
errors, since these metrics seemed most obvious to me. I don't know exactly from where comes the given data, so I ignored
some given data. For example `creator_id` column is ignored in my solution, although if needed it is fairly easy to 
modify the script, so it will analise the data in that point of view, instead of severity.

The visualization for the outcomes has been made in Google Docs Spreadsheets - I had no time for proper scripting the 
visualizations, and I didn't want to make it anyhow, but automatic.

All the outcomes are based on the task criteria - 6 hours time range since the first bug and "Confirmed" status.

## Thoughts about my solution

For each step I have written scripts exclusively for this task. After all hard work, I realized that not all of my work 
was necessary - for example I should have used Pandas for cleaning and selecting the data, and I could possibly use some 
SQL database instead of the .csv files. I hope though, that my solution will meet assumptions of the task.

What I know I should have made is visualization of the data. It is a pity that my answer doesn't come with that, but
I simply couldn't find time to provide it. The main reason for that is my lack of time, which came in a pair with poor
focus of the different aspects of the solution - I think that I should focus more on representation of analysis, than 
on cleaning the data (I could have made some of clean-ups manually). On the other hand, I hope that you will appreciate
that in most of the cases my solution is pretty much scalable and if not, it could be easily improved for handling other
issues of provided data.

The example input data is left in a repository, due to the nature of recruitment task.