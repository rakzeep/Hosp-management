import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="yourpassword",  
    database="hospital_db"    
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    date VARCHAR(20),
    time VARCHAR(10),
    doctor VARCHAR(100),
    dept VARCHAR(100)
)
""")
conn.commit()

def add_appointment():
    print("\n--- Add Appointment ---")
    name = input("Enter patient name: ")
    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time (HH:MM): ")
    doctor = input("Enter doctor's name: ")
    dept = input("Enter department: ")

    sql = "INSERT INTO appointments (name, date, time, doctor, dept) VALUES (%s, %s, %s, %s, %s)"
    val = (name, date, time, doctor, dept)
    cursor.execute(sql, val)
    conn.commit()
    print("Appointment added successfully!\n")

def view_appointments():
    print("\n--- All Appointments ---")
    cursor.execute("SELECT * FROM appointments")
    records = cursor.fetchall()
    if not records:
        print("No records found.\n")
    else:
        for row in records:
            print(f"ID: {row[0]} | Patient: {row[1]} | Date: {row[2]} | Time: {row[3]} | Doctor: {row[4]} | Dept: {row[5]}")
    print()
     
def search_appointment():
    print("\n--- Search Appointment ---")
    search_name = input("Enter patient name to search: ").strip()
    sql = "SELECT * FROM appointments WHERE name = %s"
    cursor.execute(sql, (search_name,))
    records = cursor.fetchall()
    if records:
        for row in records:
            print(f"Patient: {row[1]} | Date: {row[2]} | Time: {row[3]} | Doctor: {row[4]} | Dept: {row[5]}")
    else:
        print("No appointment found for", search_name, "\n")

def update_appointment():
    print("\n--- Update Appointment ---")
    search_name = input("Enter patient name to update: ").strip()
    cursor.execute("SELECT * FROM appointments WHERE name = %s", (search_name,))
    record = cursor.fetchone()

    if record:
        print("\nCurrent Details:")
        print(f"Patient: {record[1]} | Date: {record[2]} | Time: {record[3]} | Doctor: {record[4]} | Dept: {record[5]}")
        print("\nEnter new details (press Enter to keep unchanged):")

        new_date = input("New appointment date (DD-MM-YYYY): ") or record[2]
        new_time = input("New appointment time (HH:MM): ") or record[3]
        new_doctor = input("New doctor's name: ") or record[4]
        new_dept = input("New department: ") or record[5]

        sql = "UPDATE appointments SET date=%s, time=%s, doctor=%s, dept=%s WHERE name=%s"
        cursor.execute(sql, (new_date, new_time, new_doctor, new_dept, search_name))
        conn.commit()
        print("Appointment updated successfully!\n")
    else:
        print("No appointment found for", search_name, "\n")

def delete_appointment():
    print("\n--- Delete Appointment ---")
    search_name = input("Enter patient name to delete: ").strip()
    cursor.execute("SELECT * FROM appointments WHERE name = %s", (search_name,))
    record = cursor.fetchone()

    if record:
        cursor.execute("DELETE FROM appointments WHERE name = %s", (search_name,))
        conn.commit()
        print("Appointment deleted successfully!\n")
    else:
        print("No appointment found for", search_name, "\n")

def main():
    while True:
        print("\n=== Hospital Management System (MySQL Version) ===")
        print("1. Add Appointment")
        print("2. View Appointments")
        print("3. Search Appointment")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            add_appointment()
        elif ch == "2":
            view_appointments()
        elif ch == "3":
            search_appointment()
        elif ch == "4":
            update_appointment()
        elif ch == "5":
            delete_appointment()
        elif ch == "6":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice! Please try again.\n")

    cursor.close()
    conn.close()

main()
