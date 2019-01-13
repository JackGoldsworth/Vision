import os
from pathlib import Path


class DesktopHandler:

    folder_name = ""

    def __init__(self, folder_name):
        self.create_folder(folder_name)
        self.folder_name = folder_name

    def open_program(self, program_name):
        """
        Opens a program in the C: directory.

        :param program_name: Program name
        """
        try:
            os.startfile("C:\\" + self.folder_name + " + \\" + program_name)
        except OSError:
            print("File failed to open")

    def close_program(self, program_name):
        """
        Closes a program using the task manager.

        :param program_name:  Program name
        """
        try:
            os.system("TASKKILL /F /IM {0}.exe".format(program_name))
        except OSError:
            print("File failed to close")

    def create_folder(self, folder_name):
        """
        Creates the folder that you put program shortcuts into
        so that they can be opened.

        :param folder_name:
        """
        path = Path("C:\\{0}".format(folder_name))
        try:
            if path.exists():
                return
            else:
                os.mkdir(path)
        except OSError:
            print("Failed to make folder")
