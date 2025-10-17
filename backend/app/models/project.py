from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    long_description = Column(Text, nullable=True)
    technologies = Column(String)
    github_url = Column(String, nullable=True)
    live_url = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
