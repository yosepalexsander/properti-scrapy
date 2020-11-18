# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from rumah_scrapper.models import db_connect, init_db, Properti


class RumahScrapperPipeline:
    def __init__(self):
        """
        Initializes database connection and Session object
        """
        engine = db_connect()
        init_db(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save scrapped data to database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        data = Properti(**item)

        try:
            session.add(data)
            session.commit()

        except IntegrityError:
            print("Property ID has been added")

        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
