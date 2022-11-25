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


@router.get("/")
async def get_books(response: Response):
    books = await retrieve_books()
    if books:
        response.status_code = status.HTTP_200_OK
        return ResponseModel(books)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Book doesn't exist.")


@router.post("/")
async def add_books(response: Response,book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    if new_book:
        response.status_code = status.HTTP_201_CREATED
        return ResponseModel(new_book)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Book doesn't exist.")