import pymysql

my_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="my_computer_password",
    database="banking"
)

my_cursor = my_connection.cursor()


create_doctor_table = """
CREATE TABLE IF NOT EXISTS Doctor (
    dr_code INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Fname VARCHAR(100),
    Gender ENUM('Male', 'Female', 'Other'),
    Address VARCHAR(255),
    Designation VARCHAR(100)
);
"""


create_patient_table = """
CREATE TABLE IF NOT EXISTS Patient (
    pat_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Fname VARCHAR(100),
    Gender ENUM('Male', 'Female', 'Other'),
    Address VARCHAR(255),
    TellNum VARCHAR(15),
    dr_code INT,
    FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""

create_staff_table = """
CREATE TABLE IF NOT EXISTS Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Dept VARCHAR(100),
    Gender ENUM('Male', 'Female', 'Other'),
    Address VARCHAR(255),
    CellNum VARCHAR(15),
    dr_code INT,
    FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""

create_diagnosis_table = """
CREATE TABLE IF NOT EXISTS PatientDiagnosis (
    DiagNo INT AUTO_INCREMENT PRIMARY KEY,
    DiagDetails TEXT,
    Remark TEXT,
    DiagDate DATE,
    Other TEXT,
    pat_id INT,
    FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

create_bill_table = """
CREATE TABLE IF NOT EXISTS Bill (
    BillNo INT AUTO_INCREMENT PRIMARY KEY,
    PatName VARCHAR(100),
    DrName VARCHAR(100),
    Datetime DATETIME,
    Amount DECIMAL(10, 2),
    pat_id INT,
    FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

my_cursor.execute(create_doctor_table)
my_cursor.execute(create_patient_table)
my_cursor.execute(create_staff_table)
my_cursor.execute(create_diagnosis_table)
my_cursor.execute(create_bill_table)

print("Tables created successfully.")

my_cursor.close()
my_connection.close()
