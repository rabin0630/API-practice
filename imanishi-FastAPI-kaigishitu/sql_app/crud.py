from sqlalchemy.orm import Session
from . import models, schemas

#models(登録した項目)のCRUD設定

## Read

### ユーザー一覧を取得
def get_users(db :Session, skip: int = 0, limit: int = 100):
  return db.query(models.User).offset(skip).limit(limit).all()

### 会議室一覧取得
def get_rooms(db :Session, skip: int = 0, limit: int = 100):
  return db.query(models.Room).offset(skip).limit(limit).all()

### 予約一覧取得
def get_bookings(db :Session, skip: int = 0, limit: int = 100):
  return db.query(models.Booking).offset(skip).limit(limit).all()


## Create

### ユーザー登録
def create_user(db: Session, user: schemas.User):
  db_user = models.User(username=user.username) ### インスタンスを生成して、usernameをいれる
  db.add(db_user) ### インスタンス化したdb_userをdbに追加する
  db.commit() ### addとcommitはgitと似ている
  db.refresh(db_user) ### 変更をしたらリフレッシュする必要はある
  return db_user

### 会議室登録
def create_room(db: Session, room: schemas.Room):
  db_room = models.Room(roomname=room.roomname, capacity=room.capacity) ### インスタンスを生成して、roomnameをいれる
  db.add(db_room) ### インスタンス化したdb_roomをdbに追加する
  db.commit() ### addとcommitはgitと似ている
  db.refresh(db_room) ### 変更をしたらリフレッシュする必要はある
  return db_room

### 予約登録
def create_booking(db: Session, booking: schemas.Booking):
  db_booking = models.Booking(
      user_id = booking.user_id,
      room_id = booking.room_id,
      booked_num = booking.booked_num,
      start_datetime = booking.start_datetime,
      end_datetime = booking.end_datetime
    ) ### インスタンスを生成して、bookingnameをいれる
  db.add(db_booking) ### インスタンス化したdb_bookingをdbに追加する
  db.commit() ### addとcommitはgitと似ている
  db.refresh(db_booking) ### 変更をしたらリフレッシュする必要はある
  return db_booking