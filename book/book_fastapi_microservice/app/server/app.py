from fastapi import FastAPI
from server.routes.book import router as BookRouter

app = FastAPI()

app.include_router(BookRouter, tags=["Book"], prefix="/book")