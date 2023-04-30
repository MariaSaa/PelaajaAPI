from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def get_player(db: Session, player_id: int):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail='Player not found')
    return player

#1
def read_player_name_id(db: Session):
    return db.query(models.Player).all()

#2
def create_player(db: Session, player_in: schemas.PlayerIn):
    player = models.Player(**player_in.dict())
    if player is None:
        raise HTTPException(status_code=422, detail='Invalid data')
    else:
        db.add(player)
        db.commit()
        db.refresh(player)
    return player

#3
#id:llä 5 tulee error?
def read_player_id(id: int, db: Session):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='Unknown player :(')
    return player

#4
#response body väärässä järjestyksessä
# type filter ei toimi
def return_player_events(id: int, db: Session, type: str = None ):
    #Fetch player from database
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=404, detail='Player not found')

    # Check event type
    if type is not None:
        if type not in ['level_started', 'level_solved']:
            raise HTTPException(status_code=400, detail='Invalid event')

        player_events = db.query(models.Event).filter(models.Event.player_id == id, models.Event.type == type).all()
    else:
        player_events = db.query(models.Event).filter(models.Event.player_id == id).all()
    return player_events

#5 
def create_events(db: Session, event_in: schemas.EventsBase, player_id: int):
    db_event = models.Event(**event_in.dict(), player_id=player_id)
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='Unknown player :(')
    if event_in.type is not None:
        if event_in.type not in ['level_started', 'level_solved']:
            raise HTTPException(status_code=400, detail='Invalid event')
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event