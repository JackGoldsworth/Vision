import os
from pathlib import Path


class DesktopHandler:

    def __init__(self, folder_name):
        self.create_folder(folder_name)

    def open_program(self, program_name):
        try:
            os.startfile(program_name)
        except OSError:
            print("File failed to open")

    def close_program(self, program_name):
        try:
            os.system("TASKKILL /F /IM {0}.exe".format(program_name))
        except OSError:
            print("File failed to close")

    def create_folder(self, folder_name):
        try:
            paths = [Path("D:\\{0}".format(folder_name)), Path("C:\\{0}".format(folder_name))]
            for i in range(2):
                if paths[i].exists():
                    continue
                else:
                    os.mkdir(paths[i])
                    break
        except OSError:
            print("Failed to make folder")
