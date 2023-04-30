from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, status, Depends
from ..database.schemas import EventsDb
from ..database.database import events
from ..routers.players import get_db
from ..database import crud_event, schemas

from app.database.schemas import EventsDb

router = APIRouter(prefix='/events', tags=['events'])

#def player_name_id(db: Session = Depends(get_db)):
#   return crud_player.read_player_name_id(db)

# 6. GET /events - palauttaa kaikki eventit
#CRUD read_events
@router.get('/', response_model=List[EventsDb], status_code=200)
def get_events(type: Optional[str] = None, db: Session = Depends(get_db)):
    return crud_event.read_events(db)
    # checkEvents = []
    # #no bueno
    # for player in players:
    #     if 'events' not in player:
    #         continue
    #     for event in player['events']:
    #         if type is None or event['type'] == type:
    #             checkEvents.append(event)
    #         elif type not in ['level_started', 'level_solved']:
    #             raise HTTPException(status_code=400, detail='Invalid event type')
    # return checkEvents