from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model użytkownika
class User(BaseModel):
    id: int
    name: str
    email: str

# Pseudo-baza danych użytkowników
users_database = [
    User(id=1, name="Omik Futerkowski", email="omik.futerkowski@poczta.pl"),
    User(id=2, name="Lomik Bobkowski", email="lomik.bobek@poczta.pl"),
    User(id=3, name="Omiur Zorro", email="omiurro@poczta.pl")
]

@app.get("/")
def read_root():
    return { "/users; /users/{id}"
            }

# Zwraca listę użytkowników
@app.get("/users", response_model=List[User])
def get_users():
    return users_database

# Zwraca szczegóły po id użytkownika
@app.get("/users/{id}", response_model=User)
def get_user(id: int):
    for user in users_database:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Pozwala na dodanie nowego użytkownika
@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    if any(u.id == user.id for u in users_database):
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_database.append(user)
    return user