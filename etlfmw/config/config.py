import yaml
from .schema import PipelinesConfigSchema

with open("./config.yaml", 'r') as f:
    config_data = yaml.safe_load(f)
    config = PipelinesConfigSchema(**config_data)
