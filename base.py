
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import json
config = json.loads(open("config.json", 'r' ).read())
engine = create_engine(config["host"])
Session = sessionmaker(bind=engine)
Base = declarative_base()