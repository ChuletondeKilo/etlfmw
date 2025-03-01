from etlfmw.extractors.extractor import Extractor
from etlfmw.connections.postgres import ConnectionPostgre
from yaml import safe_load

with open('./config.yaml') as f:
    config = safe_load(f)

pipeline = Pipeline(steps=[Extractor(connection=ConnectionPostgre(config['postgres']))])
pipeline.run()



# connector = ConnectionPostgre()
# extractor = Extractor(connection=connector)
# print(extractor.extract())
