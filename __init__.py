from flask import Flask
app = Flask(__name__)
import flasker.main

from flasker import db
db.create_firms_table()