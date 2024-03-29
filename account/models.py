
from ..db.engine import Base
from sqlalchemy import (ForeignKey)
from sqlalchemy.orm import relationship,Mapped,mapped_column


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int]         = mapped_column(primary_key=True)
    username: Mapped[str]   = mapped_column(unique=True, nullable=False)
    email: Mapped[str]      = mapped_column(unique=True, nullable=False)
    password: Mapped[str]   = mapped_column(nullable=False)
    is_staff: Mapped[bool]  = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<User {self.username}"
    

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int]         = mapped_column(primary_key=True, index=True)
    name: Mapped[str]       = mapped_column(nullable=False)
    # user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


    def __repr__(self):
        return f"<Category {self.name}"


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int]         = mapped_column(Integer, primary_key=True, index=True))
    name: Mapped[str]       = mapped_column(nullable=False)
    description: Mapped[str]       = mapped_column()
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f"<Task {self.name}"