from typing import List
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PlayerIn(BaseModel):
    name: str
    class Config:
        orm_mode = True

#4
class EventsBase(BaseModel):
    type: str
    detail: str
#5
class EventsDb(EventsBase):
    id: int
    player_id: int
    timestamp: datetime
    class Config:
        orm_mode = True

#2
class PlayerDb(PlayerIn):
    id: int
    events: List[EventsDb] = []
    class Config:
        orm_mode = True