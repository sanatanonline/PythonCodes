import mysql.connector
import datetime

my_db = mysql.connector.connect(
    host="localhost",
    user="genlogos",
    passwd="Genlogos@2019",
    database="genlogos"
)

print(my_db)

my_cursor = my_db.cursor()
print(my_cursor)

sql = "insert into t_gl_event (" \
      "event_id, reference_no, logtime, event_type, event_name, event_xml) " \
      "VALUES (%s, %s, %s, %s, %s, %s)"

val = ("1cvvddf-3434f34gg", "1cvvddf-3434f34f", datetime.datetime.now(), "BUSINESS", "CLICK_EVENT", "xml")
my_cursor.execute(sql, val)
my_db.commit()

my_cursor.execute("select * from t_gl_event")

my_result = my_cursor.fetchall()

for x in my_result:
    print(type(x))
    print(x)

my_cursor.close()
my_db.close
