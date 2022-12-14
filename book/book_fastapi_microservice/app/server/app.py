import os
from fastapi import FastAPI
from server.routes.book import router as BookRouter
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
import nest_asyncio
from server.database import MONGO_DETAILS, clientMotor
import pymongo
import asyncio

app = FastAPI()

app.include_router(BookRouter, tags=["Book"], prefix="/book")

nest_asyncio.apply()

async def get_server_info():
    client = clientMotor

    try:
        print(await client.server_info())
        print('connected')
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Unable to connect to the database")
loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse ({":detail":"Endpoint is wrong"}, status_code=exc.status_code)

