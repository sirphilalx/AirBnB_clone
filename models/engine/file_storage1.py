#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class responsible for handling the serialization and deserialization of objects to and from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary containing all objects in memory.

    Methods:
        all(self):
            Returns a dictionary of all objects.

        new(self, obj):
            Sets a new object in __objects.

        save(self):
            Serializes objects to JSON and saves them to the file.

        reload(self):
            Deserializes the JSON file to objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects.

        Returns:
            dict: A dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects.

        Args:
            obj: The object to be set.
        """
        return self.__objects[obj.__class__.__name__ + "." + str(obj.id)]

    def save(self):
        """
        Serializes objects to JSON and saves them to the file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """
        Deserializes the JSON file to objects.
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    # class_name = key.split('.')[0]
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            return
