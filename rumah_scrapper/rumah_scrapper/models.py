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

    __tablename__ = "properti"

    id = Column(Integer, primary_key=True)
    property_id = Column("property_id", BigInteger, unique=True)
    bedroom = Column("bedroom", Integer)
    bathroom = Column("bathroom", Integer)
    building_area = Column("building_area", Integer)
    surface_area = Column("surface_area", Integer)
    locality = Column("locality", String(300))
    province = Column("province", String(300))
    price = Column("price", BigInteger)
