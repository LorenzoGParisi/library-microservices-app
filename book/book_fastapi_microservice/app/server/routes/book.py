from bson import ObjectId
from fastapi import APIRouter, Response, status, Body
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
    UpdateBookSchema,
    RespondeModel,
    ErrorRespondeModel
)

router = APIRouter()
@router.get("/")
async def get_books(response: Response):
    try:
        books = await retrieve_books()
        if not books:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorRespondeModel("book doesn't exist")
        response.status_code = status.HTTP_200_OK
        return RespondeModel(books)
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorRespondeModel("something doesnt work")


@router.get("/{id}")
async def get_book(id: str,response: Response):
    try:
        if ObjectId.is_valid(id):
            book = await retrieve_book(id)
            if not book:
                response.status_code = status.HTTP_404_NOT_FOUND
                return ErrorRespondeModel("id doensn't match")
            response.status_code = status.HTTP_200_OK
            return RespondeModel(book)
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorRespondeModel("not valid id")
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorRespondeModel("something doesnt work")

@router.post("/")
async def add_books(response: Response, book_body: BookSchema = Body(...)):
    try:
        book = jsonable_encoder(book_body)

        print(book)
        new_book = await add_book(book)
        if not new_book:
        # if not await add_book(book):
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorRespondeModel("Book already exists")
        response.status_code = status.HTTP_201_CREATED
        print('sono qui')
        return RespondeModel(new_book)
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorRespondeModel("something goes wrong")

@router.put("/{id}")
async def update_book_data(response: Response, id: str, req: UpdateBookSchema = Body(...)):
    try:
        if ObjectId.is_valid(id):
            req = {k: v for k, v in req.dict().items() if v is not None}
            updated_book = await update_book(id, req)
            if not updated_book:
                response.status_code = status.HTTP_404_NOT_FOUND
                return ErrorRespondeModel("id doensn't match")
            response.status_code = status.HTTP_200_OK
            return RespondeModel(updated_book)
        else:
                response.status_code = status.HTTP_404_NOT_FOUND
                return ErrorRespondeModel("not valid id")
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorRespondeModel("something doesnt work")

@router.delete("/{id}")
async def delete_book_data(response:Response, id: str):
    try:
        if ObjectId.is_valid(id):
            deleted_book = await delete_book(id)
            if not deleted_book:
                response.status_code = status.HTTP_404_NOT_FOUND
                return ErrorRespondeModel("id doensn't match")
            response.status_code = status.HTTP_200_OK
            return RespondeModel(f"Book with {id} is deleted")
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorRespondeModel("not valid id")
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorRespondeModel("something doesnt work")

