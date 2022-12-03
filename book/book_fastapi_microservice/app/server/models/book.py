from typing import Optional, Union
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(... , max_length=100,) 
    author : str = Field(... , max_length=100,) 

    class Config:
        schema_extra = {
            "example": {
                "title": "Zanna bianca",
                "author": "Jack London"
            }
        }

class UpdateBookModel(BaseModel):

    title: Union [str, None]=  Field(max_length=100)
    author: Union [str, None]=  Field(max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "example": "example",
            }
        }

def ResponseModel(data):
    return {
        "data":[data]
    }

def ErrorResponseModel(message):
    return {"message": message}


