import time

import redis

from src.executing import SwPipe

r = redis.Redis(host='127.0.0.1', port=6379, db=4, decode_responses=True)


class GetCom():

    def __init__(self, key, path, script_name):
        self.e = SwPipe("powershell.exe", self.event, self.exit, self.ready)
        self._key = key
        self._path = path
        self._script_name = script_name

    def event(self, cls, line):
        lines = time.strftime('%Y-%m-%d %H-%M-%S') + ":" + line.replace("\r\n", "")
        # 写入redis
        # r.lpush(self._key, lines)
        # sys.stdout.write(line)

    def exit(self, msg):
        print(msg)

    def ready(self):
        # self.e.write("cd D:\PycharmProjects\AutomatedTesting")  # 执行
        self.e.write(f"cd {self._path}")  # 执行
        self.e.write("./venv/Scripts/activate")
        # self.e.write("python ./suiteMain.py")
        self.e.write(f"python ./{self._script_name} {self._key}")
        self.e.write("exit")

    def run(self):
        self.e.start()


if __name__ == '__main__':
    g = GetCom("time1")
    g.run()
