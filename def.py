import psycopg2
import pandas as pd
from datetime import datetime
import warnings

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

conn = psycopg2.connect("host = '192.168.0.223' user = 'casaos' password = 'casaos' dbname = 'casaos'")

cur = conn.cursor()
#cur.execute("""SELECT datname FROM pg_database;""")
#print(f"datbases: {[x[0] for x in cur.fetchall()]}")

cur.execute("""CREATE TABLE IF NOT EXISTS test (
    column1 text,
    column2 text,
    column3 text
);""")

now =datetime.strftime(datetime.now(),'%Y-%m-%d-%H-%M-%S')
cur.execute("INSERT INTO test (column1,column2,column3) VALUES ('{}','{}','{}')".format(now,now,now))
conn.commit()

#tbl_list_df = pd.read_sql_query("SELECT * FROM pg_catalog.pg_tables WHERE Schemaname = 'public'", conn)
print("------------------------------------------------------------------------------------")

cur.close()
conn.close()