from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String, Field, DateTime
from apiflask.validators import Length, OneOf
from marshmallow_dataclass import dataclass
from dataclasses import  field
from datetime import datetime
from typing import Any
app = APIFlask(__name__)

@dataclass
class BaseResponseSchema(Schema):
    data:Any = field(metadata={'required': False,})  
    message:str = field()
    code:int = field()

@dataclass
class JobRawInSchema(Schema):
    detail_url:str = field()
    category:str = field()
    job_title:str = field() 
    company:str = field() 
    location:str =field() 
    from_where:str = field()
    crawled_time:datetime = field() 
    post_time:datetime = field()
    category:str = field()
    salary:str = field()
    extra:str = field()
    raw:str = field()



app.config['BASE_RESPONSE_SCHEMA'] = BaseResponseSchema
# the data key should match the data field name in the base response schema
# defaults to "data"
app.config['BASE_RESPONSE_DATA_KEY'] = 'data'





#from flask import Flask
from models.datamodels import JobRawData
app = APIFlask(__name__)
from sqlalchemy.orm import Session

from sqlalchemy.ext.asyncio import create_async_engine

from jobaggrv_common import get_db_url
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    get_db_url(),
    echo=True,
)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

from dataclasses import asdict
async def jobrawdatasave(data: JobRawInSchema):
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                   JobRawData(**asdict(data)) 
                ]
            )

        await session.commit()
import asyncio

import asyncio_gevent
from asyncio_gevent import async_to_sync

asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())


@app.post("/JoBRawData/")
@app.input(JobRawInSchema.Schema)
@app.output(BaseResponseSchema.Schema,201)
def job_raw_data_create(data: JobRawInSchema):
    res = async_to_sync(jobrawdatasave)(data) 
    return {
        'message': 'Data created.',
        'code': 20101
    }
