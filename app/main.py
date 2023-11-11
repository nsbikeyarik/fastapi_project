import typing

import delete as delete
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date, datetime
# datetime.now()
# datetime.day
from typing import Optional, Union
# from typing import Union, Optional, Any, List, Dict, Tuple

class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    date_joined: date
    location: Optional[str] = None
    age: int = Field(None, ge=5, le=130)


class User1(BaseModel):
    username: str
    date_joined: date
    location: str
    age: int
    car: str

class CreateUserRequest(BaseModel):
    pass


user_db = {
    'nick': User(username='nick', date_joined='2023-10-01', location='kyiv', age=23),
    'vlad': User(username='vlad', date_joined='2023-10-03', location='odessa', age=25),
    'sergiy': User(username='sergiy', date_joined='2023-10-04', location='brovaru', age=27)
}





app = FastAPI(
    title="Guest book"
)


@app.post("/users/{user_id}")
def create_user(user: Union[User, User1]) -> dict:
    print(type(user))
    username = user.username
    user_db[username] = user
    return {'message': f'Successfully create user:{username}'}

@app.get("/user/{username}")
def all_user(limit: int = 5):
    user_list = list(user_db.values())
    return user_list[:limit]


@app.get("/users/{username}")
def show_user(username: str):
    return user_db[username]


@app.delete("/users/{username}")
def delete_user(username: str):
    del user_db[username]
    return {"message": f'Successfully delete user:{username}'}


@app.put("/users/{user_id}")
def update_user(user: User):# update to user and user1
    username = user.username
    user_db[username] = user
    return {'message' f'Successfully update user: {username}'}
