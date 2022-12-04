from fastapi import FastAPI
from server.routes.book import router as BookRouter
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(BookRouter, tags=["Book"], prefix="/book")

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return JSONResponse({"detail": "Endpoint is wrong"}, status_code=exc.status_code)
