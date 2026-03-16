from sqlalchemy import Column, Integer, String, Float, Date
from backend.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)

    tmdb_id = Column(Integer, unique=True, index=True, nullable=False)

    title = Column(String, nullable=False)
    original_title = Column(String)
    release_date = Column(Date)
    overview = Column(String)
    poster_path = Column(String)
    backdrop_path = Column(String)
    vote_average = Column(Float)
    vote_count = Column(Integer)
    language = Column(String)