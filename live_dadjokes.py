import json
import sqlite3

DBPATH = "jokes.db"

def random_joke():
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("select setup, punchline, tags from jokes order by random() limit 1")

    try:
        joke = cursor.fetchall()
    except IndexError:
        print(f"IndexError: {str(id)}")

    return joke


def get_joke(id=69):
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("select setup, punchline, tags from jokes where id = ?", (id,))

    try:
        joke = cursor.fetchall()
    except IndexError:
        print(f"IndexError: {str(id)}")

    return joke


def jsonjoke(joke):
    setup = joke[0][0]
    punchline = joke[0][1]
    tags = joke[0][2]
    all_tags = tags.split("#")
    tmp_dict = {"setup":setup,"punchline":punchline,"tags":all_tags}
    my_joke_in_json = json.dumps(tmp_dict)

    return my_joke_in_json


def plainpage(the_joke):
    setup = the_joke[0][0]
    punchline = the_joke[0][1]
    html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>dad jokes</title>
<meta name="Author" content="William Witteman" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style>
h1 {{
    font-size: 5vw;
    color: #4350bd;
    font-family: serif, Georgia;
}}
body {{
    padding: 2rem;
}}

.main {{
    background-color: white;
    padding: 1rem;
}}
.setup {{
  background-color: white;
  font-size: 3vw;
  font-size: clamp(2rem,3vw,3vw);
  color: black;
  font-family: sans serif;
  padding: 1rem;
  padding-left: 2rem;
}}
.punchline {{
  background-color: white;
  font-size: 3vw;
  font-size: clamp(2rem,3vw,3vw);
  color: black;
  font-family: sans serif;
  padding: 1rem;
  padding-top: 2rem;
  padding-left: 2rem;
}}
</style>
</head>
<body>
<div class="main">
<h1>dad jokes</h1>
<div class="setup">
    {setup}
</div>
<div class="punchline">
    {punchline}
</div>
</div>

</body>
</html>"""

    return html


def get_default_joke():
    da_jokes = ["A panda walks into a bar and says to the bartender 'I'll have a Scotch and . . . . . . . . . . . . . . Coke thank you'. 'Sure thing' the bartender replies and asks 'but what's with the big pause?'","The panda holds up his hands and says, 'I was born with them'.",""]

    return da_jokes


def application(environ, start_response):
    qstring = environ.get("QUERY_STRING")
    status = '200 OK'
    html = ""


    if qstring:
        key, value = qstring.split("=")
        if key == "id":
            if int(value):
                this_joke = get_joke(int(value))
                html = plainpage(this_joke)
    else:
        joke = random_joke()
        html = plainpage(joke)

    output = html.encode("utf-8")
 
    response_headers = [('Content-type', 'text/html'),
                ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    
    return [output]