import streamlit as st
import mysql.connector
import pandas as pd

# Database connection details
DB_HOST = "shortline.proxy.rlwy.net"
DB_USER = "root"
DB_PASSWORD = "HJbJWZljtPCVElopHxCknoeDLcjsbxDk"
DB_NAME = "railway"
DB_PORT = 44228

# Connect to Railway MySQL
def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

# Fetch all students
def get_students():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students

# Streamlit App UI
st.title("🎓 Student Data Management System")

# Fetch and display student data
students = get_students()
df = pd.DataFrame(students)

if not df.empty:
    st.write("## 📋 Student List")
    st.dataframe(df)

    # Bar chart visualization of nationalities
    nationality_counts = df["nationality"].value_counts()
    st.write("### 🌍 Students by Nationality")
    st.bar_chart(nationality_counts)
else:
    st.warning("⚠ No students found in the database.")
