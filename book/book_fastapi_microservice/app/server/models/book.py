from typing import List,Union
from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    title : str = Field(... , max_length=100)
    author : Union[str, List] = Field(... , max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "title": "zanna bianca",
                "author": "jack london"
            }
        }

class UpdateBookSchema(BaseModel):
    title : Union[str,None] = Field(max_length=100)
    author : Union[str, List, None] = Field(max_length=100)

    class Config:
        schema_exra = {
            "example": {
                "title": "anna karenina",
                "author": "tolstoj"
            }
        }

def RespondeModel(data):
    return {
        "data": [data]
    }

def ErrorRespondeModel(message):
    return {
        "message": message
    }