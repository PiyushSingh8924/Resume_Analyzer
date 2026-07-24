import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P!yu5h@9780",
        database="resume_analyzer"
    )

    print("✅Connected to MySQL successfully!")

except mysql.connector.Error as err:
    print("Connection Error:", err)