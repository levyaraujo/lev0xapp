from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(settings.CONNECTION, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def init_database():
    Base.metadata.create_all(engine)