
from passwords import \
    database_connection, \
    mailuser, \
    mailpass, \
    wtfkey
from dotenv import load_dotenv
import os
import redis

load_dotenv()
from sys import platform



# class ApplicationConfigProduction:
#     # databases info
#     SQLALCHEMY_DATABASE_URI_0 = database_connection

#     SQLALCHEMY_BINDS = {
#         'dbname': SQLALCHEMY_DATABASE_URI_0,
#     }
#     DEBUG = False



#     UPLOADED_FILES_DEST = ''

#     pythonpath = ''
#     bind = '0.0.0.0:5000'
#     proc_name = 'run:app'
#     workers = 4
#     worker_rlimit_nofile = 20000
#     worker_connections = 1024


#     # Mail
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 465
#     MAIL_USERNAME = mailuser
#     MAIL_PASSWORD = mailpass
#     MAIL_USE_SSL = True
#     MAIL_USE_TLS = False
#     MAIL_DEFAULT_SENDER = '"<site>.com" <site>@<site>.com>'

#     SESSION_TYPE = "redis"
#     SESSION_PERMANENT = False
#     SESSION_USE_SIGNER = True
#     SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")

#     UPLOADED_FILES_ALLOW = ['png', 'jpeg', 'jpg', 'png', 'gif']
#     MAX_CONTENT_LENGTH = 5 * 2500 * 2500
#     ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'png', 'gif']

#     # secret keys
#     SECRET_KEY = os.environ["SECRET_KEY"]
    
#     WTF_CSRF_TIME_LIMIT = None
#     WTF_CSRF_SECRET_KEY = wtfkey
#     WTF_CSRF_ENABLED = True


#     # sqlalchemy config
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     TRAP_HTTP_EXCEPTIONS = True
#     PROPAGATE_EXCEPTIONS = True

#     ALLOWED_HOSTS = [
#         '127.0.0.1',
#         '0.0.0.0'
#     ]

class ApplicationConfig:
    # databases info
    POSTGRES_USERNAME = 'name'
    POSTGRES_PW = 'password'
    POSTGRES_SERVER = '<ipaddress>:5432'
    POSTGRES_DBNAME00 = 'nameofdb'
    SQLALCHEMY_DATABASE_URI_0 = "postgresql+psycopg2://{}:{}@{}/{}".format(POSTGRES_USERNAME,
                                                                            POSTGRES_PW,
                                                                            POSTGRES_SERVER,
                                                                            POSTGRES_DBNAME00)
    SQLALCHEMY_BINDS = {'nameofdb': SQLALCHEMY_DATABASE_URI_0}

    DEBUG = True

    UPLOADED_FILES_DEST = ''


    pythonpath = ''
    bind = '0.0.0.0:7000'
    proc_name = 'runProduction:app'
    workers = 4
    worker_rlimit_nofile = 20000
    worker_connections = 1024



    # Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = mailuser
    MAIL_PASSWORD = mailpass
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
        MAIL_DEFAULT_SENDER = '"<site>.com" <site>@<site>.com>'

    # file uploads
    UPLOADED_FILES_ALLOW = ['png', 'jpeg', 'jpg', 'png', 'gif']
    MAX_CONTENT_LENGTH = 5 * 2500 * 2500
    ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'png', 'gif']

    # secret keys
    SECRET_KEY = os.environ["SECRET_KEY"]

    # sessions
    SESSION_COOKIE_NAME = "clearnet_session"
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")

    # CORS
    CORS_ORIGINS = "<ip>"
    CORS_SEND_WILDCARD = False
    CORS_SUPPORT_CREDENTIALS = True
    CORS_EXPOSE_HEADERS= None
    CORS_ALLOW_HEADERS= "<headers>"

    # sqlalchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TRAP_HTTP_EXCEPTIONS = True
    PROPAGATE_EXCEPTIONS = True

    ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0']
    CORS_ORIGIN_WHITELIST = ['*']
