from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

# Databaseで登録したい情報を入力

# テーブル設計をする
## 細かい設定はsqlalchemyで調べる
class User(Base):   #定義の仕方はapp.pyと似ている
  __tablename__ = "users"
  user_id = Column(Integer, primary_key=True, index=True)  ### primari_keyは勝手に決まる
  username = Column(String, unique=True, index=True)

class Room(Base):
  __tablename__ = "rooms"
  room_id = Column(Integer,primary_key=True, index=True)
  roomname = Column(String,unique=True, index=True)# Field(max_length=12)
  capacity = Column(Integer, index=True)

class Booking(Base):
  __tablename__ = "bookings"
  booking_id = Column(Integer,primary_key=True, index=True)
  user_id = Column(Integer,ForeignKey("users.user_id",ondelete="SET NULL"), nullable=False, index=True)
  room_id = Column(Integer,ForeignKey("rooms.room_id",ondelete="SET NULL"), nullable=False, index=True)
  booked_num = Column(Integer)
  start_datetime = Column(DateTime, nullable=False)
  end_datetime = Column(DateTime, nullable=False)