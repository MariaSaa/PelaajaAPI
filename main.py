# import string
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
     #events: (list[EventsBase])

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
    {'id':1, 'type':'level_solved', 'detail': 'c2020', 'player_id':2, 'timestamp':'12.4.2023 19:28'},
    {'id':2, 'type':'level_started', 'detail': '98713f', 'player_id':3, 'timestamp':'12.4.2023 19:28'}, 
    {'id':3, 'type':'level_solved', 'detail': 'f2335', 'player_id':4, 'timestamp':'12.4.2023 19:28'} 
]

#GET /players - palauttaa pelaajien nimet ja id:t
@app.get('/players')
def player_name_id():
    player_names_and_ids = [{"id": player["id"], "name": player["name"]} for player in players]
    return player_names_and_ids

#GET /players/{id} - palauttaa tietyn pelaajan kaikki tiedot
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
def get_player_events(id: int, type: str):
    #tarkista pelaaja
    for i in range(len(players)):
        if players[i] == id:
            player = players[i]
        else:
            raise HTTPException(detail="player not found", status_code=404)
    #tarkista event
    player_events = [event for event in events if event['player_id'] == id and event['event_type'] in ['level_started', 'level_sorted']]
    return player_events
