import yaml
from .schema import ConnectionsConfigSchema, EnvironmentCollectionNameEnum
from enum import Enum
from pathlib import Path
from .. import common

with Path(f"{common.cwd}/connections/connections.yaml").open('r') as f:
    config_data = yaml.safe_load(f)
    config = ConnectionsConfigSchema(**config_data)
    available_connections = Enum('ConnEnum', config.connections.environments[EnvironmentCollectionNameEnum['DEV']].gather_conn_names())
