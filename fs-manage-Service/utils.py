# 用于储存全局方法
import json

def checkToken(token):
    if token == f'Bearer {getConfig("token")}':
        return True
    else:
        return False

def getConfig(key = None):
    if key:
        with open('./configs/config.json', 'r', encoding="utf-8") as task_file:
            return json.load(task_file)[key]
    else:
        with open('./configs/config.json', 'r', encoding="utf-8") as task_file:
            return json.load(task_file)
    
def setConfig(key, data):
    res = getConfig()
    res[key] = data
    with open('./configs/config.json', 'w', encoding="utf-8") as task_file:
        task_file.write(json.dumps(res))

def getTaskList() -> list:
    with open('./configs/task.json', 'r', encoding="utf-8") as task_file:
        return json.load(task_file)

def getTask(id: int) -> dict:
    with open('./configs/task.json', 'r', encoding="utf-8") as task_file:
        for i in json.load(task_file):
            if str(i['id']) == str(id):
                return i
        return None

def saveTask(data):
    with open('./configs/task.json', 'w', encoding="utf-8") as task_file:
        task_file.write(json.dumps(data))

def setTask(id, key, data):
    task = getTaskList()
    for i in range(len(task)):
        if task[i]['id'] == id:
            task[i][key] = data
            break
    saveTask(task)

def addTask(data):
    res = getTaskList()
    data["id"] = len(res) + 1
    res.append(data)
    saveTask(res)

def delTask(id):
    res = getTaskList()
    for i, v in enumerate(res):
        if v["id"] == id:
            res.pop(i)
            break
    saveTask(res)

def editTask(id, data) -> dict:
    res = getTaskList()
    for i, v in enumerate(res):
        if v["id"] == id:
            res[i]['title'] = data['title']
            res[i]['remark'] = data['remark']
            res[i]['path'] = data['path']
            break
    saveTask(res)
    
def getProcessList() -> list:
    with open('./configs/process.json', 'r', encoding="utf-8") as process_file:
        return json.load(process_file)
    
def getProcess(pid: int) -> dict:
    with open('./configs/process.json', 'r', encoding="utf-8") as process_file:
        for i in json.load(process_file):
            if i['pid'] == pid:
                return i
        return None