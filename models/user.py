from pydantic import BaseModel,EmailStr
from .base import Base

class User(Base):
    name:str
    email:EmailStr
    encrypted_master_password:str
    derived_key_hash:str
