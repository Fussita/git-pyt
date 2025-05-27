
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Response(BaseModel):
    user: list[User]

listUsers = [
    ["Pedro Perez", 28],
    ["María Rosales", 26],
    ["Juan Martínez", 32],
    ["Ana Gómez", 24],
]

db: list[User] = []

for i in listUsers:
    db.append( User( name=i[0], id=i[1] ) )

app = FastAPI()

@app.get("/usuarios", status_code=status.HTTP_200_OK, response_model=Response)
def obtener_todos():
    return Response(user=db)

@app.get("/usuarios/{user_id}")
def obtener_usuario(user_id: int):
    for i in db:
        if (i.id == user_id):
            return i
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
