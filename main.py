# import string
from typing import List
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#1
class PlayerIn(BaseModel):
    name: str

#3
class PlayerAllList(BaseModel):
    id: int
    name: str

#4
class EventsBase(BaseModel):
    id: int
    type: str
    detail: str

# #2
class PlayerDb(PlayerIn):
     id: int
     events: List[EventsBase] = []

# #5
class EventsDb(EventsBase):
    player_id: int
    timestamp: str


players = [
    {'id':1, 'name':'Maria'},
    {'id':2, 'name':'Reijo'},
    {'id':3, 'name':'Veijo'},
    {'id':4, 'name':'Keijo'}
]

events = [
    {'id':0, 'type':'level_started', 'detail': 'v2021', 'player_id':1, 'timestamp':'12.4.2023 19:28'},
    {'id':4, 'type':'level_solved', 'detail': 'v2021', 'player_id':1, 'timestamp':'12.4.2023 19:28'},
    {'id':1, 'type':'level_solved', 'detail': 'c2020', 'player_id':2, 'timestamp':'12.4.2023 19:28'},
    {'id':2, 'type':'level_started', 'detail': '98713f', 'player_id':3, 'timestamp':'12.4.2023 19:28'}, 
    {'id':3, 'type':'level_solved', 'detail': 'f2335', 'player_id':4, 'timestamp':'12.4.2023 19:28'} 
]

#GET /players - palauttaa pelaajien nimet ja id:t
#laita ensin id ja sitten nimi
@app.get('/players')
def player_name_id():
    player_names_and_ids = [{"id": player["id"], "name": player["name"]} for player in players]
    return player_names_and_ids

#GET /players/{id} - palauttaa tietyn pelaajan kaikki tiedot
#timestamp puuttuu
@app.get("/players/{id}")
def get_player(id: int):
    for player in players:
        if player['id'] == id:
            player_events = [event for event in events if event['player_id'] == id]
            player['events'] = player_events
            return player
    raise HTTPException(status_code=404, detail='Player not found')


#POST /players - uuden pelaajan luomiseen
@app.post('/players')
def create_player(player_in:PlayerIn):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player

#4. GET /players/{id}/events - palauttaa tietyn pelaajan kaikki eventit
@app.get('/players/{id}/events')
def get_player_events(id: int, type: str = None):
    #tarkista pelaaja
    player = None
    for p in players:
        if p['id'] == id:
            player = p
            break
    if not player:
        raise HTTPException(status_code=404, detail='Player not found')

    #tarkista event
    if type is not None:
        if type not in ['level_started', 'level_sorted']:
            raise HTTPException(status_code=400, detail='Invalid event')

        player_events = [event for event in events if event['player_id'] == id and event['type'] == type]
    else:
        player_events = [event for event in events if event['player_id'] == id]

    return player_events

#5. POST /players/{id}/events - luo uuden eventin pelaajalle
#tuplakoodia! korjaa! (pelaajan ja eventin tarkistus)
@app.post('/players/{id}/events', status_code=201, response_model=EventsDb,)
def create_event(id: int, event: EventsBase, type: str = None):
    #tarkista pelaaja
    player = None
    for p in players:
        if p['id'] == id:
            player = PlayerDb(**p)
            break
    if not player:
        raise HTTPException(status_code=404, detail='Player not found',)
    #tarkista event type
    if type is not None:
        if type not in ['level_started', 'level_sorted']:
            raise HTTPException(status_code=400, detail='Invalid event')
    #luo uusi event
    new_event = EventsDb(**event.dict(), player_id=id, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    player.events.append(new_event)
    return new_event

