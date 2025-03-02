import yaml
from schema import ConnectionsConfigSchema

with open("./connections.yaml", 'r') as f:
    config_data = yaml.safe_load(f)
    config = ConnectionsConfigSchema(**config_data)

print(config)