class Configure(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://johnw:qwe123@sjdevetsecapp01:9000/csrf"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-never-guess'