import os

from .default import *

SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONN_STR')
# 'postgresql://username:password@localhost:5432/db_name'