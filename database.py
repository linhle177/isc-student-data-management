import mysql.connector

DB_HOST = "shortline.proxy.rlwy.net"
DB_USER = "root"
DB_PASSWORD = "HJbJWZljtPCVElopHxCknoeDLcjsbxDk"
DB_NAME = "railway"
DB_PORT = 44228

def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

import mysql.connector

DB_HOST = "shortline.proxy.rlwy.net"
DB_USER = "root"
DB_PASSWORD = "HJbJWZljtPCVElopHxCknoeDLcjsbxDk"
DB_NAME = "railway"
DB_PORT = 44228

def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Students Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        dob DATE,
        nationality VARCHAR(100),
        email VARCHAR(255) UNIQUE,
        phone VARCHAR(20),
        address TEXT
    )
    """)

    # Create Education Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Education (
        edu_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        high_school VARCHAR(255),
        grad_year INT,
        study_destination VARCHAR(100),
        preferred_major VARCHAR(255),
        ielts_score DECIMAL(3,1),
        toefl_score INT,
        FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
    )
    """)

    # Create Application Status Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ApplicationStatus (
        app_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        status ENUM('Pending', 'Approved', 'Rejected'),
        university_name VARCHAR(255),
        tuition_fees DECIMAL(10,2),
        scholarship_status ENUM('Yes', 'No'),
        visa_status ENUM('Pending', 'Approved', 'Rejected'),
        FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
    )
    """)

    # Create Consultation & Follow-ups Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Consultation (
        consultation_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        consultant_name VARCHAR(255),
        meeting_notes TEXT,
        follow_up_date DATE,
        FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
    print("✅ All tables created successfully!")

if __name__ == "__main__":
    create_tables()
def insert_sample_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Insert into Students
    cursor.execute("""
    INSERT INTO Students (full_name, dob, nationality, email, phone, address)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, ("Nguyen Van B", "2002-10-15", "Vietnamese", "nguyenvanb@example.com", "0912345678", "Ho Chi Minh, Vietnam"))

    student_id = cursor.lastrowid  # Get the inserted student's ID

    # Insert into Education
    cursor.execute("""
    INSERT INTO Education (student_id, high_school, grad_year, study_destination, preferred_major, ielts_score, toefl_score)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (student_id, "ABC High School", 2021, "USA", "Computer Science", 7.5, 95))

    # Insert into Application Status
    cursor.execute("""
    INSERT INTO ApplicationStatus (student_id, status, university_name, tuition_fees, scholarship_status, visa_status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (student_id, "Pending", "MIT", 50000, "Yes", "Pending"))

    # Insert into Consultation
    cursor.execute("""
    INSERT INTO Consultation (student_id, consultant_name, meeting_notes, follow_up_date)
    VALUES (%s, %s, %s, %s)
    """, (student_id, "Ms. Linh", "Discussed financial aid options", "2025-03-01"))

    conn.commit()
    conn.close()
    print("✅ Sample data inserted successfully!")

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
