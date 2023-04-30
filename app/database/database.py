from .schemas import PlayerDb, EventsDb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection string
#tekee projektin juureen pelaajaAPI tietokannan
SQLALCHEMY_DATABASE_URL = "sqlite:///./pelaajaAPI.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Sessionlocal, luodaan yhteys
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

events = [
    {'id':0, 'type':'level_started', 'detail': 'v2021', 'player_id':1, 'timestamp':'12.4.2023 19:28'},
    {'id':4, 'type':'level_solved', 'detail': 'v2021', 'player_id':1, 'timestamp':'12.4.2023 19:28'},
    {'id':1, 'type':'level_solved', 'detail': 'c2020', 'player_id':2, 'timestamp':'12.4.2023 19:28'},
    {'id':2, 'type':'level_started', 'detail': '98713f', 'player_id':3, 'timestamp':'12.4.2023 19:28'}, 
    {'id':3, 'type':'level_solved', 'detail': 'f2335', 'player_id':4, 'timestamp':'12.4.2023 19:28'} 
]