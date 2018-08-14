import os


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
            os.mkdir("D:\\{0}".format(folder_name))
        except OSError:
            print("Failed to make folder")
