import main
import sqlite3

conn = sqlite3.connect('movie.db')


def test_top10_profit_by_generes():
    actual_output = main.get_top10_category_by_profit('genres')
    expect_output = []
    sql_result = conn.execute("SELECT genres, AVG(profit) AS avg_profit "
                              "FROM (SELECT genres, (gross - budget) AS profit "
                              "      FROM movie_table) AS profit_summary "
                              "GROUP BY genres "
                              "ORDER BY avg_profit DESC "
                              "LIMIT 10;")
    for row in sql_result:
        expect_output.append(row[0])

    assert actual_output == expect_output


def test_top10_profit_by_director():
    actual_output = main.get_top10_category_by_profit('director_name')
    expect_output = []
    sql_result = conn.execute("SELECT director_name, AVG(profit) AS avg_profit "
                              "FROM (SELECT director_name, (gross - budget) AS profit "
                              "      FROM movie_table) AS profit_summary "
                              "GROUP BY director_name "
                              "ORDER BY avg_profit DESC "
                              "LIMIT 10;")
    for row in sql_result:
        expect_output.append(row[0])

    assert actual_output == expect_output
