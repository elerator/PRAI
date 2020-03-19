import os
import sqlite3

from lightweight_research_tool.settings import *
path = os.path.join(os.path.join(os.path.split(BASE_DIR)[0],"database2"), 'db.sqlite3')
print(path)

with open(path, "r+"):
    print("okay reading in r+ mode worked")

conn = sqlite3.connect(path)
