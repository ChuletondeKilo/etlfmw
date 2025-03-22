import yaml
from .schema import PipelinesConfigSchema
from pathlib import Path
from os import getcwd

with Path(getcwd() + "/config.yaml").open('r') as f:
    config_data = yaml.safe_load(f)
    config: PipelinesConfigSchema = PipelinesConfigSchema(**config_data)
