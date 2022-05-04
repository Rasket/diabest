from hashlib import blake2b
from hmac import compare_digest
from fastapi import APIRouter, Depends, HTTPException, Request, Header, status
from typing import Optional
import databases
import random
from datetime import datetime
from models.phonecode import phonecode_table
import os
from models.card import card_table
from  sqlalchemy.sql.expression import func, select

DB_USER = "diabes"
DB_PASSWORD = "secret"
DB_HOST = "localhost"
DB_NAME = "diabest"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)

SECRET_KEY = b'537y~@$#321J490!@l!891FG2ht78T'
AUTH_SIZE = 10
router = APIRouter()
api_router_a = APIRouter()

@router.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()
# выдача данных из БД по блюдам
@router.get("/cards/random/")
async def read_item(q: Optional[str] = None):
    query = card_table.select().order_by(func.random())
    return await database.fetch_all(query)


api_router_a.include_router(router, tags=["card"])
