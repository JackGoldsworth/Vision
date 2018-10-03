import json

from .command_info import CommandInfo


class CommandParser:
    commands = {}

    def get_command_file(self, file_name):
        """
        Loads all of the commands and their properties
        from the commands.json file.

        :param file_name: the file name
        """
        with open(file_name) as file:
            json_file = json.loads(file)
            for command in json_file:
                self.commands[command] = CommandInfo(command["definition"], command["usage"], command["parser"])

    def list_commands(self):
        """
        Prints out a list of all of the commands loaded.
        """
        for name, info in self.commands.items():
            print("**Command Name: %(name)s\nDescription: %(description)s\nUsage: %(usage)s\n", name=name,
                  description=info().description, usage=info().usage)
