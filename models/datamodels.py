from sqlalchemy import Boolean, Column,DateTime, Integer, Text, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class JobRawData(Base):
    __tablename__ = "jobarrgv_jobrawdata"

    id = Column('id', Integer, primary_key=True, index=True)
    detail_url = Column('detail_url',String)
    job_title = Column('job_title',String)
    company = Column('company',String)
    location = Column('location',String)
    from_where = Column('from_where',String)
    crawled_time = Column('crawled_time',DateTime)
    post_time = Column('post_time',DateTime)
    category = Column('category',String)
    extra = Column('extra',Text)
    raw = Column('raw',Text)
    salary = Column('salary',String)
    

