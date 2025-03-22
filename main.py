import etlfmw
from etlfmw.connections import main

print(main.conn_manager)
# pipeline = Pipeline(steps=[Extractor(connection=ConnectionPostgre(config['postgres']))])
# pipeline.run()



# connector = ConnectionPostgre()
# extractor = Extractor(connection=connector)
# print(extractor.extract())
