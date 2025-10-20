from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Вивчити Python та Flask", "completed": False},
    {"id": 2, "title": "Написати тести з pytest", "completed": False},
]
next_id = 3

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    return jsonify(task) if task else (jsonify({"message": "Завдання не знайдено"}), 404)

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"message": "Назва завдання є обов'язковою"}), 400
    new_task = {"id": next_id, "title": data['title'], "completed": False}
    tasks.append(new_task)
    next_id += 1
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Завдання не знайдено"}), 404
    data = request.get_json()
    task.update(data)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task_exists = any(t for t in tasks if t["id"] == task_id)
    if not task_exists:
        return jsonify({"message": "Завдання не знайдено"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)