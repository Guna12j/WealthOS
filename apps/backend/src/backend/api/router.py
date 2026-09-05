from fastapi import APIRouter

from backend.api.users import router as users_router

router = APIRouter()

router.include_router(users_router)