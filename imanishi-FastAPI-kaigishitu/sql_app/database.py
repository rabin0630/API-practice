from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースの保存先とDBを操作するための準備

## 1.データベースの保存先を決定
### データベースの格納先を指定
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"   # データベースの格納先

## 2.DBを操作するための準備
### CRUDのベースとなる基盤（エンジン）をインスタンス化     コピペでええよ　　　Crud操作をするとき
engine = create_engine(
  SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
  ) # connect_argsはsqlite用の設定
### インスタンス化する（セッションを定義する)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) # エンジンとこれを統合
Base = declarative_base()  # クラスを継承した