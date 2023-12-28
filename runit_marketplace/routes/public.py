from fastapi import APIRouter

public_router = APIRouter()


@public_router.get("/")
def hello_world():
    return "Hello, World!"

@public_router.get("/users")
async def get_users():
    return [{"name": "John"}, {"name": "Jane"}]


@public_router.get("/users/{user_id}") 
async def get_user(user_id: int):
    return {"name": f"User {user_id}"}
