from fastapi import APIRouter, Body, Response, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

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

    if ObjectId.is_valid(id):
        book = await retrieve_book(id)
        if book:
            response.status_code = status.HTTP_200_OK
            return ResponseModel(book)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Id doesn't match.")


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

@router.put("/{id}")
async def update_book_data(response: Response,id: str, req: UpdateBookModel = Body(...)):
    if ObjectId.is_valid(id):
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_book = await update_book(id, req)
        if updated_book:
            response.status_code = status.HTTP_200_OK
            return ResponseModel(updated_book)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Id doesn't match.")


@router.delete("/{id}")
async def delete_book_data(response: Response,id: str):
    deleted_book= await delete_book(id)
    if deleted_book:
        response.status_code = status.HTTP_200_OK
        # return f"Book with {id} is deleted"
        return ResponseModel(f"Book with {id} is deleted")
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponseModel("Book doesn't exist.")