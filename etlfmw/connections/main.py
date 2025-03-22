import yaml
from .schema import ConnectionsConfigSchema, EnvironmentCollectionNameEnum
from os import getcwd
from pathlib import Path
from .base import connectionsManager

with Path(getcwd() + "/connections.yaml").open('r') as f:
    config_data = yaml.safe_load(f)
    config: ConnectionsConfigSchema = ConnectionsConfigSchema(**config_data)

conn_manager: connectionsManager = connectionsManager(config.connections.environments[EnvironmentCollectionNameEnum['DEV']])
conn_manager.instantiate_connections()
