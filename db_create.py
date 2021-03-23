from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from app import db

db.create_all()