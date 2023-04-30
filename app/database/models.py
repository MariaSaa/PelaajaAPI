from sqlalchemy import Column, Integer, String, func, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

#Pelaajat
#id
#name
#events

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    events = relationship("Event", back_populates="player")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    detail = Column(String)
    player_id = Column(Integer, ForeignKey("players.id"))

    player = relationship("Player", back_populates="events")
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)


