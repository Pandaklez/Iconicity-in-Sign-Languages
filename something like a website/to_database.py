import csv
import sqlite3

con = sqlite3.connect("app.db")
cur = con.cursor()
cur.execute("CREATE TABLE t (word VARCHAR(100), semantic_field VARCHAR(100), base VARCHAR(100), pattern VARCHAR(100), non_iconic VARCHAR(100), languages VARCHAR(100), urls VARCHAR(100));") # use your column names here

with open('annotated_data_new.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['word'], i['semantic_field'], i['base'], i['pattern'], i['non_iconic'], i['languages'], i['urls']) for i in dr]

cur.executemany("INSERT INTO t (word, semantic_field, base, pattern, non_iconic, languages, urls) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()
