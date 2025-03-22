import yaml
from .schema import ConnectionsConfigSchema, EnvironmentCollectionNameEnum
from enum import Enum
from pathlib import Path
from ..common import cwd
from .base import connectionsManager

with Path(f"{cwd}/connections/connections.yaml").open('r') as f:
    config_data = yaml.safe_load(f)
    config: ConnectionsConfigSchema = ConnectionsConfigSchema(**config_data)
    available_connections = Enum('ConnEnum', config.connections.environments[EnvironmentCollectionNameEnum['DEV']].gather_conn_names())

conn_manager: connectionsManager = connectionsManager(config.connections.environments[EnvironmentCollectionNameEnum['DEV']])
conn_manager.instantiate_connections()
