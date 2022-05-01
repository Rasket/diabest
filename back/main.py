from typing import Optional
from fastapi import FastAPI, Request, Header, status, HTTPException
from verify_request import api_router
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

app = FastAPI()
app.include_router(api_router)

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080/*",
    "http://127.0.0.1:5000/phone/register/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_phone_code():
    code = ""
    for i in range(0, 6):
        code += str(random.randint(0, 9))
    return code

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()

@app.get("/")
async def read_root():
    # изменим роут таким образом, чтобы он брал данные из БД
    query = "SELECT * FROM phonecode"
    return await database.fetch_all(query)

@app.post("/phone/register/{phonenum}")
async def read_item(phonenum: str, q: Optional[str] = None):
    phonenum = phonenum[1:]
    query = phonecode_table.select().where(phonecode_table.c.phone == phonenum)
    response = await database.fetch_all(query)
    phone = ""
    if (response):
        for i in response:
            phone = tuple(i.values())[0]
        query = (
            phonecode_table.update()
            .values(code=generate_phone_code())
            .where(phonecode_table.c.phone == phone)
            .returning(phonecode_table.c.phone)
        )
    else:
        query = (
            phonecode_table.insert()
            .values(phone=phonenum, code=generate_phone_code())
            .returning(phonecode_table.c.phone)
        )
    return await database.fetch_all(query)
