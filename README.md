# Movie_Analyzer

A simple movie analyzer that:

a. Load the data into Sqlite database

b. Compute the top 10 genres in decreasing order by their profitability.

c. Return the top 10 actors or directors in decreasing order by their profitability

Data source:
https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset?select=movie_metadata.csv


To run the program:

1. load the csv data by running data_importer.py
2. run main.py(this should produce the result for a and b above)

To run test cases:
1. load the csv data by running data_importer.py(this step can be skipped if db is already loaded from the previous step)
2. run unit_test.py
