import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ExecutionLogs(Base):
    __tablename__ = 'execution_logs'

    execution_id = sa.Column(sa.String, primary_key=True)

    def __repr__(self):
        return f"<ExecutionLogs(execution_id={self.execution_id})>"

# Database connection string
DATABASE_URL = 'postgresql://postgres:Rotiman1*@localhost/postgres'

# Create an engine
engine = sa.create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

table_mapping = {
    'execution_logs': ExecutionLogs
}

# Function to log a message
def log_message(table, execution_id):
    new_log = table_mapping[table](execution_id=execution_id)
    session.add(new_log)
    session.commit()
    print(f"Logged message: {execution_id}")

__all__ = ['log_message']