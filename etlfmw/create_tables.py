from common import Base, engine

# Example of creating the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tables created successfully.")