import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, Float, String, Column, desc
import os


#DIR = os.path.join(os.getcwd(), "My Database SQLAlchemy")
DIR = "C:\\Users\\adm_cafrunikuhn\\Desktop\\Henrique\\Repositories\\Python-Projects\\My Database SQLAlchemy"
print(DIR)
print(os.getcwd())
if os.getcwd() != DIR:
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

class DatabaseManagement:
    def create_db(self):
        # Create the table in the my_database database
        ## Check if the database exists
        self.db_exists = os.path.exists(os.path.join(DIR, FILE_NAME))
        if not self.db_exists:
            print("Creating my_database database...")
            Base.metadata.create_all(engine)

    def initiate_db_session(self):
        # Create database session
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_test(self, test_name, test_temp, test_voltage, low_condition, high_condition, test_result):    
        tests = []
        tests.append(Tests(test_name=test_name, test_temp=test_temp, test_voltage=test_voltage,
            low_condition=low_condition, high_condition=high_condition, test_result=test_result))

        self.session.add_all(tests)
        self.session.commit()

        return "Test create success."

    def query_test(self):
        # Query the database
        tests_db = self.session.query(Tests).all()
        db_size = len(tests_db)
        #for test in tests_db:
        #    print(f'ID: {test.id}, Test Name: {test.test_name}, Test Temperature: {test.test_temp}, '
        #          f'Test Voltage: {test.test_voltage}, Low Condition: {test.low_condition},'
        #          f'High Condition: {test.high_condition}, Test Result: {test.test_result}')
        return db_size

    def query_by_filter(self, column_search, query_filter):  
        query_filter = query_filter
        column_search = column_search  
        column = getattr(Tests, column_search)
        tests_db = self.session.query(Tests).filter(column == query_filter).order_by(desc(Tests.id)).first()

        #for test in tests_db:
        #    print(f'ID: {test.id}, Test Name: {test.test_name}, Test Temperature: {test.test_temp}, '
        #          f'Test Voltage: {test.test_voltage}, Low Condition: {test.low_condition},'
        #          f'High Condition: {test.high_condition}, Test Result: {test.test_result}')
        return getattr(tests_db, column_search)

    def edit_register(self, column_search, query_item, new_value):
        column = getattr(Tests, column_search)
        edit_db = self.session.query(Tests).filter(column == query_item).order_by(desc(Tests.id)).first()       
        edit_db.test_name = new_value
        self.session.commit()
        new_value_db = self.session.query(Tests).filter(column == new_value).order_by(desc(Tests.id)).first()
        return getattr(new_value_db, column_search)
    
    def delete_regiter(self, column_search, query_item):
        column = getattr(Tests, column_search)
        delete_db_list = self.session.query(Tests).filter(column == query_item).all()
        if delete_db_list:
            for delete_db in delete_db_list:
                self.session.delete(delete_db)

            self.session.commit()        
            deleted_db = self.session.query(Tests).filter(column == query_item).order_by(desc(Tests.id)).first()
            return deleted_db
        else:
            return "No items found matching the provided criteria."

        return deleted_db