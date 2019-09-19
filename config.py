import os

user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']
port = os.environ['PG_PORT']
db_name = os.environ['PG_DB_NAME']


class CarrosConfig:
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f'postgres://{user}:{password}@{host}:{port}/{db_name}'
    # SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s'.format(user, password, host, port, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
