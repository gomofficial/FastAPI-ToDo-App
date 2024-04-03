from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException

class NotFoundError(HTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)