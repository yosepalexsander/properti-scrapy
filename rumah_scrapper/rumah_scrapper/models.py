from sqlalchemy import Column, BigInteger, Integer, String, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import rumah_scrapper.settings as settings

Base = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE), convert_unicode=True)


def init_db(engine):
    Base.metadata.create_all(engine)


class Properti(Base):
    """Sqlalchemy model for Rumah data"""

    __tablename__ = "rumah"

    id = Column(Integer, primary_key=True)
    property_id = Column("property_id", BigInteger, unique=True)
    bedroom = Column("bedroom", Integer, nullable=True)
    bathroom = Column("bathroom", Integer, nullable=True)
    building_area = Column("building_area", Integer, nullable=True)
    surface_area = Column("surface_area", Integer, nullable=True)
    locality = Column("locality", String(300), nullable=True)
    province = Column("province", String(300), nullable=True)
    price = Column("price", BigInteger, nullable=True)
