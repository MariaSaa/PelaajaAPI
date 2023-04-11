from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class PlayerIn(BaseModel):
    name: str
    event: list

class PlayerDb(PlayerIn):
    id: int

players = [
    {'id':1, 'name':'Maria', 'events':['moi']},
    {'id':2, 'name':'Reijo', 'events':['hei']},
    {'id':3, 'name':'Veijo', 'events':['batman']},
    {'id':4, 'name':'Keijo', 'events':['lentää']}
]

#GET /players - palauttaa pelaajien nimet ja id:t
@app.get('/players')
def player_name_id():
    player_names_and_ids = [{"id": player["id"], "name": player["name"]} for player in players]
    return player_names_and_ids

#GET /players/{id} - palauttaa tietyn pelaajan kaikki tiedot
@app.get('/players/{id}')
def get_players(id: int):
    return players[id]

#POST /players - uuden pelaajan luomiseen
@app.post('/players')
def create_player(player_in:PlayerIn):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player


# @app.get('/players/{id}')
# def get_players(player_name: str = ''):
#      if player_name != '':
#          return [b for b in players if b['name'] == player_name]
#      else:
#          return players
