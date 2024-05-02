from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "John Doe", "age": 20, "major": "Computer Science"},
    {"id": 2, "name": "Jane Smith", "age": 21, "major": "Physics"},
    {"id": 3, "name": "Alice Johnson", "age": 22, "major": "Mathematics"}
]

# Endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Endpoint to get a specific student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"message": "Student not found"}), 404

# Endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    if 'name' not in new_student or 'age' not in new_student or 'major' not in new_student:
        return jsonify({"message": "Missing data"}), 400

    new_student['id'] = len(students) + 1
    students.append(new_student)
    return jsonify({"message": "Student added successfully", "student": new_student}), 201

# Endpoint to update an existing student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    update_data = request.json
    student.update(update_data)
    return jsonify({"message": "Student updated successfully", "student": student})

# Endpoint to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
