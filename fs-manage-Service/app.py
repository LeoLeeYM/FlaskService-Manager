from flask import Flask, jsonify, Blueprint, request
import json
from flask_cors import CORS
import subprocess
import os
import base64
import utils

appp = Flask(__name__)
CORS(appp)

@appp.route('/login', methods=['POST'])
def login():
    global userId, pwd

    data = request.get_json()

    if data.get('userId') == utils.getConfig('userId') and data.get('pwd') == utils.getConfig('pwd'):
        token = str(base64.b32encode(os.urandom(24)).hex())
        response = {
            'status': 'success',
            'token': token
        }
        utils.setConfig('token', token)
    else:
        response = {
            'status': 'failure',
            'message': 'Invalid credentials'
        }

    return jsonify(response)

@appp.route('/listTask', methods=['GET'])
def list_task():
    if request.headers.get('Authorization') == f'Bearer {utils.getConfig("token")}':
        return jsonify(utils.getTaskList()), 200
    else:
        return jsonify({'error': 'Invalid token'}), 401
    
@appp.route('/getTask', methods=['GET'])
def get_task():
    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401
    
    task_id = request.args.get('taskId')
    task = utils.getTask(task_id)

    if task:
        log_path = f'./taskLog/{task["pid"]}.log'
        log_data = None

        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                log_data = log_file.read()

        response = {
            'task': task,
            'logData': log_data
        }

        return jsonify(response)
    else:
        return jsonify({'error': 'Task not found'}), 404

@appp.route('/runTask', methods=['GET'])
def run_task():
    task_id = request.args.get('taskId')

    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401

    task = utils.getTask(task_id)
    if task:
        with open('./configs/transferRun.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                "path": task['path'],
                "taskId": task['id']
            }))
            f.close()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Task not found'}), 404

@appp.route('/closeTask', methods=['GET'])
def close_task():
    task_id = request.args.get('taskId')

    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401

    task = utils.getTask(task_id)
    if task:
        utils.setTask(task['id'], 'isRun', False)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Task not found'}), 404
    
@appp.route('/createTask', methods=['POST'])
def create_task():
    data = request.get_json()

    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401

    utils.addTask({
        "title": data["title"],
        "remark": data["remark"],
        "isRun": False,
        "pid": None,
        "path": data["path"]
    })

    return jsonify({'status': 'success'})

@appp.route('/delTask', methods=['GET'])
def del_task():
    task_id = request.args.get('taskId')

    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401

    task = utils.getTask(task_id)
    if task:
        utils.delTask(task['id'])
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Task not found'}), 404
    
@appp.route('/editTask', methods=['POST'])
def edit_task():
    data = request.get_json()

    if not utils.checkToken(request.headers.get('Authorization')):
        return jsonify({'error': 'Invalid token'}), 401

    utils.editTask(data["taskId"] ,{
        "title": data["title"],
        "remark": data["remark"],
        "isRun": False,
        "pid": None,
        "path": data["path"]
    })

    return jsonify({'status': 'success'})

    
# 启动服务器
if __name__ == '__main__':
    appp.run(port=6060, host="0.0.0.0", debug=True)