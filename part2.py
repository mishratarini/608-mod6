# create a books database
import sqlite3
connection = sqlite3.connect('books.db')

# Read from authors, author_ISBN, and titles table in books DB
import pandas as pd
pd.options.display.max_columns = 10
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))
print(pd.read_sql('SELECT * FROM author_ISBN', connection))
print(pd.read_sql('SELECT * FROM titles', connection))

# Where and Order By clause on authors, author_ISBN, and titles table in books DB
import pandas as pd
pd.options.display.max_columns = 10
print(pd.read_sql('SELECT id, first, last FROM authors WHERE last LIKE "D%"', connection, index_col=['id']))
print(pd.read_sql('SELECT first, last FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER by last,first', connection))
print(pd.read_sql('SELECT title, edition, copyright FROM titles WHERE copyright > "2016" ORDER BY title ASC', connection))
