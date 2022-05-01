from typing import Optional
from fastapi import FastAPI, Request, Header, status, HTTPException

import databases
import random
from models.phonecode import phonecode_table

DB_USER = "diabes"
DB_PASSWORD = "secret"
DB_HOST = "localhost"
DB_NAME = "diabest"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)
