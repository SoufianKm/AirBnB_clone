#!/usr/bin/python3
""" class User """


from models.base_model import BaseModel


class User(BaseModel):
    """ Class User based on BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
