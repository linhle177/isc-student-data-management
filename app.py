import streamlit as st
import mysql.connector
import pandas as pd

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

def get_table_data(table_name):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return pd.DataFrame(data)

# Streamlit App UI
st.title("🎓 Student Data Management System")

# Display Students Table
st.write("## 📝 Students List")
students_df = get_table_data("Students")
st.dataframe(students_df)

# Display Education Table
st.write("## 📚 Education Information")
education_df = get_table_data("Education")
st.dataframe(education_df)

# Display Application Status Table
st.write("## 📌 Application Status")
application_df = get_table_data("ApplicationStatus")
st.dataframe(application_df)

# Display Consultation & Follow-ups Table
st.write("## 📅 Consultations & Follow-ups")
consultation_df = get_table_data("Consultation")
st.dataframe(consultation_df)
