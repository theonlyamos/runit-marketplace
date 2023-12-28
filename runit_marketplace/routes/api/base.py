from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

@api_router.get("/")
async def get_all_apps():
    return [{"name": "John"}, {"name": "Jane"}] 

