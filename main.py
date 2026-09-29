from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List
import sqlite3

app = FastAPI()

# Connect to SQLite database
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY, name TEXT, position TEXT)''')

# 1. Read all employees
@app.get('/employees', response_model=List[Employee])
def get_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    return [Employee(*row) for row in rows]


# 2. Read specific employee
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id: int):
    cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
    row = cursor.fetchone()
    if row:
        return Employee(*row)
    raise HTTPException(status_code=404, detail='Employee Not Found')


# 3. Add an employee
@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    cursor.execute('''
        INSERT INTO employees (id, name, position)
        VALUES (?, ?, ?)
    ''', (new_emp.id, new_emp.name, new_emp.position))
    conn.commit()
    return new_emp


# 4. Update an employee
@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    cursor.execute('''
        UPDATE employees SET name = ?, position = ?
        WHERE id = ?
    ''', (updated_employee.name, updated_employee.position, emp_id))
    conn.commit()
    return updated_employee


# 5. Delete an employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int):
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()
    return {'message': 'Employee deleted successfully'}


# Close the database connection when the application exits
import atexit

@atexit.register
def close_connection():
    if conn:
        conn.close()
