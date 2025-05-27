
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

class UserModel(BaseModel):
    id: int = Field(..., ge=18, le=100) 
    name: str = Field(min_length=6)
    user: str = Field(min_length=6)
    password: str = Field(min_length=6)
    email: EmailStr = Field(min_length=6)
 
app = FastAPI()
users: list[UserModel] = []

@app.get('/')
def root():
    return f'Bienvenido API'

@app.get('/users', response_model=list[UserModel])
def getUsers():
    return users

@app.post('/create')
def createUser( user: UserModel ):
    users.append(user)

@app.get("/users/{id}", response_model=UserModel)
# UNION[UserModel, str]
def getUser(id: int):
    for i in users:
        if (i.id == id):
            return i
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
