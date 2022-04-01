import time
from src.executing import SwPipe
from config import SCRIPT_PATH
import sys

class GetCom():

    def __init__(self,script_name,send):
        self.e = SwPipe("powershell.exe", self.event, self.exit, self.ready)
        self._path = SCRIPT_PATH
        self._script_name = script_name
        self._send = send

    def event(self, line):
        lines = line.replace("\r\n", "")
        self._send(lines)
        # sys.stdout.write(line)

    def exit(self, msg):
        print(msg)

    def ready(self):
        self.e.write(f"cd {self._path}")  # 进入项目目录
        self.e.write("./venv/Scripts/activate") #激活虚拟环境
        # self.e.write(f"python ./{self._script_name} {self._key}")
        self.e.write(f"robot {self._path}{self._script_name}")
        self.e.write("exit")

    def run(self):
        self.e.start()


if __name__ == '__main__':
    g = GetCom("\\test_cases\智慧安监")
    g.run()

