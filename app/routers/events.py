from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, status, Depends
from ..database.schemas import EventsDb
from ..database.database import events
from ..routers.players import get_db
from ..database import crud_event, schemas

from app.database.schemas import EventsDb

router = APIRouter(prefix='/events', tags=['events'])

# 6. GET /events - palauttaa kaikki eventit
#CRUD read_events
@router.get('/', response_model=List[EventsDb], status_code=200)
def get_events(type: Optional[str] = None, db: Session = Depends(get_db)):
    return crud_event.read_events(db)