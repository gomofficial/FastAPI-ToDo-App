from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class UserNotFoundError(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail="User not found"

class UserAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="User already exists"

class UserAuthenticationError(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="wrong username or password"

class CategoryAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="category already exists"

class CategoryDoesntExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="category does not exist"


class TaskDoesntExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="task does not exist"

class TaskAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail="task already exists"