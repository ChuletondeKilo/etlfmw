import etlfmw
from etlfmw.connections import config

print(config.conn_manager)
# pipeline = Pipeline(steps=[Extractor(connection=ConnectionPostgre(config['postgres']))])
# pipeline.run()



# connector = ConnectionPostgre()
# extractor = Extractor(connection=connector)
# print(extractor.extract())
