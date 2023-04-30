#Mallit In -loppuiset, mitä tietoja tarvitaan LUODESSA uutta 
#Mallit database, mitä 
#1
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from fastapi import Depends, HTTPException, APIRouter, status
from ..database.schemas import PlayerDb, PlayerIn, EventsBase, EventsDb
# from ..database.database import SessionLocal, players
from ..database.database import events
from ..database import crud_player, schemas
from ..database.database import SessionLocal


router = APIRouter(prefix='/players', tags=['players'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close 


#GET /players - palauttaa pelaajien nimet ja id:t
#CRUD read_player_name_id db
@router.get('', status_code=200)
def return_player_name_id(db: Session = Depends(get_db)):
    return crud_player.read_player_name_id(db)
    # player_names_and_ids = [{"id": player["id"], "name": player["name"]} for player in players]
    # return player_names_and_ids

#3
#GET /players/{id} - palauttaa tietyn pelaajan kaikki tiedot
#CRUD read_player_id
@router.get("/{id}", response_model=PlayerDb, status_code=200)
def get_player_id(id: int, db: Session = Depends(get_db)):
    return crud_player.read_player_id(id, db)
    # for player in players:
    #     if player['id'] == id:
    #         player_events = [event for event in events if event['player_id'] == id]
    #         player['events'] = player_events
    #         return player
    # raise HTTPException(status_code=404, detail='Player not found')

#2
#POST /players - uuden pelaajan luomiseen
#CRUD create_player
@router.post('', status_code=201)
def create_new_player(player_in:PlayerIn, db: Session = Depends(get_db)):
    return crud_player.create_player(db, player_in)
    # new_id = len(players)
    # player = PlayerDb(**player_in.dict(), id=new_id)
    # players.append(player.dict())
    # return player

#4. GET /players/{id}/events - palauttaa tietyn pelaajan kaikki eventit
#CRUD return_player_events
@router.get('{id}/events', status_code=200)
def get_player_events(id: int, type: str = None, db: Session = Depends(get_db)):
    return crud_player.return_player_events(id, db)
   

#5. POST /players/{id}/events - luo uuden eventin pelaajalle
#CRUD create_events
# @router.post('/{id}/events', response_model=EventsDb, status_code=201)
# def create_event_database(event_in: schemas.EventsBase, player_id: int, db: Session = Depends(get_db)):
#     return crud_player.create_events(db, event_in, player_id)
@router.post('/{id}/events', response_model=schemas.EventsDb, status_code=201)
def create_event_database(event_in: schemas.EventsBase, id: int, db: Session = Depends(get_db)):
    player = crud_player.get_player(db, id)
    if not player:
        raise HTTPException(status_code=404, detail='Player not found')
    event = crud_player.create_events(db, event_in, player_id=id)
    return event
