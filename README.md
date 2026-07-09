# Hospital Management System

A simple command-line Hospital Management System built using Python and MySQL. This project allows users to manage patient appointments by adding, viewing, searching, updating, and deleting appointment records stored in a MySQL database.

## Features

- Add new patient appointments
- View all scheduled appointments
- Search appointments by patient name
- Update existing appointment details
- Delete appointments
- Persistent data storage using MySQL database

## Technologies Used

- Python
- MySQL
- MySQL Connector/Python

```
```
## Database Setup

Before running the program, create a MySQL database:

```sql
CREATE DATABASE hospital_db;
```

The program will automatically create the required `appointments` table when executed.

The table contains the following fields:

| Field | Description |
|---|---|
| id | Unique appointment ID |
| name | Patient name |
| date | Appointment date |
| time | Appointment time |
| doctor | Doctor's name |
| dept | Department name |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rakzeep/Hosp-management.git
```

### 2. Install required dependencies

Install the MySQL connector package:

```bash
pip install mysql-connector-python
```

### 3. Configure MySQL Connection

Update the database connection details in the Python file:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="hospital_db"
)
```

Replace:

- `yourpassword` with your MySQL password
- Database details according to your local setup

## Running the Project

Run the Python file:

```bash
python hospital_management.py
```

The program will display a menu:

```
=== Hospital Management System (MySQL Version) ===

1. Add Appointment
2. View Appointments
3. Search Appointment
4. Update Appointment
5. Delete Appointment
6. Exit
```

## How It Works

The application connects Python with a MySQL database to store and manage appointment records.

- The user interacts with the command-line interface.
- Python functions handle different operations.
- SQL queries are executed through MySQL Connector.
- Changes are committed to the database after every operation.

## Future Improvements

Possible enhancements for this project:

- Add patient login and authentication
- Add doctor management system
- Add appointment availability checking
- Create a graphical user interface (GUI)
- Add data validation for dates and times
- Generate appointment reports
