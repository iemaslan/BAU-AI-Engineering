from main import get_connection


my_connection = get_connection()
my_cursor = my_connection.cursor()

# Task 3: Doctor names and their patients
query = """
SELECT doctor.Name AS Doctor_Name, GROUP_CONCAT(patient.Name) AS Patients
FROM Doctor AS doctor
LEFT JOIN Patient AS patient ON doctor.dr_code = patient.dr_code
GROUP BY doctor.dr_code;
"""

try:
    my_cursor.execute(query)
    result = my_cursor.fetchall()

    for row in result:
        print(f"Doctor: {row[0]}, Patients: {row[1]}")
except Exception as e:
    print(f"Error: {e}")
finally:
    my_connection.close()
