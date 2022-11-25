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

@router.get("/{id}")
async def get_book(id: str, response: Response ):
    book = await retrieve_book(id)
    if book:
        response.status_code = status.HTTP_200_OK
        return ResponseModel(book)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Book doesn't exist.")