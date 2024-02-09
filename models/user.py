#!/usr/bin/python3
""" class User """


from base_model import BaseModel


class User(base_model.BaseModel):
    """ Class User based on BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
