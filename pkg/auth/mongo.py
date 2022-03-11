from pymongo.database import Database
from uuid import UUID
from .schema import AddUserSchema
from models.user import User
from bson import BSON
from pydantic import EmailStr
from typing import Union

class Repo:
    db:Database = None

    def __init__(self,client:Database) -> None:
        self.db = client

    def AddUser(self,inp :AddUserSchema) -> BSON:
        user_dict = inp.dict(by_alias=True)
        user_dict["derived_key_hash"] = user_dict["derived_key"]
        del user_dict["derived_key"]
        user = User(**user_dict)
        id = self.db.users.insert_one(user.dict(by_alias=True)).inserted_id
        print(type(self.db))
        return id
    
    def GetUserByEmail(self,email:EmailStr) -> Union[User,None]:
        user_dict = self.db.users.find_one({"email":email})
        if user_dict != None:
            return User(**user_dict)
        return None
    
    def GetUserById(self,id :BSON) -> User:
        return self.db.users.find_one({"_id":str(id)})