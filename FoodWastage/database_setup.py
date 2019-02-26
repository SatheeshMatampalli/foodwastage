from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()


class UserComplaint(Base):
    __tablename__ = 'usercomplaint'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    message = Column(String(2000), nullable=False)
    # confirmpassword = Column(String(250), nullable=False)



engine = create_engine('sqlite:///Foodwastage.db')

Base.metadata.create_all(engine)