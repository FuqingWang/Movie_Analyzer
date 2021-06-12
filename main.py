import sqlite3
import pandas as pd


def get_top10_category_by_profit(col_name):
    conn = sqlite3.connect('movie.db')

    df = pd.read_sql_query(f"SELECT {col_name}, budget, gross from movie_table", conn)

    # data pre-processing
    # drop rows with 0 values on budget or gross
    df.drop(df[df['budget'] == 0].index, inplace=True)
    df.drop(df[df['gross'] == 0].index, inplace=True)

    # compute profit = gross - budget
    df['profit'] = df.apply(lambda row: row.gross - row.budget, axis=1)

    # analysis
    # compute the mean profit for each generes
    df_mean_profit = df.groupby([col_name]).mean()

    df_top10 = df_mean_profit.sort_values('profit', ascending=False).head(10)
    #print(df_top10)
    print(list(df_top10.index.values))

    return list(df_top10.index.values)


def main():
    print("The top 10 genres by profit is: ")
    get_top10_category_by_profit('genres')

    print("The top 10 director by profit is: ")
    get_top10_category_by_profit('director_name')


if __name__ == '__main__':
    main()
