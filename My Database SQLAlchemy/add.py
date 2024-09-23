import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, String, Column
import os

# Define the database directory and filename
DIR = os.path.join(os.getcwd(), "My Database SQLAlchemy")
os.chdir(DIR)

# Connecting to the existing database
DATABASE_URL = 'sqlite:///test.db'
engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)

# Mapping declaration
Base = declarative_base()

# Define the User class to map to the 'users' table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

# Query the database
users = session.query(User).all()
for user in users:
    print(f'ID: {user.id}, Name: {user.name}, Fullname: {user.fullname}, Age: {user.age}')

# Example: Add a new user
new_user = User(name='Thor', fullname='God of Thunder', age=1500)
session.add(new_user)
session.commit()

# Query the database again to see the new user
users = session.query(User).all()
for user in users:
    print(f'ID: {user.id}, Name: {user.name}, Fullname: {user.fullname}, Age: {user.age}')