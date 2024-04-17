#!/usr/bin/python

"""Return the joke with the requested ID 
from the jokes.db sqlite database."""

import json
import sqlite3

def new_joke(setup, punchline, tags):
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    vals = (str(setup), str(punchline), str(tags))
    cursor.execute("insert into jokes (setup, punchline, tags) values (?,?,?)", vals)
    inserted_id = cursor.lastrowid
    conn.commit()
    joke_dict = {"id":inserted_id, "setup":setup,"punchline":punchline,"tags":tags}
    joke_json = json.dumps(joke_dict)
    
    return joke_json


if __name__ == "__main__":
    print(new_joke("test setup","test punchline","#notags"))