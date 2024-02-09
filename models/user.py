#!/usr/bin/python3
""" class User """


import base_model


class User(base_model.BaseModel):
    """ Class User based on BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
