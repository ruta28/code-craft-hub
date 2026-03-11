from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "courses.json"

# Allowed status values
VALID_STATUS = ["Not Started", "In Progress", "Completed"]


# ---------------------------------------------------
# Ensure JSON file exists
# ---------------------------------------------------
def initialize_file():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([], file)
        except Exception as e:
            print("Error creating file:", e)


# ---------------------------------------------------
# Read courses from JSON file
# ---------------------------------------------------
def read_courses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return None


# ---------------------------------------------------
# Write courses to JSON file
# ---------------------------------------------------
def write_courses(courses):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(courses, file, indent=4)
        return True
    except Exception:
        return False


# ---------------------------------------------------
# Generate next ID
# ---------------------------------------------------
def generate_id(courses):
    if len(courses) == 0:
        return 1
    return max(course["id"] for course in courses) + 1


# ---------------------------------------------------
# Validate date format
# ---------------------------------------------------
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ---------------------------------------------------
# POST /api/courses
# Add a new course
# ---------------------------------------------------
@app.route("/api/courses", methods=["POST"])
def add_course():

    courses = read_courses()

    if courses is None:
        return jsonify({"error": "File read error"}), 500

    data = request.get_json()

    required_fields = ["name", "description", "target_date", "status"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    if data["status"] not in VALID_STATUS:
        return jsonify({"error": "Invalid status value"}), 400

    if not validate_date(data["target_date"]):
        return jsonify({"error": "Invalid date format (YYYY-MM-DD required)"}), 400

    new_course = {
        "id": generate_id(courses),
        "name": data["name"],
        "description": data["description"],
        "target_date": data["target_date"],
        "status": data["status"],
        "created_at": datetime.now().isoformat()
    }

    courses.append(new_course)

    if not write_courses(courses):
        return jsonify({"error": "File write error"}), 500

    return jsonify(new_course), 201


# ---------------------------------------------------
# GET /api/courses
# Get all courses
# ---------------------------------------------------
@app.route("/api/courses", methods=["GET"])
def get_courses():

    courses = read_courses()

    if courses is None:
        return jsonify({"error": "File read error"}), 500

    return jsonify(courses)


# ---------------------------------------------------
# GET /api/courses/<id>
# Get specific course
# ---------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):

    courses = read_courses()

    if courses is None:
        return jsonify({"error": "File read error"}), 500

    for course in courses:
        if course["id"] == course_id:
            return jsonify(course)

    return jsonify({"error": "Course not found"}), 404


# ---------------------------------------------------
# PUT /api/courses/<id>
# Update a course
# ---------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    courses = read_courses()

    if courses is None:
        return jsonify({"error": "File read error"}), 500

    data = request.get_json()

    for course in courses:

        if course["id"] == course_id:

            if "name" in data:
                course["name"] = data["name"]

            if "description" in data:
                course["description"] = data["description"]

            if "target_date" in data:
                if not validate_date(data["target_date"]):
                    return jsonify({"error": "Invalid date format"}), 400
                course["target_date"] = data["target_date"]

            if "status" in data:
                if data["status"] not in VALID_STATUS:
                    return jsonify({"error": "Invalid status value"}), 400
                course["status"] = data["status"]

            if not write_courses(courses):
                return jsonify({"error": "File write error"}), 500

            return jsonify(course)

    return jsonify({"error": "Course not found"}), 404


# ---------------------------------------------------
# DELETE /api/courses/<id>
# Delete course
# ---------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    courses = read_courses()

    if courses is None:
        return jsonify({"error": "File read error"}), 500

    for course in courses:

        if course["id"] == course_id:

            courses.remove(course)

            if not write_courses(courses):
                return jsonify({"error": "File write error"}), 500

            return jsonify({"message": "Course deleted successfully"})

    return jsonify({"error": "Course not found"}), 404


# ---------------------------------------------------
# Run Flask app
# ---------------------------------------------------
if __name__ == "__main__":

    initialize_file()

    app.run(debug=True)