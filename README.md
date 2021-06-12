# Movie_Analyzer

A simple movie analyzer written in Python3.9 that:

a. Load the data into Sqlite database

b. Compute the top 10 genres in decreasing order by their profitability.

c. Return the top 10 actors or directors in decreasing order by their profitability

Data source:
https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset?select=movie_metadata.csv
Libraries used:
csv, sqlite3, pandas

To run program and see results:

1. load the csv data by running data_importer.py
2. run main.py(this should produce the result for a and b)

To run test cases:
1. load the csv data by running data_importer.py(this step can be skipped if db is already loaded from the previous step)
2. run unit_test.py
