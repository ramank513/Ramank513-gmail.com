from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []  # in-memory list to hold tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added", "task": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
