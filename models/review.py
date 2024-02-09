#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
        @place_id: string - empty string or the Place id
        @user_id: string - empty string or the User id
        @text: string - might be empty string
    """
    place_id = ""
    user_id = ""
    text = ""
