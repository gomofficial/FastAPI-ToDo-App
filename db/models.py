from uuid import uuid4, UUID
from .engine import Base
from sqlalchemy import (ForeignKey, Column, Table)
from sqlalchemy.orm import relationship,Mapped,mapped_column
from typing import List,Optional

class User(Base):
    __tablename__ = 'users'

    username: Mapped[str]       = mapped_column(unique=True, nullable=False)
    email: Mapped[str]          = mapped_column(unique=True, nullable=False)
    password: Mapped[str]       = mapped_column(nullable=False)
    is_staff: Mapped[bool]      = mapped_column(default=False)
    is_active: Mapped[bool]     = mapped_column(default=False)
    id: Mapped[UUID]            = mapped_column(primary_key=True, default_factory=uuid4)


    def __repr__(self):
        return f"<User {self.username}"   


class Category(Base):
    __tablename__ = 'categories'

    name: Mapped[str]         = mapped_column(unique=True, nullable=False)
    user_id:Mapped[UUID]      = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    user: Mapped["User"]      = relationship("User")
    id: Mapped[UUID]          = mapped_column(primary_key=True, default_factory=uuid4)

    def __repr__(self):
        return f"<Category {self.name}"


class Task(Base):
    __tablename__ = 'tasks'

    name: Mapped[str]              = mapped_column(nullable=False)
    description: Mapped[str]       = mapped_column()
    user: Mapped["User"]           = relationship("User")
    category: Mapped["Category"]   = relationship("Category")
    user_id: Mapped[UUID]          = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    cat_id: Mapped[UUID]           = mapped_column(ForeignKey("categories.id",ondelete="CASCADE"))
    id: Mapped[UUID]               = mapped_column(primary_key=True, default_factory=uuid4)

    def __repr__(self):
        return f"<Task {self.name}"

