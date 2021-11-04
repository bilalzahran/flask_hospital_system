from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.config import db_url

engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))