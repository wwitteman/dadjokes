#!/usr/bin/python                                                                         
 
"""Basic API using FastAPI"""
 
# main.py
 
from by_id import by_id
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from new import new_joke
from pydantic import BaseModel
from typing import Annotated
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
class Joke(BaseModel):
    setup: str
    punchline: str | None = None
    tags: str | None = None
 
app = FastAPI()
 
@app.get("/")
async def root():
    return {"setup": "What does a baby computer call his father?", "punchline": "Data.", "tags": ""}
 
@app.get("/id/{id}")
async def byId(id: str):
    the_joke = by_id(id)
    return {the_joke}
 
@app.post("/new/")
async def new(joke: Joke, token: Annotated[str, Depends(oauth2_scheme)]):
    the_joke = new_joke(setup=joke.setup, punchline=joke.punchline, tags=joke.tags)
    return {the_joke}
