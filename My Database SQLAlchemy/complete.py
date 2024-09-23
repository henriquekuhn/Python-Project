import unittest
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, Float, String, Column
import os

DIR = os.path.join(os.getcwd(), "My Database SQLAlchemy")
os.chdir(DIR)

# Connecting to the Database
FILE_NAME = 'tests_database.db'
DATABASE_FILENAME = 'sqlite:///tests_database.db'
engine = sqlalchemy.create_engine(DATABASE_FILENAME, echo=True)

# Maping Declaration
Base = declarative_base()

class Tests(Base):
    __tablename__ = 'tests' # Obrigatory
    id = Column(Integer, primary_key=True) # Obrigatory
    test_name = Column(String(50))
    test_temp = Column(Float)
    test_voltage = Column(Float)
    low_condition = Column(Float)
    high_condition = Column(Float)
    test_result = Column(Float)

# Create the table in the my_database database
## Check if the database exists

db_exists = os.path.exists(os.path.join(DIR, FILE_NAME))
print(db_exists)
if not db_exists:
    print("Creating my_database database...")
    Base.metadata.create_all(engine)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()
    
tests = []
running = True
while(running):
    flag = int(input("1. Add new SiP test. \n2. To commit registration. \n3. To check the database. \n4. Check by filter \n5. Exit\n\n"))

    if flag == 1:
        # Create a list of users
        test_name = input("Test Name: ")
        test_temp = float(input("Test Temperature: "))
        test_voltage = float(input("Test Voltage: "))
        test_result = float(input("Test Result: "))

        if 10 <= test_temp <= 30:
            low_condition = 0.5
            high_condition = 1.5
        
        elif test_temp < 18:
            low_condition = 0.2
            high_condition = 1.2

        else:
            low_condition = 0.8
            high_condition = 1.8

        
        tests.append(Tests(test_name=test_name, test_temp=test_temp, test_voltage=test_voltage,
                               low_condition=low_condition, high_condition=high_condition, test_result=test_result))

    elif flag == 2:
        session.add_all(tests)
        session.commit()

    elif flag == 3:
        # Query the database
        tests_db = session.query(Tests).all()
        for test in tests_db:
            print(f'ID: {test.id}, Test Name: {test.test_name}, Test Temperature: {test.test_temp}, '
                  f'Test Voltage: {test.test_voltage}, Low Condition: {test.low_condition},'
                  f'High Condition: {test.high_condition}, Test Result: {test.test_result}')

    elif flag == 4:
        query_flag = int(input("Query by: 1. Name 2. Style\n"))
        if query_flag == 1:
            query_name = input("Enter the recipe name to query: ")
            #queried_recipes = session.query(Tests).filter(Tests.test_name.ilike(f"%{query_name}%")).all()
            queried_recipes = session.query(Tests).filter(Tests.test_name()
            for test in queried_recipes:
                print(f'ID: {test.id}, Test Name: {test.test_name}, Test Temperature: {test.test_temp}, '
                  f'Test Voltage: {test.test_voltage}, Low Condition: {test.low_condition},'
                  f'High Condition: {test.high_condition}, Test Result: {test.test_result}')
        elif query_flag == 2:
            query_style = input("Enter the style to query: ")
            queried_recipes = session.query(Tests).filter(Tests.style.ilike(f"%{query_style}%")).all()
            for recipe in queried_recipes:
                print(f'ID: {recipe.id}, Name: {recipe.name}, Style: {recipe.style}, Version: {recipe.version}')

    else:
        running = False

