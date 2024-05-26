import requests
import json
import sqlite3

key = "9e058f0fb454486db5fbb566e54d6070"
info = input("sheiyvanet raze gsurt infos migeba: ")
date = "2024-04-26"
url = f"https://newsapi.org/v2/everything?q={info}&from={date}&sortBy=publishedAt&apiKey={key}"
resp = requests.get(url)
# print(resp.headers)
print(resp.status_code)
content = resp.json()
# print(json.dumps(content, indent=3))
print(content["articles"][0]['author'])
print(content["articles"][0]['title'])
print(content["articles"][0]['description'])
conn = sqlite3.connect('news.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS news (
id INTEGER PRIMARY key AUTOINCREMENT,
author,
title,
description)
""")


c.execute("insert into news (author, title, description) values (?, ?, ?)", (content["articles"][0]['author'],content["articles"][0]['title'], content["articles"][0]['description']  ))
conn.commit()
conn.close()
