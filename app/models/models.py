from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class TaskAPI(db.Model):
	__tablename__ = 'Task_API'
	
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	title = db.Column(db.String(255), nullable = False)
	description = db.Column(db.String(255), nullable = False)
	create_date = db.Column(db.DateTime, default= datetime.datetime.now)