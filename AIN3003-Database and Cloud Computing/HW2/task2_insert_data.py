from task1_create_table import my_connection

my_cursor = my_connection.cursor()

# Task 2: DML Statements to Insert Sample Data
insert_doctor_data = """
INSERT INTO Doctor (Name, Fname, Gender, Address, Designation) VALUES
('John Doe', 'William', 'Male', '123 Elm Street', 'Cardiologist'),
('Jane Smith', 'Olivia', 'Female', '456 Oak Avenue', 'Neurologist'),
('Sam Brown', 'Michael', 'Male', '789 Pine Road', 'Pediatrician'),
('Alice Johnson', 'Emma', 'Female', '12 Birch Lane', 'Dermatologist'),
('Michael Davis', 'David', 'Male', '34 Cedar Drive', 'Surgeon'),
('Emily White', 'Sophia', 'Female', '56 Spruce Street', 'Psychiatrist'),
('Chris Green', 'James', 'Male', '78 Willow Court', 'Orthopedist'),
('Olivia Wilson', 'Charlotte', 'Female', '90 Maple Avenue', 'Gynecologist'),
('Liam Thomas', 'Henry', 'Male', '101 Walnut Boulevard', 'Ophthalmologist'),
('Sophia Martinez', 'Isabella', 'Female', '112 Poplar Road', 'ENT Specialist'),
('Noah Garcia', 'Mason', 'Male', '123 Cypress Circle', 'Oncologist'),
('Ava Rodriguez', 'Amelia', 'Female', '145 Chestnut Place', 'Rheumatologist'),
('Ethan Lee', 'Logan', 'Male', '156 Hickory Drive', 'Pulmonologist'),
('Isabella Brown', 'Abigail', 'Female', '167 Redwood Lane', 'Anesthesiologist'),
('Mason Clark', 'Aiden', 'Male', '178 Fir Court', 'General Practitioner'),
('Mia Lewis', 'Madison', 'Female', '189 Ash Way', 'Urologist'),
('Lucas Hall', 'Elijah', 'Male', '200 Beech Road', 'Immunologist'),
('Amelia Young', 'Harper', 'Female', '211 Dogwood Lane', 'Nephrologist'),
('Jacob King', 'Eli', 'Male', '222 Olive Court', 'Hematologist'),
('Aiden Scott', 'Carter', 'Male', '233 Acacia Street', 'Radiologist'),
('Emma Adams', 'Ava', 'Female', '244 Willow Walk', 'Endocrinologist'),
('James Wright', 'Isaac', 'Male', '255 Sequoia Drive', 'Pathologist'),
('Harper Walker', 'Aria', 'Female', '266 Maplewood Lane', 'Plastic Surgeon'),
('Logan Harris', 'Luke', 'Male', '277 Redwood Boulevard', 'Neurologist'),
('Abigail Baker', 'Sofia', 'Female', '288 Elm Avenue', 'Cardiologist'),
('Daniel Perez', 'Daniel', 'Male', '299 Sycamore Place', 'Dermatologist'),
('Elijah Torres', 'Samuel', 'Male', '310 Aspen Court', 'Orthopedist'),
('Chloe Rivera', 'Evelyn', 'Female', '321 Oakwood Street', 'Pediatrician'),
('Henry Brooks', 'Landon', 'Male', '332 Cedar Avenue', 'Psychiatrist'),
('Aria Bell', 'Scarlett', 'Female', '343 Magnolia Road', 'Surgeon'),
('Carter Murphy', 'Nathan', 'Male', '354 Linden Street', 'Gynecologist'),
('Ella Cox', 'Grace', 'Female', '365 Aspen Way', 'ENT Specialist'),
('Benjamin Gray', 'Jack', 'Male', '376 Pinewood Road', 'Oncologist'),
('Lily Flores', 'Ellie', 'Female', '387 Birch Court', 'Rheumatologist'),
('Andrew Simmons', 'Gabriel', 'Male', '398 Willow Drive', 'Pulmonologist'),
('Madison Nelson', 'Hazel', 'Female', '409 Maple Circle', 'Urologist'),
('David Mitchell', 'Julian', 'Male', '420 Chestnut Street', 'General Practitioner'),
('Scarlett Price', 'Violet', 'Female', '431 Redwood Court', 'Immunologist'),
('Eli Carter', 'Wyatt', 'Male', '442 Sequoia Road', 'Nephrologist'),
('Violet Rogers', 'Aurora', 'Female', '453 Oak Street', 'Hematologist'),
('Aaron Fisher', 'Grayson', 'Male', '464 Spruce Lane', 'Radiologist'),
('Sofia Reed', 'Layla', 'Female', '475 Cypress Avenue', 'Endocrinologist'),
('Owen Howard', 'Evan', 'Male', '486 Birchwood Boulevard', 'Plastic Surgeon'),
('Layla Butler', 'Penelope', 'Female', '497 Maple Lane', 'Pathologist'),
('Alexander Ramirez', 'Xavier', 'Male', '508 Cedar Court', 'Oncologist'),
('Aurora Kelly', 'Lucy', 'Female', '519 Redwood Boulevard', 'Psychiatrist'),
('Nathan Jenkins', 'Dylan', 'Male', '530 Willow Road', 'Orthopedist'),
('Grace Sanders', 'Audrey', 'Female', '541 Aspen Avenue', 'Surgeon'),
('John Doe', 'William', 'Male', '123 Elm Street', 'Cardiologist'),
('Jane Smith', 'Olivia', 'Female', '456 Oak Avenue', 'Neurologist'),
('Sam Brown', 'Michael', 'Male', '789 Pine Road', 'Dermatologist');


"""
try:
    my_cursor.execute(insert_doctor_data)
    print("Doctor data inserted successfully")
except Exception as e:
    print(f"Error inserting doctor data: {e}")

insert_patient_data = """
INSERT INTO Patient (Name, Fname, Gender, Address, TellNum, dr_code) VALUES
('Liam Anderson', 'Oliver', 'Male', '123 Oak Street', '555-123-4567', 1),
('Emma Taylor', 'Ava', 'Female', '456 Pine Avenue', '555-234-5678', 2),
('Noah Martinez', 'James', 'Male', '789 Birch Road', '555-345-6789', 3),
('Sophia White', 'Charlotte', 'Female', '123 Elm Street', '555-456-7890', 7),
('Mason Clark', 'Henry', 'Male', '456 Oak Avenue', '555-567-8901', 8),
('Ava Brown', 'Amelia', 'Female', '789 Pine Road', '555-678-9012', 9),
('Isabella Wilson', 'Isla', 'Female', '123 Birch Lane', '555-789-0123', 10),
('Ethan King', 'Logan', 'Male', '456 Cedar Drive', '555-890-1234', 11),
('Mia Lewis', 'Ella', 'Female', '789 Spruce Street', '555-901-2345', 12),
('James Hall', 'Lucas', 'Male', '123 Willow Court', '555-012-3456', 13),
('Olivia Moore', 'Grace', 'Female', '456 Maple Avenue', '555-123-4567', 14),
('Alexander Scott', 'Liam', 'Male', '789 Walnut Boulevard', '555-234-5678', 15),
('Sophia Young', 'Emily', 'Female', '123 Poplar Road', '555-345-6789', 16),
('Benjamin Adams', 'Jack', 'Male', '456 Cypress Circle', '555-456-7890', 17),
('Ella Carter', 'Harper', 'Female', '789 Chestnut Place', '555-567-8901', 18),
('Daniel Perez', 'Oliver', 'Male', '123 Hickory Drive', '555-678-9012', 19),
('Scarlett Bell', 'Layla', 'Female', '456 Redwood Lane', '555-789-0123', 20),
('Elijah Kelly', 'Carter', 'Male', '789 Fir Court', '555-890-1234', 21),
('Chloe Ramirez', 'Aria', 'Female', '123 Ash Way', '555-901-2345', 22),
('Henry Howard', 'Gabriel', 'Male', '456 Beech Road', '555-012-3456', 23),
('Emily Price', 'Hazel', 'Female', '789 Dogwood Lane', '555-123-4567', 24),
('Mason Ward', 'Nathan', 'Male', '123 Olive Court', '555-234-5678', 25),
('Amelia Fisher', 'Anna', 'Female', '456 Acacia Street', '555-345-6789', 26),
('Lucas Brooks', 'Aiden', 'Male', '789 Willow Walk', '555-456-7890', 27),
('Sophia Bell', 'Stella', 'Female', '123 Sequoia Drive', '555-567-8901', 28),
('Logan Flores', 'Ethan', 'Male', '456 Maplewood Lane', '555-678-9012', 29),
('Ava Rogers', 'Emma', 'Female', '789 Redwood Boulevard', '555-789-0123', 30),
('Noah Walker', 'Levi', 'Male', '123 Elm Avenue', '555-890-1234', 31),
('Mia Simmons', 'Scarlett', 'Female', '456 Sycamore Place', '555-901-2345', 32),
('Oliver Mitchell', 'Benjamin', 'Male', '789 Aspen Court', '555-012-3456', 33),
('Sophia Evans', 'Sophia', 'Female', '123 Oakwood Street', '555-123-4567', 34),
('James Turner', 'Caleb', 'Male', '456 Cedar Avenue', '555-234-5678', 35),
('Chloe Foster', 'Chloe', 'Female', '789 Magnolia Road', '555-345-6789', 36),
('Henry Parker', 'Henry', 'Male', '123 Linden Street', '555-456-7890', 37),
('Liam Ross', 'Logan', 'Male', '456 Aspen Way', '555-567-8901', 38),
('Emily Watson', 'Aria', 'Female', '789 Pinewood Road', '555-678-9012', 39),
('Ethan Peterson', 'Ethan', 'Male', '123 Birch Court', '555-789-0123', 40),
('Olivia Bryant', 'Amelia', 'Female', '456 Willow Drive', '555-890-1234', 41),
('Mason Edwards', 'Mason', 'Male', '789 Maple Circle', '555-901-2345', 42),
('Scarlett Bailey', 'Ella', 'Female', '123 Chestnut Street', '555-012-3456', 43),
('Daniel Cooper', 'Daniel', 'Male', '456 Redwood Court', '555-123-4567', 44),
('Emma Ramirez', 'Layla', 'Female', '789 Sequoia Road', '555-234-5678', 45),
('Benjamin Kelly', 'Aiden', 'Male', '123 Birchwood Boulevard', '555-345-6789', 46),
('Sophia Price', 'Scarlett', 'Female', '456 Maple Lane', '555-456-7890', 47),
('Logan Foster', 'Logan', 'Male', '789 Cedar Court', '555-567-8901', 48),
('Liam Young', 'Liam', 'Male', '123 Oak Street', '555-678-9012', 49),
('Mia Jenkins', 'Mia', 'Female', '456 Pine Avenue', '555-789-0123', 50),
('Alice Brown', 'John', 'Female', '789 Pine Road', '555-1234', 1),
('Bob White', 'William', 'Male', '101 Maple Drive', '555-5678', 1),
('Charlie Green', 'David', 'Male', '202 Oak Avenue', '555-8765', 2),
('David Black', 'Thomas', 'Male', '303 Elm Street', '555-4321', 2),
('Eve Blue', 'Sarah', 'Female', '404 Birch Road', '555-1122', 3),
('Frank Red', 'Daniel', 'Male', '505 Cedar Street', '555-3344', 3);
"""

insert_staff_data = """
INSERT INTO Staff (Name, Dept, Gender, Address, CellNum, dr_code) VALUES
('John Carter', 'Administration', 'Male', '123 Elm Street', '555-101-2345', 1),
('Emma Watson', 'Nursing', 'Female', '456 Oak Avenue', '555-102-3456', 2),
('Liam Brown', 'Radiology', 'Male', '789 Pine Road', '555-103-4567', 3),
('Sophia Taylor', 'Pharmacy', 'Female', '321 Pine Avenue', '555-104-5678', 7),
('Mason Lee', 'Laboratory', 'Male', '567 Willow Street', '555-105-6789', 8),
('Isabella Clark', 'Surgery', 'Female', '789 Oak Lane', '555-106-7890', 9),
('Ethan Walker', 'Physiotherapy', 'Male', '123 Cedar Boulevard', '555-107-8901', 10);

"""

insert_diagnosis_data = """
INSERT INTO PatientDiagnosis (DiagDetails, Remark, DiagDate, Other, pat_id) VALUES
('Hypertension', 'Blood pressure under control', '2024-10-01', 'Lifestyle modifications advised', 51),
('Diabetes Mellitus', 'Insulin dose adjusted', '2024-10-02', 'Routine follow-up', 52),
('Pneumonia', 'Antibiotics completed', '2024-10-03', 'Chest X-ray clear', 53),
('Migraine', 'Reduced frequency of episodes', '2024-10-04', 'Prescribed preventive medication', 54),
('Asthma', 'Symptoms stable', '2024-10-05', 'Peak flow readings normal', 55),
('Anemia', 'Hb levels improving', '2024-10-06', 'Iron supplements continued', 56),
('UTI', 'Treatment successful', '2024-10-07', 'No further symptoms', 57),
('Fracture Healing', 'Bone healing on track', '2024-10-08', 'X-ray review satisfactory', 58),
('Thyroid Disorder', 'Medication adjusted', '2024-10-09', 'TSH within normal limits', 59),
('Obesity', 'Weight loss plan initiated', '2024-10-10', 'Dietary counseling provided', 60),
('Hypertension', 'Medication compliance good', '2024-10-11', 'No complications', 61),
('Allergic Rhinitis', 'Symptoms controlled', '2024-10-12', 'Advised allergen avoidance', 62),
('Depression', 'Therapy sessions ongoing', '2024-10-13', 'CBT sessions weekly', 63),
('Osteoarthritis', 'Pain management effective', '2024-10-14', 'Advised physiotherapy', 64),
('Gastritis', 'Symptoms improved', '2024-10-15', 'Dietary modifications advised', 65),
('Hypertension', 'BP under control', '2024-10-16', 'Routine monitoring', 66),
('Type 1 Diabetes', 'HbA1c improved', '2024-10-17', 'Insulin regimen adjusted', 67),
('Chronic Sinusitis', 'No active infection', '2024-10-18', 'Maintenance therapy started', 68),
('Bronchitis', 'Resolved with treatment', '2024-10-19', 'Advised smoking cessation', 69),
('Hypothyroidism', 'Euthyroid state achieved', '2024-10-20', 'Medication continued', 70),
('Anxiety Disorder', 'Therapy initiated', '2024-10-21', 'Progressing well', 71),
('Hypertension', 'Stable BP readings', '2024-10-22', 'Lifestyle changes effective', 72),
('Back Pain', 'Pain reduced with therapy', '2024-10-23', 'Advised posture correction', 73),
('Flu', 'Recovered fully', '2024-10-24', 'No complications', 74),
('GERD', 'Symptoms managed', '2024-10-25', 'PPI therapy continued', 75),
('Chronic Kidney Disease', 'Function stable', '2024-10-26', 'Routine nephrology follow-up', 76),
('Iron Deficiency Anemia', 'Treatment ongoing', '2024-10-27', 'Dietary advice provided', 77),
('Skin Allergy', 'Symptoms resolved', '2024-10-28', 'Advised skin patch testing', 78),
('Hypertension', 'Controlled with medication', '2024-10-29', 'Regular follow-up advised', 79),
('Diabetes', 'Blood sugar stable', '2024-10-30', 'Routine monitoring', 80),
('Pneumonia', 'Antibiotic course completed', '2024-10-31', 'Chest clear on X-ray', 81),
('Asthma', 'Controlled with inhalers', '2024-11-01', 'Peak flow readings satisfactory', 82),
('Migraine', 'Frequency reduced', '2024-11-02', 'Preventive therapy effective', 83),
('Obesity', 'Lifestyle changes initiated', '2024-11-03', 'Diet plan reviewed', 84),
('Hypertension', 'Routine follow-up', '2024-11-04', 'No complications', 85),
('Sinusitis', 'Treatment completed', '2024-11-05', 'No active symptoms', 86),
('Thyroid Dysfunction', 'TSH stable', '2024-11-06', 'Medication dosage unchanged', 87),
('Anemia', 'Iron levels improving', '2024-11-07', 'Supplements continued', 88),
('Depression', 'Therapy effective', '2024-11-08', 'Progress monitored', 89),
('Bronchitis', 'Recovered fully', '2024-11-09', 'No residual symptoms', 90),
('UTI', 'Treated successfully', '2024-11-10', 'Urine culture negative', 91),
('GERD', 'Symptoms resolved', '2024-11-11', 'Dietary advice reinforced', 92),
('Back Pain', 'Pain-free', '2024-11-12', 'Therapy completed', 93),
('Gastritis', 'Improved with treatment', '2024-11-13', 'Maintenance therapy advised', 94),
('Hypertension', 'BP well-controlled', '2024-11-14', 'Medication continued', 95),
('Diabetes', 'Stable glucose levels', '2024-11-15', 'Routine monitoring', 96),
('Asthma', 'Stable symptoms', '2024-11-16', 'Advised regular monitoring', 97);

"""

insert_bill_data = """
INSERT INTO Bill (PatName, DrName, Datetime, Amount, pat_id) 
VALUES 
    ('Alice Brown', 'John Doe', '2024-11-25 10:30:00', 150.50, 51),
    ('Charlie Green', 'Jane Smith', '2024-11-25 11:00:00', 200.00, 52),
    ('Daisy White', 'Sam Brown', '2024-11-24 15:45:00', 180.75, 53),
    ('Ethan Black', 'Alice Johnson', '2024-11-23 09:15:00', 220.10, 54),
    ('Fiona Blue', 'Michael Davis', '2024-11-22 14:30:00', 175.25, 55),
    ('George Gray', 'Emily White', '2024-11-21 16:00:00', 190.00, 56),
    ('Hannah Red', 'Chris Green', '2024-11-20 12:45:00', 210.30, 57),
    ('Ian Orange', 'Olivia Wilson', '2024-11-19 10:00:00', 160.80, 58),
    ('Jenny Pink', 'Liam Thomas', '2024-11-18 11:15:00', 205.60, 59),
    ('Kyle Yellow', 'Sophia Martinez', '2024-11-17 13:45:00', 195.90, 60);
"""

# Execute the DML statements to insert sample data
my_cursor.execute(insert_doctor_data)
my_cursor.execute(insert_patient_data)
my_cursor.execute(insert_staff_data)
my_cursor.execute(insert_diagnosis_data)
my_cursor.execute(insert_bill_data)

my_connection.commit()
print("Data has been inserted successfully!")
