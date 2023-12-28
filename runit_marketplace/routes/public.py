from fastapi import APIRouter

public_router = APIRouter()


@public_router.get("/")
def hello_world():
    return "Hello, World!"
