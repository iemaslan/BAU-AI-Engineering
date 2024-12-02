from main import get_connection

my_connection = get_connection()
my_cursor = my_connection.cursor()

query = """
SELECT 
    p.Name AS Patient_Name,
    d.Name AS Doctor_Name,
    SUM(b.Amount) AS Total_Debt
FROM 
    Patient p
JOIN 
    Doctor d ON p.dr_code = d.dr_code
JOIN 
    Bill b ON p.pat_id = b.pat_id
WHERE 
    b.Amount > 100
GROUP BY 
    p.pat_id, d.dr_code;
"""

my_cursor.execute(query)

results = my_cursor.fetchall()
for row in results:
    print(f"Patient: {row[0]}, Doctor: {row[1]}, Total Debt: {row[2]}")

my_connection.close()
