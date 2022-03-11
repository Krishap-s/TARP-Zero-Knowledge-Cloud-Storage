from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Base(BaseModel):
    created_time:datetime = Field(default=datetime.now())
    updated_time:datetime = Field(default=datetime.now())
    deleted_time:datetime = Field(default=datetime.now())
