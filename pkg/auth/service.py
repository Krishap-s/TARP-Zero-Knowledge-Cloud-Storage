from pydantic import EmailStr
from .schema import AddUserSchema, GetUserSchema, SignInSchema
from .mongo import Repo
from pymongo.database import Database 
from bson import BSON
from models.user import User
from Cryptodome.Hash import SHA256
from fastapi.exceptions import HTTPException

class Service():
    repo:Repo = None

    def __init__(self,client:Database) -> None:
        self.repo = Repo(client)
    
    def RegisterUser(self,inp:AddUserSchema) -> BSON:
        if self.repo.GetUserByEmail(inp.email) != None:
            raise Exception("email already exists")

        hasher = SHA256.new()
        hasher.update(inp.derived_key.encode())
        inp.derived_key = hasher.hexdigest()
        id = self.repo.AddUser(inp)
        return id
    
    def GetSalt(self,inp:EmailStr) -> str:
        user = self.repo.GetUserByEmail(inp)
        if user == None:
            raise HTTPException(status_code="404",detail="user not found")
        return user.salt


    def SignIn(self,inp:SignInSchema) -> User:
        user = self.repo.GetUserByEmail(inp.email)
        if user == None:
            raise HTTPException(status_code="404",detail="user not found")
        hasher = SHA256.new()
        hasher.update(inp.derived_key.encode())
        if hasher.hexdigest() != user.derived_key_hash:
            raise HTTPException(status_code="403",detail="invalid credentials")
        else:
            return user

        

