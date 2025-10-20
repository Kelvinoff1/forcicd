import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_tasks():
    """Тест для GET /tasks"""
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    """Тест для POST /tasks"""
    new_task = {"title": "Протестувати Python API"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task)
    assert response.status_code == 201
    assert response.json()["title"] == new_task["title"]

def test_delete_task():
    """Тест для DELETE /tasks/:id"""
    # Створюємо завдання, щоб його видалити
    res = requests.post(f"{BASE_URL}/tasks", json={"title": "Temp task"})
    task_id = res.json()["id"]

    # Видаляємо
    delete_res = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert delete_res.status_code == 204

    # Перевіряємо, що воно видалене
    get_res = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert get_res.status_code == 404