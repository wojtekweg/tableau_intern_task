# Recruiting process task for Data Analyst Intern at Tableau.

## Thoughts about my solution

My solution is written with using of .csv files as a storage for the data. I know that such data structure choice is
not as scalable as SQL database and not as features-rich as Pandas, but it was my first idea and since recruitment task
has limited time, and I do not have much free time I decided to not rewriting it for other choice. Although I am aware
that this kind of solution is far from perfect.

Code that you are about to see has some TO-DO comments here and there - I decided to mark that way situations where I
know something should be written better, but due to some limitations (mostly time) I wasn't able to change it.

## The task content

You are facing the new task: yours new PM asked you for help in calculating and visualizing the new KPI, that will
help in process of providing results for the client.

The KPI definition is: amount of accepted errors per hour in first 6 hours since starting the testing cycle. PM told
you that for sake of simplicity you can assume that cycle starts with the first reported error.

If you will be able to show that metric, PM will appreciate analysis of the data, because he has no time for it.

Create the view that will show the given metric and suggest another charts that will be helpful for PM.

File that you have to analyze: cycle_data.csv