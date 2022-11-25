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