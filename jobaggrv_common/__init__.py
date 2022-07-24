
from configparser import ConfigParser
import os

def get_db_url():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(BASE_DIR, 'JobAggrV/conf/config.ini')
    config_obj = ConfigParser()
    config_obj.read(config_path)
    database_type = config_obj.get('database','type')
    if database_type == 'mysql':
        database_type = 'mysql+aiomysql'
    database_host = config_obj.get('database','host')
    database_port = config_obj.get('database','port')
    database_name = config_obj.get('database','name')
    database_user = config_obj.get('database','user')
    database_password = config_obj.get('database','password')
    return f'{database_type}://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}'

