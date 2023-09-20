from models.basemodel import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Text, DateTime, Boolean, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    topic = Column(String)
    title = Column(String)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))  # ForeignKey referencing User.id
    date_posted = Column(DateTime)

    def __init__(self, *args, **kwags):
        """
        init user
        """
        super().__init__(*args, **kwags)
