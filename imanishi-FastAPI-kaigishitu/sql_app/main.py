from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud, models, schemas
from .database import engine, SessionLocal

# modelsのBaseを持ってくる Databaseの作成をしている。
models.Base.metadata.create_all(bind=engine) # databaseのエンジンを使ってdatabaseの作成をしている。

# 2.apiを作成する
app = FastAPI()

### データベースを取得するための関数  とりあえずコピペでいいよ
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# apiを作成する
# @app.get("/")
# async def index():
#   return {"message","Success"}

### post
@app.post("/users")
async def create_users(user: schemas.User ,db : Session = Depends(get_db)):
  return crud.create_user(db=db,user=user)

@app.post("/rooms")
async def create_rooms(room: schemas.Room ,db : Session = Depends(get_db)):
  return crud.create_room(db=db,room=room)

@app.post("/bookings")
async def create_bookings(booking: schemas.Booking ,db : Session = Depends(get_db)):
  return crud.create_booking(db=db,booking=booking)

### read
@app.get("/users", response_model=List[schemas.User]) #返す値はschemasの型をリスト形式
async def read_users(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
  users = crud.get_users(db, skip=skip, limit=limit)
  return users

@app.get("/rooms", response_model=List[schemas.Room]) #返す値はschemasの型をリスト形式
async def read_rooms(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
  rooms = crud.get_rooms(db, skip=skip, limit=limit)
  return rooms

@app.get("/bookings", response_model=List[schemas.Booking]) #返す値はschemasの型をリスト形式
async def read_bookings(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
  bookings = crud.get_bookings(db, skip=skip, limit=limit)
  return bookings
