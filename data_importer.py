import csv
import sqlite3

conn = sqlite3.connect('movie.db')
cur = conn.cursor()
print("connected to sqlite3")


def db_create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS movie_table ("
                "color, director_name, num_critic_for_reviews, duration, director_facebook_likes, "
                "actor_3_facebook_likes, actor_2_name, actor_1_facebook_likes, "
                "gross REAL, "
                "genres, actor_1_name, movie_title, num_voted_users, cast_total_facebook_likes, "
                "actor_3_name, facenumber_in_poster, plot_keywords, "
                "movie_imdb_link, num_user_for_reviews, language, country, content_rating, "
                "budget REAL, "
                "title_year, actor_2_facebook_likes, imdb_score, aspect_ratio, movie_facebook_likes);")

    print("Table created successfully")


def db_import_csv():
    with open('movie_metadata.csv', 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if line[8] != '' and line[22] != '':
                conn.execute("INSERT into movie_table values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                             (str(line[0]), str(line[1]), str(line[2]), str(line[3]), str(line[4]), str(line[5]),
                              str(line[6]), str(line[7]), float(line[8]), str(line[9]), str(line[10]), str(line[11]),
                              str(line[12]), str(line[13]), str(line[14]), str(line[15]), str(line[16]), str(line[17]),
                              str(line[18]), str(line[19]), str(line[20]), str(line[21]), float(line[22]), str(line[23]),
                              str(line[24]), str(line[25]), str(line[26]), str(line[27])))
            if line[9] == 'Family|Sci-Fi':
                print(f"gross: {line[8]}, budget: {line[22]}")
                print(line[8] != '' and line[22] != '')
    print("Data imported successfully")


db_create_table()
db_import_csv()
conn.commit()
conn.close()
print("close connection")
