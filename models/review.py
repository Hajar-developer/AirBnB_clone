#!/usr/bin/python3

"""

Implementation of Review class

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Implementing for the Review
    """

    place_id = ""
    user_id = ""
    text = ""
