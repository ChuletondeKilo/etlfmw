import yaml
from .schema import PipelinesConfigSchema
from pathlib import Path
from .. import common

with Path(f"{common.cwd}/config/config.yaml").open('r') as f:
    config_data = yaml.safe_load(f)
    config: PipelinesConfigSchema = PipelinesConfigSchema(**config_data)

pipelines = config.pipelines_list()

