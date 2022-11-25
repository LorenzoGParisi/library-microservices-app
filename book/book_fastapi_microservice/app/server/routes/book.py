from fastapi import APIRouter, Body, Response, status
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_books,
    retrieve_book,
    add_book,
    update_book,
    delete_book
)

from server.models.book import (
    BookSchema,
    UpdateBookModel,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()