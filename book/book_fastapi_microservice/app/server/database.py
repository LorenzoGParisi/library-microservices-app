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

#create an book
async def add_book(book_data: dict ):
    book = await book_collection.insert_one(book_data)
    new_book = await book_collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)


async def update_book(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False