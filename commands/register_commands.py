import requests
import yaml

TOKEN = "MTI0MjI4OTk5OTkyNDMwMTk3Nw.Gah361.nGKVdC_Z7qbjUvYARTe9XTkMSr3PPZyZcsOzao"
APPLICATION_ID = "1242289999924301977"
URL = f"https://discord.com/api/v9/applications/{1242289999924301977}/commands"


with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# Send the POST request for each command
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")
