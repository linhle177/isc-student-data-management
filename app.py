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

def get_table_data(query, params=None):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    data = cursor.fetchall()
    conn.close()
    return pd.DataFrame(data)

st.title("🎓 Student Data Management System")

# Fetch all students
students_df = get_table_data("SELECT * FROM Students")

# Show each student in an expandable section
for _, student in students_df.iterrows():
    with st.expander(f"📌 {student['full_name']} - {student['nationality']}"):
        st.write(f"📅 **Date of Birth:** {student['dob']}")
        st.write(f"📧 **Email:** {student['email']}")
        st.write(f"📞 **Phone:** {student['phone']}")
        st.write(f"🏠 **Address:** {student['address']}")

        # Education Info
        edu_df = get_table_data("SELECT * FROM Education WHERE student_id=%s", (student["student_id"],))
        if not edu_df.empty:
            st.write("🎓 **Education Information**")
            st.dataframe(edu_df.style.set_properties(**{'text-align': 'left'}))

        # Application Status
        app_df = get_table_data("SELECT * FROM ApplicationStatus WHERE student_id=%s", (student["student_id"],))
        if not app_df.empty:
            st.write("📌 **Application Status**")
            st.dataframe(app_df.style.set_properties(**{'text-align': 'left'}))

        # Consultation Notes
        consult_df = get_table_data("SELECT * FROM Consultation WHERE student_id=%s", (student["student_id"],))
        if not consult_df.empty:
            st.write("📅 **Consultation & Follow-ups**")
            st.dataframe(consult_df.style.set_properties(**{'text-align': 'left'}))

st.success("✅ Data loaded successfully!")
