import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'taintedalpha'
DATABASE = 'public'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=(PASSWORD), dbname=(DATABASE))
cursor = connection.cursor()
results = cursor.fetchall()
connection.close()

