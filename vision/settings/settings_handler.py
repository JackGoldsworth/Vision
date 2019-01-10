import json


class SettingsHandler:
    settings = {}
    file_name = None

    def load_settings(self, file_name):
        self.file_name = file_name
        with open(file_name) as file:
            self.settings = json.load(file)
        print(self.settings)

    def save_settings(self):
        with open(self.file_name, "w") as file:
            json.dump(self.settings, file, indent=2)

    def change_settings(self, application, setting, value):
        self.settings[application][setting] = value

    def get_setting(self, application, setting):
        return self.settings[application][setting]
