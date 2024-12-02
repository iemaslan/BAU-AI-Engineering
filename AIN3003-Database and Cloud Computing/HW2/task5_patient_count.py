import pymysql
from main import get_connection

my_connection = get_connection()
my_cursor = my_connection.cursor()

# SQL Query for Task 5
query = """
SELECT d.Name AS Doctor_Name, 
       COUNT(p.pat_id) AS Total_Patients
FROM Doctor d
LEFT JOIN Patient p ON d.dr_code = p.dr_code
GROUP BY d.dr_code;
"""

my_cursor.execute(query)

results = my_cursor.fetchall()

print("Doctor Name | Total Patients")
for row in results:
    print(f"{row[0]} | {row[1]}")

my_cursor.close()
my_connection.close()
