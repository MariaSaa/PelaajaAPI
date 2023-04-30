from ast import List
from datetime import datetime
from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

#6 
def read_events(db: Session, type: Optional[str] = None):
    if type and type not in ['level_started', 'level_solved']:
        raise HTTPException(status_code=400, detail='Unknown event type')

    events = db.query(models.Event)
    if type:
        events = events.filter(models.Event.type == type)

    return events.all()
