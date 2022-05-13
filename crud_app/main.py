from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, 'inventory.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    done = db.Column(db.Boolean)
    dateAdded = db.Column(db.DateTime, default=datetime.now())


def create_inventory(text):
    inventory_item = Inventory(text=text)
    db.session.add(inventory_item)
    db.session.commit()
    db.session.refresh(inventory_item)


def view_inventory(inventory_item_id, text, done):
    db.session.query(Inventory).filter_by(id=inventory_item_id).update({
        'text': text,
        'done': True if done == 'on' else False
    })
    db.session.commit()


def delete_inventory_item(inventory_item_id):
    db.session.query(Inventory).filter_by(id=inventory_item_id).delete()
    db.session.commit()