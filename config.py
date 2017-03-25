import os

DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir,'sqlite')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(database_path, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

POST_PER_PAGE=15
SECRET_KEY='a2s3d4f5g6asdasd'