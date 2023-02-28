from pydantic import BaseModel, Field, EmailStr
from typing import Optional


# Define the model for the request body
class TaskCreate(BaseModel):
    id: Optional[int]
    name: str
    description: str
    status: bool


class TaskUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    status: Optional[bool]


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)


