import subprocess
import multiprocessing.dummy as multiprocessing
import atexit
import utils
import json
import os
import signal
import time, threading

# 存储运行的进程的字典
running_processes = {}

def run_flask_server(script_path, task_id):
    # 使用subprocess.Popen启动Flask服务器
    process = subprocess.Popen(['python', "-Xfrozen_modules=off", script_path],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               text=True,
                               bufsize=1,
                               universal_newlines=True,
                               creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0)

    pid = process.pid
    utils.setTask(task_id, 'pid', pid)
    utils.setTask(task_id, 'isRun', True)

    # 实时获取输出并保存到文件，使用PID作为文件名
    output_filename = f'./taskLog/{pid}.log'

    def cleanup():
        # 在退出时结束 Flask 服务器
        process.terminate()
        process.wait()

    # 注册退出处理函数
    atexit.register(cleanup)

    def listen_is_run():
        if utils.getTask(task_id) is None:
            return
        while utils.getTask(task_id)['isRun']:
            time.sleep(0.1)

        process.send_signal(signal.CTRL_BREAK_EVENT)

    # 启动监听线程
    is_run_thread = threading.Thread(target=listen_is_run)
    is_run_thread.start()

    try:
        for line in process.stdout:
            with open(output_filename, 'a', encoding="utf-8") as output_file:
                print(f"{pid}: {line.strip()}")  # 在控制台输出
                output_file.write(line.strip() + '\n')
                if utils.getTask(task_id) is None:
                    continue
                if not utils.getTask(task_id)['isRun']:
                    process.send_signal(signal.CTRL_BREAK_EVENT)
                    break  # 根据标志安全退出
    except KeyboardInterrupt:
        pass
    finally:
        utils.setTask(task_id, 'isRun', False)

    # 获取进程的返回代码
    return process.returncode

def run_flask_server_in_process(script_path, task_id):
    process = multiprocessing.Process(target=run_flask_server, args=(script_path, task_id))
    process.start()

    # 存储进程对象到字典
    running_processes[task_id] = {'process': process}

if __name__ == '__main__':

    for i in utils.getTaskList():
        utils.setTask(i['id'], 'isRun', False)

    run_flask_server_in_process("app.py", 0)

    while True:
        have_task = False
        with open('./configs/transferRun.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            if file_content != '':
                data = json.loads(file_content)
                path, task_id = data['path'], data['taskId']
                have_task = True
                run_flask_server_in_process(path, task_id)

        if have_task:
            with open('./configs/transferRun.json', 'w', encoding='utf-8') as f2:
                f2.write('')
