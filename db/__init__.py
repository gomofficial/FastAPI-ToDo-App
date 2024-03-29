from .engine import Base
from ..account.models import User, Category, Task

__all__= [
    "Base",
    "User",
    "Category",
    "Task",
]

Base.metadata.create_all(bind=engine)

