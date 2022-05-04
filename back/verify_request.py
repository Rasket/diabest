from hashlib import blake2b
from hmac import compare_digest
from fastapi import APIRouter, Depends, HTTPException, Request, Header, status
from typing import Optional
import databases
import random
from datetime import datetime
from models.phonecode import phonecode_table
import os


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
api_router = APIRouter()

@router.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()

def to_bytes(a):
    return bytes(a, 'utf-8')

def sign_link(phone):
    phone = to_bytes(phone)
    h = blake2b(digest_size=AUTH_SIZE*3, key=SECRET_KEY)
    h.update(phone + os.urandom(14) + to_bytes(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    return h.hexdigest().encode('utf-8').decode("utf-8")

def sign_token(phone):
    phone = to_bytes(phone)
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
    h.update(os.urandom(14) + to_bytes(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + phone)
    return h.hexdigest().encode('utf-8').decode("utf-8")

def verify(phone, sig):
    phone = to_bytes(phone)
    good_sig = sign(phone)
    return compare_digest(good_sig, sig)

@router.get("/phone/code/{phonenum}")
async def read_phone_code(phonenum: str, request: Request,
 q: Optional[str] = None, user_agent: Optional[str] = Header(None)):
    try:
         auth_header = request.headers['authorization']
    except KeyError as e:
         auth_header = None
    if ('Basic ZGlhYmVzdF9ib3Q6NEtKRkQ4OTNLMC1hS0FvaXUhNGs5aXBvNTQ=' == auth_header):
        phonenum = phonenum[2:]
        query = phonecode_table.select().where(phonecode_table.c.phone == phonenum)
        response = await database.fetch_all(query)
        if (response):
            query = (
                phonecode_table.update()
                .values(code=sign_link(phonenum), token=sign_token(phonenum),
                expr_date=datetime.now())
                .where(phonecode_table.c.phone == phonenum)
                .returning(phonecode_table.c.code)
            )
            return await database.fetch_one(query)
        else:
            query = (
                phonecode_table.insert()
                .values(phone=phonenum, code=sign_link(phonenum), token=sign_token(phonenum),
                expr_date=datetime.now())
                .returning(phonecode_table.c.code)
            )
            return await database.fetch_one(query)

    else:
        return 'Unauthorized'
# получить код по номеру
'''
@router.get("/phone/code/{phonenum}")
async def read_phone_code(phonenum: str, request: Request,
 q: Optional[str] = None, user_agent: Optional[str] = Header(None)):
    try:
         auth_header = request.headers['authorization']
    except KeyError as e:
         auth_header = None
    if ('Basic ZGlhYmVzdF9ib3Q6NEtKRkQ4OTNLMC1hS0FvaXUhNGs5aXBvNTQ=' == auth_header):
        phonenum = phonenum[2:]
        query = (
            phonecode_table.select()
            .where(phonecode_table.c.phone == phonenum)
        )
        return await database.fetch_one(query)
    else:
        return 'Unauthorized'
'''


@router.get("/phone/confirm/{phonenum}/{codenum}")
async def read_phone_code(phonenum: str, codenum: str, request: Request,
 q: Optional[str] = None):
    if (len(phonenum) == 12):
        phonenum = phonenum[2:]
    else:
        phonenum = phonenum[1:]
    query = (
        phonecode_table.select()
        .where(phonecode_table.c.phone == phonenum)
    )
    response = await database.fetch_one(query)
    if (response):
        for i in response:
            print(i)
            if (i == 'phone'):
                phone = response[i]
            if (i == 'code'):
                code = response[i]
            if (i == 'token'):
                token = response[i]
        print(phone, code, phonenum, codenum)
        if ((phone == phonenum) and (code==codenum)):
            query = (
                phonecode_table.update()
                .values(code='Removed')
                .where(phonecode_table.c.phone == phonenum)
                .returning(phonecode_table.c.token)
            )
            return await database.fetch_one(query)
        else:
            raise HTTPException(status_code=405, detail="Not correct")
    else:
        raise HTTPException(status_code=404, detail="User not found")



api_router.include_router(router, tags=["read_phone_code"])
