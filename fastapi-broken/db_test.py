import sqlite3

def get_joke(id=69):
    conn = sqlite3.connect("/home/willyyam/python/dadjokes/jokes.db")
    cursor = conn.cursor()
    cursor.execute("select setup, punchline, tags from jokes where id = ?", (id,))

    joke = cursor.fetchall()
    try:
        setup = f"{joke[0][0]}"
        punchline = f"{joke[0][1]}"
        tags = f"{joke[0][2]}"
    except IndexError:
        setup = "What smells funny?"
        punchline = "Clown farts."
        tags = f"#defaultjoke#noid-{str(id)}"

    return joke

print(get_joke())