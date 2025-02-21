from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = 'mysql+pymysql://root:Jojo%40123@127.0.0.1:3306/todos_db'
DATABASE_URL = 'sqlite:///./todos_db.db'

# engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}) for sqllite
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
