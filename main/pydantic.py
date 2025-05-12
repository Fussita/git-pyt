
import time
import json
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from pydantic import BaseModel
from pydantic import ValidationError
from enum import Enum
from typing import List

class Comment(BaseModel):
    text: str | None = None

class Blog(BaseModel):
    comment: List[Comment] | None
    created_at: datetime = Field(default_factory=datetime.now)
    name: str = Field(...,min_length=5) #Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    age: int = Field(..., le=60, ge=18) # MENOR A 60 , MAYOR A 18
    # gt=0 , Debe ser estrictamente mayor a 0

    @field_validator('date')
    def validar_fechas(cls, v):
        if v.fecha_fin <= v.fecha_inicio:
            raise ValueError("La fecha de fin debe ser posterior a la de inicio")
        return v

    @field_validator('name')
    def name_must_contain_uppercase(cls, v):
        if not any(x.isupper() for x in v):
            raise ValueError('name must have at least one uppercase letter')
        return v

my_blog = Blog(title="Our First Blog",comment=[{'text':'My comment'},{'text':'Your comment'},])

# SERIALIZAR EL OBJETO A DICCIONARIO bg_dict = bg.model_dump()
# SERIELIZAR EL OBJETO A JSON userjson = json.dumps(bg_dict)
# DESERIALIZAR UN DICC A UN OBJ
bg_data = {}
new_user = Blog.model_validate(bg_data)

class Languages(str,Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

external_data = {
    'id': 123,
    'signup_ts': '2024-10-09 12:22',
    'friends': [1, '2', b'3'],
}

try:
    blog = Blog(**external_data)
    # blog.id
    # print(blog.model_dump_json())
except ValidationError as e:
    print(e.errors())

