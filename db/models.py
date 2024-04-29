from uuid import uuid4
from .engine import Base
from sqlalchemy import (ForeignKey, Column, Integer, String, Boolean, UUID, Table)
from sqlalchemy.orm import relationship
from typing import List,Optional

class User(Base):
    __tablename__ = 'users'
    
    id            = Column(UUID, primary_key=True, default=uuid4)
    # username      = Column(String, unique=True, nullable=False)
    # email         = Column(String, unique=True, nullable=False)
    # password      = Column(String, nullable=False)
    # is_staff      = Column(Boolean, default=False)
    # is_active     = Column(Boolean, default=False)

    # def __repr__(self):
    #     return f"<User {self.username}"   


class Category(Base):
    __tablename__ = 'categories'

    # name          = Column(String, unique=True, nullable=False)
    # user_id       = Column(UUID, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    # user          = relationship("User")
    id            = Column(UUID, primary_key=True, default=uuid4)

    # def __repr__(self):
    #     return f"<Category {self.name}"


class Task(Base):
    __tablename__ = 'tasks'

    # name          = Column(String, unique=True, nullable=False)
    # description   = Column(String, unique=True, nullable=False)
    # user          = relationship("User")
    # category      = relationship("Category")
    # user_id       = Column(UUID, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    # cat_id        = Column(UUID, ForeignKey("categories.id",ondelete="CASCADE"), nullable=False)
    id            = Column(UUID, primary_key=True, default=uuid4)

    # def __repr__(self):
    #     return f"<Task {self.name}"
    
