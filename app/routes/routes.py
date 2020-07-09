from flask import render_template, redirect, request, url_for, flash, jsonify
from app.models.models import db
from app.models.models import TaskAPI
from app.schemas.schemas import ma
from app.schemas.schemas import TaskAPISchema
from app import app

task_schema =  TaskAPISchema()
tasks_schema =	TaskAPISchema(many = True)

@app.route('/tasks', methods=['POST'])
def create_task():
	title = request.json['title']
	description = request.json['description']

	new_task = TaskAPI(title = title, description = description)
	db.session.add(new_task)
	db.session.commit()

	return task_schema.jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
	all_tasks = TaskAPI.query.all()
	result = tasks_schema.dump(all_tasks)
	return jsonify(result), 200

@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
	task = TaskAPI.query.get(id)
	if(task != None):
		return task_schema.jsonify(task)
	else:
		return jsonify({'title': None, 'description': None, 'id': None, 'create_date': None}), 400

@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
	task = TaskAPI.query.get(id)
	if(task != None):
		title = request.json['title']
		description = request.json['description']

		task.title = title
		task.description = description
		db.session.commit()

		return task_schema.jsonify(task), 200
	else:
		return jsonify({'title': None, 'description': None, 'id': None, 'create_date': None}), 400

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
	del_task = TaskAPI.query.get(id)
	if(del_task != None):
		db.session.delete(del_task)
		db.session.commit()
		all_tasks = TaskAPI.query.all()
		result = tasks_schema.dump(all_tasks)
		return jsonify(result)
	else:
		return jsonify({'title': None, 'description': None, 'id': None, 'create_date': None}), 400