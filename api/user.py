from models.user import User
from fastapi import APIRouter
from pydantic import EmailStr
from pkg.auth.schema import AddUserSchema,SignInSchema,GetUserSchema
from pkg.auth.service import Service
from db.db import get_database
from bson import BSON

userSvc = Service(get_database())

UserRouter = APIRouter(prefix="/users")

@UserRouter.put("/register",response_model=BSON)
def RegisterRoute(body:AddUserSchema):
    user_id = userSvc.RegisterUser(body)
    return user_id

@UserRouter.post("/login",response_model=GetUserSchema)
def LoginRoute(body:SignInSchema):
    user = userSvc.SignIn(body)
    user_dict = user.dict()
    return GetUserSchema(**user_dict)

@UserRouter.get("/get_salt")
def GetSalt(email:EmailStr):
    salt = userSvc.GetSalt(email)
    return salt
