from typing import Optional
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(... , max_length=100) 
    author : str = Field(... , max_length=100) 

    class Config:
        schema_extra = {
            "example": {
                "title": "Zanna bianca",
                "author": "Jack London"
            }
        }

class UpdateBookModel(BaseModel):
    title: Optional[str] = Field(max_length=100)
    author: Optional[str] = Field(max_length=100)

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


