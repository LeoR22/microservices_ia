"""
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-- Autor: Leandro Rivera
-- Descripción: Proyecto donde se expone un API LLMs de TinyLlama en el framework de FastAPI desde un contendor de Docker
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
"""
from api_v1.routes import tinyllama
from fastapi import APIRouter

router = APIRouter()

router.include_router(tinyllama.router) 

