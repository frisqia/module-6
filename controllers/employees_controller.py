from flask import jsonify, request
from db import employees

def get_employees():
    return jsonify({"employees": employees})

def get_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

def create_employee():
    try:
        data = request.get_json()
        validate_employee_data(data)
        
        new_id = len(employees) + 1
        new_employee = {
            "id": new_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "role": data['role'],
            "schedule": data['schedule']
        }
        employees.append(new_employee)
        return jsonify({"message": "Successfully created a new employee"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def update_employee(id):
    try:
        data = request.get_json()
        employee_to_update = next((e for e in employees if e['id'] == id), None)
        if employee_to_update:
            validate_employee_data(data)
            employee_to_update.update(data)
            return jsonify({"message": "Employee updated successfully"}), 200
        else:
            return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def delete_employee(id):
    global employees
    employees = [e for e in employees if e['id'] != id]
    return jsonify({"message": "Employee deleted successfully"}), 200

def validate_employee_data(data):
    required_fields = ['name', 'email', 'phone', 'role', 'schedule']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the employee")