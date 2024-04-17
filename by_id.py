#!/usr/bin/python

"""Return the joke with the requested ID 
from the jokes.db sqlite database."""

import json
import sqlite3

def by_id(id):
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    myID = (int(id),)
    cursor.execute("select setup, punchline, tags from jokes where id = ?", myID)
    joke = cursor.fetchall()
    try:
        setup = f"{joke[0][0]}"
        punchline = f"{joke[0][1]}"
        tags = f"{joke[0][2]}"
    except IndexError:
        setup = "What smells funny?"
        punchline = "Clown farts."
        tags = f"#defaultjoke#noid-{str(id)}"
    joke_dict = {"setup":setup,"punchline":punchline,"tags":tags}
    joke_json = json.dumps(joke_dict)
    
    return joke_json


if __name__ == "__main__":
    print(by_id(999))