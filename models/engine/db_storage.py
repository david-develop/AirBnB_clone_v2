#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
    __engine = None
    __session = None
    """
    __engine = None
    __session = None
    obj_list = {State, City, User, Place, Review, Amenity}

    def __init__(self):
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary (like FileStorage)
        """
        my_dict = {}
        if cls is None:
            for obj_value in self.obj_list:
                my_list = self.__session.query(obj_value).all()
                for obj in my_list:
                    my_dict.update({"{}.{}".format(type(obj).__name__,
                                                   obj.id): obj})
        else:
            if type(cls) is str:
                cls = eval(cls)
            my_list = self.__session.query(cls).all()
            for obj in my_list:
                my_dict.update({"{}.{}".format(type(obj).__name__,
                                               obj.id): obj})
        return my_dict

    def new(self, obj):
        """add the object to the current database
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """deserialize the JSON file path
        """
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
