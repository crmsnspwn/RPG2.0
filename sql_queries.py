import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect('RPG2.db')
c = conn.cursor()

# with conn:
#     c.execute("""
#     CREATE TABLE Players
#     (ID INT NOT NULL,
#     NAME TEXT NOT NULL,
#     RACE TEXT NOT NULL,
#     CLASS TEXT NOT NULL,
#     LEVEL INT,
#     STRENGTH INT,
#     DEXTERITY INT,
#     CONSTITUTION INT,
#     INTELLIGENCE INT,
#     WISDOM INT,
#     CHARISMA INT,
#     HIT_POINTS INT,
#     SPELL_SLOTS INT,
#     BAG TEXT,
#     ARMOR TEXT,
#     WEAPON TEXT);
#     """)

c.execute("""
    SELECT tbl_name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name ASC
    """)
tables = c.fetchall()
for table in tables:
    print(table)