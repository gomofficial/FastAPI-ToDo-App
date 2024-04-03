from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class UserNotFoundError(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail="User not found"