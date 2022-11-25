import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database
database = client.books

# collection
book_collection = database.get_collection("books_collection")

def book_helper(book):
    return{
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
    }

# crud operations 
#retrieve all books
async def retrieve_books():
    books = []
    async for book in book_collection.find():
        books.append(book_helper(book))
    return books


#retrieve an books with a matching id
async def retrieve_book(id: str):
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)