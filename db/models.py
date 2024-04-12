from uuid import uuid4, UUID
from .engine import Base
from sqlalchemy import (ForeignKey, Column, Table)
from sqlalchemy.orm import relationship,Mapped,mapped_column
from typing import List,Optional


association_table = Table(
    "association_table",
    Base.metadata,
    Column("categories", ForeignKey("categories.id", ondelete="CASCADE"), primary_key=True),
    Column("tasks", ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True))


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str]       = mapped_column(unique=True, nullable=False)
    email: Mapped[str]          = mapped_column(unique=True, nullable=False)
    password: Mapped[str]       = mapped_column(nullable=False)
    categories: Mapped[List["Category"]] = relationship(back_populates="user")
    tasks: Mapped[List["Task"]] = relationship(back_populates="user")
    is_staff: Mapped[bool]      = mapped_column(default=False)
    is_active: Mapped[bool]     = mapped_column(default=False)
    id: Mapped[UUID]            = mapped_column(primary_key=True, default_factory=uuid4)


    def __repr__(self):
        return f"<User {self.username}"   


class Category(Base):
    __tablename__ = 'categories'

    name: Mapped[str]         = mapped_column(unique=True, nullable=False)
    user_id:Mapped[UUID]       = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    user: Mapped["User"]      = relationship(back_populates="categories")
    tasks: Mapped[List["Task"]] = relationship(
        secondary=association_table, back_populates="categories")
    id: Mapped[UUID]          = mapped_column(primary_key=True, default_factory=uuid4)

    def __repr__(self):
        return f"<Category {self.name}"

class Task(Base):
    __tablename__ = 'tasks'

    name: Mapped[str]         = mapped_column(nullable=False)
    description: Mapped[str]  = mapped_column()
    user_id:Mapped[UUID]       = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    user: Mapped["User"]      = relationship(back_populates="tasks")
    
    categories: Mapped[List["Category"]] = relationship(
        secondary=association_table, back_populates="tasks")
    id: Mapped[UUID]          = mapped_column(primary_key=True, default_factory=uuid4)

    def __repr__(self):
        return f"<Task {self.name}"
 