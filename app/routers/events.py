from typing import List, Optional

from fastapi import HTTPException, APIRouter, status
from ..database.schemas import EventsDb
from ..database.database import events

from app.database.schemas import EventsDb

router = APIRouter(prefix='/events', tags=['events'])

# 6. GET /events - palauttaa kaikki eventit
@router.get('/events', response_model=List[EventsDb])
def get_events(type: Optional[str] = None):
    checkEvents = []
    #no bueno
    for player in players:
        if 'events' not in player:
            continue
        for event in player['events']:
            if type is None or event['type'] == type:
                checkEvents.append(event)
            elif type not in ['level_started', 'level_solved']:
                raise HTTPException(status_code=400, detail='Invalid event type')
    return checkEvents