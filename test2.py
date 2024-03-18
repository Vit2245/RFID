import mysql.connector

try:
    conn = mysql.connector.connect(
        host="158.160.152.77",
        user="vitas",
        password="Izl_2245739",
        database="testrfid"
    )

except mysql.connector.Error as e:
    print("Ошибка при подключении к базе данных")