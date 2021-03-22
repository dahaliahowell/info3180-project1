from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app # we import the app object from the app module
from app import db

db.create_all()