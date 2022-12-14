import motor.motor_asyncio
import pymongo
from bson.objectid import ObjectId
from server.utilities. utilities import dict_lowerCase

MONGO_DETAILS = "mongodb://localhost:27017"
# stringa di connessione per il container di mongo. example-mongo e' il nome del container
# MONGO_DETAILS = "mongodb://example-mongo:27017"
clientMotor = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, serverSelectionTimeoutMS=5000)
database = clientMotor.book
book_collection = database.get_collection("books_collection")

def book_helper(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
    }


index = book_collection.create_index(
    [("title", pymongo.ASCENDING), ("author", pymongo.ASCENDING)],
    unique = True
)


# retrieve all books
async def retrieve_books():
    books = []
    async for book in book_collection.find():
        books.append(book_helper(book))
    return books


# retrieve books by id
async def retrieve_book(id: str):
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)


# create book
async def add_book(book_data: dict):
    dict_lowerCase(book_data)
    if book_data:
            book = await book_collection.insert_one(book_data)
            print('sono qui')
            if book:
                new_book = await book_collection.find_one({"_id": book.inserted_id})
                return book_helper(new_book)
            return False


# update book
async def update_book(id: str, data: dict):
    if len(data)<1:
        return False
    dict_lowerCase(data)

    book = await book_collection.find_one({"_id": ObjectId(id)})
    print(book)
    if book:
        updated_book = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return data
        return False


# delete a book
async def delete_book(id:str):
    book = await book_collection.find_one({"_id":ObjectId(id)})
    if book:
        await book_collection.delete_one({"_id": ObjectId(id)})
        return True



