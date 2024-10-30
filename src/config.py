
import json

def load_config(config_path):
    with open(config_path, "r") as file:
        return json.load(file)

def load_messages(messages_path):
    with open(messages_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data["mensagens"]
