


from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy import pool
from sqlalchemy.orm import sessionmaker

from configparser import ConfigParser
import os
from sqlalchemy.ext.asyncio import AsyncSession
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, 'JobAggrV/conf/config.ini')
config_obj = ConfigParser()
config_obj.read(config_path)

def get_db_url(sync=True):
    database_type = config_obj.get('database','type')
    if database_type == 'mysql':
        if sync:
            database_type = 'mysql+pymysql'
        else:
            database_type = 'mysql+aiomysql'
    database_host = config_obj.get('database','host')
    database_port = config_obj.get('database','port')
    database_name = config_obj.get('database','name')
    database_user = config_obj.get('database','user')
    database_password = config_obj.get('database','password')
    return f'{database_type}://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}'

engine = create_engine(
        get_db_url(),
        poolclass=pool.QueuePool,
    )

async_engine = create_async_engine(
        get_db_url(sync=False),
        poolclass=pool.QueuePool,
    )

async_session = sessionmaker(async_engine, class_=AsyncSession)
session = sessionmaker(engine)
