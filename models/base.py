from pydantic import BaseModel, Field
from datetime import datetime
import bson

class Base(BaseModel):
    _id:bson.BSON= Field(default=bson.ObjectId())
    created_time:datetime = Field(default=datetime.now())
    updated_time:datetime = Field(default=datetime.now())
    deleted_time:datetime = Field(default=datetime.now())
