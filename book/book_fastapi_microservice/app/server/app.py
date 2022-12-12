import os
from fastapi import FastAPI
from app.server.routes.book import router as BookRouter
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
import asyncio
import nest_asyncio
import pymongo
import time
from pymongo import MongoClient


app = FastAPI()


app.include_router(BookRouter, tags=["Book"], prefix="/book")

from app.server.database import MONGO_DETAILS, clientMotor
nest_asyncio.apply()


async def get_server_info():
    client = clientMotor

    try:
        print(await client.server_info())
        print('connected')
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Unable to connect to the database")
        # os._exit(os.EX_OK)
        # raise SystemExit
loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse ({":detail":"Endpoint is wrong"}, status_code=exc.status_code)

