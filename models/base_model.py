#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class for models with common attributes.

    Attributes:
        id (uuid.UUID): A unique identifier generated using UUID4.
        created_at (datetime.datetime): The timestamp when the model instance was created.
        updated_at (datetime.datetime): The timestamp when the model instance was last updated.

    Methods:
        __init__: Initializes a BaseModel instance.

    Example Usage:
        >>> base_model = BaseModel()
        >>> print(base_model.id)
        a1f90b6a-47b0-4d2d-9894-07ae075c34b7
        >>> print(base_model.created_at)
        2023-10-12 15:32:18.764742
        >>> print(base_model.updated_at)
        2023-10-12 15:32:18.764742
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Keyword Args:
            id (uuid.UUID, optional): A pre-defined UUID for the instance.
            created_at (str, optional): A string representing the creation timestamp in ISO 8601 format.
            updated_at (str, optional): A string representing the update timestamp in ISO 8601 format.

        Note:
            If no arguments are provided, the instance will be initialized with a new UUID and current timestamps.

            If 'created_at' and 'updated_at' are provided as strings, they will be converted to datetime objects.

        Example Usage:
            >>> base_model = BaseModel()
            >>> custom_uuid = uuid.UUID('550e8400-e29b-41d4-a716-446655440000')
            >>> base_model = BaseModel(id=custom_uuid, created_at='2023-10-12T15:32:18.764742', updated_at='2023-10-12T15:32:18.764742')
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.now().strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time, and saves the object to storage.

        Args:
            self: The instance of the object.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object into a dictionary representation for easy serialization.

        Args:
            self: The instance of the object.

        Returns:
            dict: A dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Args:
            self: The instance of the object.

        Returns:
            str: A string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
