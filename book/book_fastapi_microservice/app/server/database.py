import motor.motor_asyncio
from bson.objectid import ObjectId
import pymongo


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database
database = client.test

# collection
book_collection = database.get_collection("books_collection")
def book_helper(book):
    return{
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
    }

index = book_collection.create_index(
    [("title", pymongo.ASCENDING), ("author", pymongo.ASCENDING)],
    unique=True
)

#functions
def dict_lowerCase(dict):
    for key in dict:
        if type(dict[key]) != type([]):
            dict[key] = dict[key].lower()
        elif type(dict[key]) == type([]):
            for index,item in enumerate(dict[key]):
                dict[key][index] = item.lower()

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
    dict_lowerCase(book_data)

    if book_data:
        book = await book_collection.insert_one(book_data)

        new_book = await book_collection.find_one({"_id": book.inserted_id})
        return book_helper(new_book)


async def update_book(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False


    # database.book_collection.find_one_and_update({"_id": ObjectId(id)},
    # {"$set": data})
    # print(data)
    # return data
    dict_lowerCase(data)
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return data
        return False


#delete an book
async def delete_book(id: str):
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        await book_collection.delete_one({"_id":ObjectId(id)})
        return True