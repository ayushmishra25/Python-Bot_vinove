
import json

class ConfigManager:
    def _init_(self, config_file="config.json"):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def update(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)