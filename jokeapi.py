#!/usr/bin/python                                                                         
 
"""Basic API using FastAPI"""
 
# main.py

from by_id import by_id
from fastapi import FastAPI
from pydantic import BaseModel 
 
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
 
