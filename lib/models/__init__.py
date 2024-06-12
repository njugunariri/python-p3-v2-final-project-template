import sqlite3

CONN = sqlite3.connect('lib/models/library.db')
CURSOR = CONN.cursor()
