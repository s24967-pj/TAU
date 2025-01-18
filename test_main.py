from fastapi.testclient import TestClient
from main import app, users_database 

client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == len(users_database)

def test_get_user_by_id():
    # TEST istniejacy użytkownik
    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Omik Futerkowski"
    assert user["email"] == "omik.futerkowski@poczta.pl"

    # TEST nieistniejący uzytkownik
    response = client.get("/users/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_create_user():
    new_user = {"id": 100, "name": "Test nowy user", "email": "nowyuser@poczta.pl"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user == new_user

    # TEST czy użytkownik został doddany
    response = client.get("/users/100")
    assert response.status_code == 200
    assert response.json() == new_user

def test_update_user():
    updated_user = {"id": 1, "name": "Zaktualizowany Omik", "email": "omik.updated@poczta.pl"}
    response = client.put("/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json() == updated_user

    # TEST czy zmiana została zapisana
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == updated_user

    # TEST aktualizacji nieistniejącego użytkownika
    updated_user_nonexistent = {"id": 99, "name": "Nieistniejący user", "email": "nieistnieje@poczta.pl"}
    response = client.put("/users/99", json=updated_user_nonexistent)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204

    # TEST odczytu usuniętego użytkownika
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

    # TEST usunięcia nieistniejącego uzytkownika
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
